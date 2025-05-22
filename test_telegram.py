import requests

BOT_TOKEN = "8189815354:AAGPgXUZlQp4e3aUSpTYY_bbYJv9Uc-9I10"
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
