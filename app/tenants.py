COMMON_SUPPORT_FIELDS = [
    {
        "name": "requester_name",
        "label": "Nome do solicitante",
        "type": "text",
        "required": True,
        "placeholder": "Nome Sobrenome",
        "autocomplete": "name",
    },
    {
        "name": "requester_email",
        "label": "E-mail do solicitante",
        "type": "email",
        "required": True,
        "placeholder": "email@empresa.com",
        "autocomplete": "email",
    },
    {
        "name": "customer_name",
        "label": "Nome do cliente",
        "type": "text",
        "required": True,
        "placeholder": "Nome Sobrenome",
    },
    {
        "name": "customer_email",
        "label": "E-mail do cliente",
        "type": "email",
        "required": True,
        "placeholder": "cliente@empresa.com",
    },
    {
        "name": "customer_phone",
        "label": "Telefone do cliente",
        "type": "tel",
        "required": True,
        "placeholder": "(62) 99999-9999",
        "pattern": r"\(?[0-9]{2}\)?\s?[0-9]{4,5}-?[0-9]{4}",
        "hint": "Use DDD e telefone. Exemplo: (62) 99999-9999.",
    },
    {
        "name": "company_name",
        "label": "Nome da empresa",
        "type": "text",
        "required": True,
        "placeholder": "Empresa LTDA",
    },
    {
        "name": "customer_id",
        "label": "ID do cliente",
        "type": "number",
        "required": True,
        "placeholder": "12345",
        "min": 1,
    },
    {
        "name": "issue_type",
        "label": "Tipo de solicitação",
        "type": "select",
        "required": True,
        "options": [
            {"value": "bug", "label": "Erro ou falha"},
            {"value": "access", "label": "Acesso ou login"},
            {"value": "billing", "label": "Financeiro"},
            {"value": "question", "label": "Dúvida operacional"},
            {"value": "other", "label": "Outro"},
        ],
    },
    {
        "name": "priority",
        "label": "Prioridade",
        "type": "select",
        "required": True,
        "options": [
            {"value": "normal", "label": "Normal"},
            {"value": "high", "label": "Alta"},
            {"value": "urgent", "label": "Urgente"},
        ],
    },
    {
        "name": "issue_summary",
        "label": "Descrição do problema",
        "type": "textarea",
        "required": True,
        "placeholder": "Descreva o que aconteceu, quando começou e o impacto para o cliente.",
        "rows": 7,
        "maxlength": 4000,
    },
    {
        "name": "attachment",
        "label": "Anexo",
        "type": "file",
        "required": False,
        "accept": ".csv,.doc,.docx,.jpeg,.jpg,.pdf,.png,.txt,.xls,.xlsx,.zip",
        "hint": "Arquivos ate 8 MB nos formatos permitidos.",
    },
]


TENANTS = {
    "auvo_15": {
        "slug": "auvo_15",
        "name": "Auvo",
        "reseller_id": "15",
        "headline": "Solicitar suporte Auvo",
        "description": "Registre uma solicitação para que o time de suporte analise o caso com as informações corretas.",
        "accent_color": "#1d6fd3",
        "logo": {
            "src": "img/auvo.svg",
            "alt": "Auvo",
        },
        "media_url": "https://drive.google.com/file/d/1RM5dImT6en9xG7OXC8k_L8q83ULjTCKr/preview",
        "fields": COMMON_SUPPORT_FIELDS,
    },
    "chatshub_16": {
        "slug": "chatshub_16",
        "name": "ChatsHub",
        "reseller_id": "16",
        "headline": "Solicitar suporte ChatsHub",
        "description": "Envie os dados do atendimento para abertura e triagem do chamado.",
        "accent_color": "#148a7a",
        "logo": {
            "src": "img/chatshub.svg",
            "alt": "ChatsHub",
        },
        "media_url": "https://drive.google.com/file/d/1QNeRmMTD79xs7_9NTJ1oBfCeBVsd7Mle/preview",
        "fields": COMMON_SUPPORT_FIELDS
        + [
            {
                "name": "channel",
                "label": "Canal afetado",
                "type": "select",
                "required": False,
                "options": [
                    {"value": "whatsapp", "label": "WhatsApp"},
                    {"value": "instagram", "label": "Instagram"},
                    {"value": "webchat", "label": "Webchat"},
                    {"value": "other", "label": "Outro"},
                ],
            }
        ],
    },
}


def get_tenant(slug):
    return TENANTS.get(slug)


def list_tenants():
    return list(TENANTS.values())
