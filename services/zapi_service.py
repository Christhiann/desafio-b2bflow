import os
import requests

def enviar_mensagem(numero: str, mensagem: str):

    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")

    url = (
        f"https://api.z-api.io/instances/"
        f"{instance_id}/token/{token}/send-text"
    )

    payload = {
        "phone": numero,
        "message": mensagem
    }

    response = requests.post(
        url,
        json=payload
    )

    return response