# White Label Support Hub

Plataforma Flask para criação de portais whitelabel de suporte. Cada rota pública
representa um tenant com identidade visual, mídia de apoio, campos personalizados e
regras de validação próprias.

## Funcionalidades

- Hub inicial com os portais disponíveis.
- Rotas whitelabel configuráveis, como `/auvo_15` e `/chatshub_16`.
- Formulário único renderizado a partir da configuração do tenant.
- Campos dinâmicos: texto, e-mail, telefone, número, seleção, área de texto e anexo.
- Processamento de submissão em `/<tenant>/suporte`.
- Registro local dos chamados em `instance/tickets/tickets.jsonl`.
- Upload seguro com nomes sanitizados, limite de tamanho e extensões permitidas.
- Logos isolados em molduras responsivas para preservar a estética da página.
- Testes cobrindo rotas, campos customizados, validação e criação de chamado.

## Estrutura Principal

```text
app/
  routes.py              # Rotas do hub, formulário, submissão e sucesso
  tenants.py             # Catálogo de clientes e campos por tenant
  tickets.py             # Validação, upload e persistência local do chamado
  templates/
    base.html
    landing_page.html
    support_form.html
    success.html
    error.html
  static/
    css/style.css
    img/
      auvo.svg
      chatshub.svg
```

## Como Adicionar um Cliente

Inclua uma entrada em `app/tenants.py`:

```python
"cliente_99": {
    "slug": "cliente_99",
    "name": "Cliente",
    "reseller_id": "99",
    "headline": "Solicitar suporte Cliente",
    "description": "Texto exibido no painel lateral.",
    "accent_color": "#1d6fd3",
    "logo": {"src": "img/cliente.svg", "alt": "Cliente"},
    "media_url": "https://drive.google.com/file/d/.../preview",
    "fields": COMMON_SUPPORT_FIELDS + [
        {
            "name": "campo_extra",
            "label": "Campo extra",
            "type": "text",
            "required": False,
        }
    ],
}
```

Adicione o arquivo de logo em `app/static/img/`. O layout limita largura, altura e
usa `object-fit: contain`, então imagens horizontais ou quadradas não devem
quebrar o formulário.

## Execução Local

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Acesse:

- `http://localhost:5000/`
- `http://localhost:5000/auvo_15`
- `http://localhost:5000/chatshub_16`

## Configuração

Variáveis úteis:

- `FLASK_CONFIG`: `development`, `testing` ou `production`.
- `SECRET_KEY`: obrigatória em produção.
- `MAX_CONTENT_LENGTH`: limite máximo de upload em bytes. Padrão: 8 MB.

Em produção, execute com Gunicorn ou outro servidor WSGI:

```bash
FLASK_CONFIG=production SECRET_KEY=sua-chave gunicorn run:app
```

## Testes e Qualidade

```bash
python -m pytest
python -m black --check .
python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Próximos Passos Recomendados

- Trocar persistência local por banco de dados.
- Enviar chamados para uma API, webhook, e-mail ou ferramenta de help desk.
- Adicionar autenticação administrativa para listar/exportar chamados.
- Adicionar captcha ou rate limit caso o formulário fique público na internet.
- Guardar anexos em storage externo com política de retenção.
