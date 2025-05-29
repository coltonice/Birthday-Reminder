import requests

BOT_TOKEN = "HIDDEN"
CHAT_ID = "7704002914"

message = "🚨 Telegram test: If you see this, your bot is working!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)
print(response.status_code)
print(response.json())
