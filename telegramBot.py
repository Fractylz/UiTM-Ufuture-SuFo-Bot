import requests

BOT_TOKEN = "8275693340:AAE1vx5O2JSxVRNQ_le7BCKw93w5_x_Swro"
CHAT_ID = (
    "1922524521"  # get this from sending a message to your bot and checking getUpdates
)


def send_text(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})


def send_photo(photo_path: str, caption: str = ""):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, "rb") as photo:
        requests.post(
            url, data={"chat_id": CHAT_ID, "caption": caption}, files={"photo": photo}
        )
