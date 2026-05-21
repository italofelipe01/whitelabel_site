import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from werkzeug.utils import secure_filename

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class TicketValidationError(ValueError):
    def __init__(self, errors):
        super().__init__("Invalid ticket payload")
        self.errors = errors


def create_ticket(app, tenant, form_data, uploaded_files):
    errors = {}
    payload = {}

    try:
        payload = _validate_payload(tenant, form_data)
    except TicketValidationError as exc:
        errors.update(exc.errors)

    try:
        _validate_file_fields(app, tenant, uploaded_files)
    except TicketValidationError as exc:
        errors.update(exc.errors)

    if errors:
        raise TicketValidationError(errors)

    attachments = _save_attachments(app, tenant, uploaded_files)

    ticket_id = uuid.uuid4().hex[:12]
    record = {
        "id": ticket_id,
        "tenant": tenant["slug"],
        "tenant_name": tenant["name"],
        "reseller_id": tenant["reseller_id"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "fields": payload,
        "attachments": attachments,
        "attachment": attachments.get("attachment"),
    }

    tickets_dir = Path(app.instance_path) / "tickets"
    tickets_dir.mkdir(parents=True, exist_ok=True)
    tickets_file = tickets_dir / "tickets.jsonl"
    with tickets_file.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, ensure_ascii=False) + "\n")

    return record


def _validate_payload(tenant, form_data):
    errors = {}
    payload = {}

    for field in tenant["fields"]:
        field_type = field["type"]
        if field_type == "file":
            continue

        name = field["name"]
        value = form_data.get(name, "").strip()

        if field.get("required") and not value:
            errors[name] = "Campo obrigatório."
            continue

        if not value:
            payload[name] = value
            continue

        if field_type == "email" and not EMAIL_PATTERN.fullmatch(value):
            errors[name] = "Informe um e-mail válido."
            continue

        if field_type == "tel" and field.get("pattern"):
            pattern = re.compile(f"^{field['pattern']}$")
            if not pattern.fullmatch(value):
                errors[name] = "Informe um telefone válido com DDD."
                continue

        if field_type == "number":
            try:
                numeric_value = int(value)
            except ValueError:
                errors[name] = "Informe um número válido."
                continue

            if "min" in field and numeric_value < field["min"]:
                errors[name] = f"Informe um valor maior ou igual a {field['min']}."
                continue

        if field_type == "select":
            allowed_values = {option["value"] for option in field.get("options", [])}
            if value not in allowed_values:
                errors[name] = "Selecione uma opção válida."
                continue

        if field.get("maxlength") and len(value) > field["maxlength"]:
            errors[name] = f"Use no máximo {field['maxlength']} caracteres."
            continue

        payload[name] = value

    if errors:
        raise TicketValidationError(errors)

    return payload


def _validate_file_fields(app, tenant, uploaded_files):
    errors = {}

    for field in tenant["fields"]:
        if field["type"] != "file":
            continue

        name = field["name"]
        file_storage = uploaded_files.get(name)
        has_file = bool(file_storage and file_storage.filename)

        if field.get("required") and not has_file:
            errors[name] = "Campo obrigatório."
            continue

        if has_file and not _is_allowed_file(app, file_storage.filename):
            errors[name] = "Formato de arquivo não permitido."

    if errors:
        raise TicketValidationError(errors)


def _save_attachments(app, tenant, uploaded_files):
    attachments = {}

    for field in tenant["fields"]:
        if field["type"] != "file":
            continue

        attachment = _save_attachment(app, tenant, uploaded_files.get(field["name"]))
        if attachment:
            attachments[field["name"]] = attachment

    return attachments


def _save_attachment(app, tenant, file_storage):
    if not file_storage or not file_storage.filename:
        return None

    filename = secure_filename(file_storage.filename)
    upload_dir = Path(app.instance_path) / "uploads" / tenant["slug"]
    upload_dir.mkdir(parents=True, exist_ok=True)

    stored_name = f"{uuid.uuid4().hex}_{filename}"
    stored_path = upload_dir / stored_name
    file_storage.save(stored_path)

    return {
        "original_name": file_storage.filename,
        "stored_name": stored_name,
        "path": str(stored_path),
    }


def _is_allowed_file(app, filename):
    safe_name = secure_filename(filename)
    extension = safe_name.rsplit(".", 1)[-1].lower() if "." in safe_name else ""
    return bool(extension and extension in app.config["ALLOWED_UPLOAD_EXTENSIONS"])
