import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": text
        }
    )

    return response.json()


print("Price Drop Bot started!")
