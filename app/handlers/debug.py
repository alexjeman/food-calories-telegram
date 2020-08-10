from telegram import *
from telegram.ext import *


def cb_echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


handlers = [
    MessageHandler(Filters.text, cb_echo),
]
