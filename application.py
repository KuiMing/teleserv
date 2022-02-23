from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, MessageHandler, Filters
import logging
import os


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
TOKEN = os.getenv("ACCESS_TOKEN")

BOT = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route("/")
def hello():
    "hello world"
    return "Hello World!!!!!"

@app.route("/callback", methods=['POST'])
def callback() -> str:
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), BOT)
        dispatcher.process_update(update)
    return 'ok'


def reply_handler(bot, update) -> None:
    text = update.message.text
    update.message.reply_text(text)

dispatcher = Dispatcher(BOT, None)
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
