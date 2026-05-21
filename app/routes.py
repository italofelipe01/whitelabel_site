import secrets

from flask import (
    Blueprint,
    abort,
    current_app,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.exceptions import RequestEntityTooLarge

from app.tenants import get_tenant, list_tenants
from app.tickets import TicketValidationError, create_ticket

main = Blueprint("main", __name__)


@main.get("/")
def landing_page():
    return render_template("landing_page.html", tenants=list_tenants())


@main.get("/<tenant_slug>")
def support_form(tenant_slug):
    tenant = get_tenant(tenant_slug)
    if tenant is None:
        abort(404)

    return render_template(
        "support_form.html",
        csrf_token=_get_csrf_token(tenant_slug),
        errors={},
        form_values={},
        tenant=tenant,
    )


@main.post("/<tenant_slug>/suporte")
def submit_support_form(tenant_slug):
    tenant = get_tenant(tenant_slug)
    if tenant is None:
        abort(404)

    if not _is_valid_csrf_token(tenant_slug, request.form.get("_csrf_token")):
        abort(400)

    try:
        ticket = create_ticket(current_app, tenant, request.form, request.files)
    except TicketValidationError as exc:
        return (
            render_template(
                "support_form.html",
                csrf_token=_get_csrf_token(tenant_slug),
                errors=exc.errors,
                form_values=request.form,
                tenant=tenant,
            ),
            422,
        )

    return redirect(
        url_for(
            "main.ticket_success",
            tenant_slug=tenant_slug,
            ticket_id=ticket["id"],
        )
    )


@main.get("/<tenant_slug>/sucesso/<ticket_id>")
def ticket_success(tenant_slug, ticket_id):
    tenant = get_tenant(tenant_slug)
    if tenant is None:
        abort(404)

    return render_template("success.html", tenant=tenant, ticket_id=ticket_id)


@main.app_errorhandler(RequestEntityTooLarge)
def handle_file_too_large(error):
    return (
        render_template(
            "error.html",
            message="O arquivo enviado ultrapassa o limite permitido.",
            status_code=413,
        ),
        413,
    )


def _get_csrf_token(tenant_slug):
    key = f"csrf_token:{tenant_slug}"
    if key not in session:
        session[key] = secrets.token_urlsafe(32)
    return session[key]


def _is_valid_csrf_token(tenant_slug, token):
    if not current_app.config.get("WTF_CSRF_ENABLED", True):
        return True

    expected_token = session.get(f"csrf_token:{tenant_slug}")
    return bool(
        token and expected_token and secrets.compare_digest(token, expected_token)
    )
