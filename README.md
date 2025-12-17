# White Label Support Hub

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-yellow.svg?style=flat-square)
![Framework](https://img.shields.io/badge/flask-2.0%2B-red.svg?style=flat-square)

> Uma plataforma web modular desenvolvida em Flask para gerenciamento de formulários de suporte técnico personalizados (White Label) para múltiplos clientes corporativos.

## 🎯 Visão Geral

O **White Label Support Hub** é uma solução SaaS (Software as a Service) projetada para centralizar a entrada de chamados de suporte de diferentes empresas em uma única infraestrutura. O sistema permite a renderização dinâmica de interfaces personalizadas baseadas na identidade visual e requisitos de cada cliente (ex: Auvo, ChatsHub), mantendo um *backend* unificado.

### ✨ Funcionalidades Principais

* **Arquitetura Multi-Tenant**: Suporte a múltiplas rotas personalizadas (`/auvo_15`, `/chatshub_16`) na mesma instância.
* **Formulários Dinâmicos**: Interfaces HTML5 responsivas adaptadas para coleta de dados específicos (IDs, anexos, descrições).
* **Integração de Mídia**: Suporte nativo para incorporação de tutoriais e documentação via iFrames.
* **Validação de Dados**: Front-end com validação de padrões (Regex) para telefones e e-mails corporativos.
* **Organização Modular**: Código estruturado utilizando Blueprints e Factory Pattern para escalabilidade.

## 🛠️ Tecnologias

* **Backend**: Python, Flask (Microframework).
* **Frontend**: HTML5, CSS3, Jinja2 Templating.
* **Teste**: Unittest/Pytest.
* **Deploy**: Compatível com Gunicorn/Nginx.

## 🚀 Instalação e Execução

### Pré-requisitos
* Python 3.x
* Pip

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/italofelipe01/whitelabel_site.git
cd whitelabel_site
```

2. **Crie um ambiente virtual (Opcional, mas recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
python run.py
```

5. **Acesse no navegador**
   * Landing Page: `http://localhost:5000/`
   * Portal Auvo: `http://localhost:5000/auvo_15`
   * Portal ChatsHub: `http://localhost:5000/chatshub_16`

## 🧪 Testes

Para executar os testes:

```bash
python -m unittest discover tests
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Ítalo Felipe Lira de Morais**
