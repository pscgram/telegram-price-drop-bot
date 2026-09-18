import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHANNEL_ID,
    "text": "🤖 Price Drop Bot is working! ✅"
}

response = requests.post(url, json=data)

print(response.json())
