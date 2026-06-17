from dotenv import load_dotenv
from services.zapi_service import enviar_mensagem

load_dotenv()

resposta = enviar_mensagem(
    "5598986290251",
    "Teste da integração Python + ZAPI"
)

print(resposta.status_code)
print(resposta.text)