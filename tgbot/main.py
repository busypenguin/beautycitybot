import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Updater
from dispatcher import setup_dispatcher


def run_polling(telegram_api_key):
    """ Run bot in polling mode """

    # bot = Bot(token=telegram_api_key)
    updater = Updater(token=telegram_api_key)
    dispatcher = updater.dispatcher

    dispatcher = setup_dispatcher(dispatcher)

    print("Polling of bot has started")

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    load_dotenv()
    telegram_api_key = os.environ['TG_BOT_HTTP_KEY']
    run_polling(telegram_api_key)
