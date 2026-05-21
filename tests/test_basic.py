import json
import shutil
import unittest
import uuid
from io import BytesIO
from pathlib import Path

from app import create_app


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        root_dir = Path(__file__).resolve().parents[1]
        self.instance_dir = (
            root_dir / ".test-instance" / f"{self._testMethodName}-{uuid.uuid4().hex}"
        )
        shutil.rmtree(self.instance_dir, ignore_errors=True)
        self.instance_dir.mkdir(parents=True, exist_ok=True)
        self.app = create_app("testing")
        self.app.instance_path = str(self.instance_dir)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        shutil.rmtree(self.instance_dir, ignore_errors=True)

    def test_landing_page_lists_tenants(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Auvo", response.get_data(as_text=True))
        self.assertIn("ChatsHub", response.get_data(as_text=True))

    def test_tenant_form_route(self):
        response = self.client.get("/auvo_15")
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Solicitar suporte Auvo", html)
        self.assertIn('name="customer_id"', html)
        self.assertIn("auvo.svg", html)

    def test_chatshub_form_has_custom_field(self):
        response = self.client.get("/chatshub_16")
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Canal afetado", html)
        self.assertIn("chatshub.svg", html)

    def test_unknown_tenant_returns_404(self):
        response = self.client.get("/tenant_inexistente")

        self.assertEqual(response.status_code, 404)

    def test_valid_ticket_submission_creates_record(self):
        response = self.client.post("/auvo_15/suporte", data=_valid_payload())

        self.assertEqual(response.status_code, 302)
        self.assertIn("/auvo_15/sucesso/", response.headers["Location"])

        tickets_file = self.instance_dir / "tickets" / "tickets.jsonl"
        record = json.loads(tickets_file.read_text(encoding="utf-8").strip())

        self.assertEqual(record["tenant"], "auvo_15")
        self.assertEqual(record["reseller_id"], "15")
        self.assertEqual(record["fields"]["customer_id"], "12345")
        self.assertIsNone(record["attachment"])

    def test_invalid_submission_renders_field_errors(self):
        payload = _valid_payload()
        payload["requester_email"] = "email-invalido"

        response = self.client.post("/auvo_15/suporte", data=payload)
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 422)
        self.assertIn("Informe um e-mail válido.", html)

    def test_invalid_attachment_extension_is_rejected(self):
        payload = _valid_payload()
        payload["attachment"] = (BytesIO(b"payload"), "script.exe")

        response = self.client.post(
            "/auvo_15/suporte",
            data=payload,
            content_type="multipart/form-data",
        )

        self.assertEqual(response.status_code, 422)
        self.assertIn(
            "Formato de arquivo não permitido.", response.get_data(as_text=True)
        )


def _valid_payload():
    return {
        "requester_name": "Joao Silva",
        "requester_email": "joao@example.com",
        "customer_name": "Maria Souza",
        "customer_email": "maria@example.com",
        "customer_phone": "(62) 99999-9999",
        "company_name": "Empresa LTDA",
        "customer_id": "12345",
        "issue_type": "bug",
        "priority": "normal",
        "issue_summary": "Sistema apresenta erro ao abrir a tela inicial.",
    }
