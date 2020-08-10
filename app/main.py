import logging
import itertools

from telegram.ext import Updater

from app import config
from app.handlers import debug


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # noqa
    level=logging.DEBUG
)


updater = Updater(
    token=config.BOT_TOKEN,
    use_context=True
)


# Set handlers here...
for handler in itertools.chain(
    debug.handlers,
):
    updater.dispatcher.add_handler(handler)


# Use polling if BOT_DEBUG is True
if config.BOT_DEBUG:
    updater.start_polling()
else:
    updater.start_webhook(
        listen=config.WEBHOOK_HOST,
        port=config.WEBHOOK_PORT,
        url_path=config.WEBHOOK_PATH,
    )
    updater.bot.set_webhook(
        url=config.WEBHOOK_URL,
    )


updater.idle()
