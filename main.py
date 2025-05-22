import json
import requests
from datetime import datetime, timedelta
import schedule
import time

# 🔧 Replace these with your actual values
BOT_TOKEN = "8189815354:AAGPgXUZlQp4e3aUSpTYY_bbYJv9Uc-9I10"
CHAT_ID = "7704002914"

def load_birthdays():
    """Load birthday entries from the JSON file."""
    with open('birthdays.json', 'r') as file:
        return json.load(file)

def send_telegram_message(message):
    """Send a message using Telegram Bot."""
    url = f"https://api.telegram.org/bot{8189815354:AAGPgXUZlQp4e3aUSpTYY_bbYJv9Uc-9I10}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("Failed to send message:", response.text)

def check_birthdays():
    """Check for birthdays today or in 7 days, and notify."""
    today = datetime.today().strftime('%m-%d')
    upcoming = (datetime.today() + timedelta(days=7)).strftime('%m-%d')
    birthdays = load_birthdays()

    for person in birthdays:
        name = person['name']
        bday = person['birthday']
        if bday == today:
            send_telegram_message(f"🎉 Today is {name}'s birthday!")
        elif bday == upcoming:
            send_telegram_message(f"📅 {name}'s birthday is in 7 days!")

# Check every day at 9 AM
schedule.every().day.at("09:00").do(check_birthdays)

print("Birthday reminder is running...")

while True:
    schedule.run_pending()
    time.sleep(60)
