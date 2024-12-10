import requests
import os
from dotenv import load_dotenv

# load the .env variables
load_dotenv()


bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
message = "HERE IS THE MESSAGE"
def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code}")
        print(response.json())


# sends the message
send_message(bot_token, chat_id, message)
