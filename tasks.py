from celery import shared_task
import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = 'YOUR_CHAT_ID_HERE'  # Replace or dynamically collect

@shared_task
def send_welcome_message(username):
    if not TOKEN:
        return 'Telegram token not set.'
    message = f"Welcome {username} to our platform!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)