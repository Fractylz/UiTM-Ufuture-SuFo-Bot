import requests
import os
from dotenv import load_dotenv


# Config
load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv(
    "CHAT_ID"
)  # get this from sending a message to your bot and checking getUpdates


def send_text(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})


def send_photo(photo_path: str, caption: str = ""):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, "rb") as photo:
        requests.post(
            url, data={"chat_id": CHAT_ID, "caption": caption}, files={"photo": photo}
        )
