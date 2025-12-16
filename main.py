import logging
import config

from telegram.ext import (
    Application,
    CommandHandler
    )
from bot import start
from logger import setup_logging

setup_logging(level=logging.DEBUG)

def main() -> None:
    if not config.BOT_TOKEN:
        raise RuntimeError("empty BOT_TOKEN")

    application = Application.builder().token(config.BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    logging.getLogger(__name__).info("bot is up")
    application.run_polling()

if __name__ == "__main__":
    main()
