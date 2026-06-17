from dotenv import load_dotenv
from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem

load_dotenv()

contatos = buscar_contatos()

for contato in contatos:

    nome = contato["nome"]
    telefone = contato["telefone"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    resposta = enviar_mensagem(
        telefone,
        mensagem
    )

    print(
        f"Mensagem enviada para {nome}: {resposta.status_code}"
    )