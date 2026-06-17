# Desafio B2BFlow

## Objetivo

Desenvolver uma aplicação Python capaz de buscar contatos armazenados no Supabase e enviar mensagens personalizadas via WhatsApp utilizando a API da Z-API.

A mensagem enviada segue o formato:

```text
Olá, <nome_contato> tudo bem com você?
```

## Tecnologias

* Python 3.11
* Supabase
* Z-API
* Requests
* Python Dotenv
* Logging

## Estrutura do Projeto

```text
desafio-b2bflow/
│
├── main.py
├── logger_config.py
├── requirements.txt
├── .env.example
├── .gitignore
│
└── services/
    ├── supabase_service.py
    └── zapi_service.py
```

## Configuração do .env

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Como Executar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd desafio-b2bflow
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o arquivo .env

Preencha as variáveis de ambiente com os dados do seu projeto Supabase e da sua instância Z-API.

### 4. Execute a aplicação

```bash
python main.py
```

## Fluxo da Aplicação

```text
Supabase
   ↓
Busca de contatos
   ↓
Python
   ↓
Personalização da mensagem
   ↓
Z-API
   ↓
WhatsApp
```

## Exemplo de Mensagem

```text
Olá, Christhian tudo bem com você?
```
