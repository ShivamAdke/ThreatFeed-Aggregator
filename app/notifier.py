import requests, os
from dotenv import load_dotenv

load_dotenv()
WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def send_alert(message):
    data = {"content": message}
    response = requests.post(WEBHOOK, json=data)
    return response.status_code