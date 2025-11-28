# White Label Support Hub

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=flat-square)
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

## 🛠️ Tecnologias

* **Backend**: Python, Flask (Microframework).
* **Frontend**: HTML5, CSS3, Jinja2 Templating.
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

2. **Instale as dependências**
```bash
pip install flask
```

3. **Execute a aplicação**
```bash
python meu_site.py
```

4. **Acesse no navegador**
   * Landing Page: `http://localhost:5000/`
   * Portal Auvo: `http://localhost:5000/auvo_15`
   * Portal ChatsHub: `http://localhost:5000/chatshub_16`

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Ítalo Felipe Lira de Morais**

---

**Nota:** Corrigi a formatação dos blocos de código no markdown. Agora todos os snippets bash estão devidamente formatados com a sintaxe correta de três acentos graves, garantindo que sejam renderizados corretamente como blocos de código.
