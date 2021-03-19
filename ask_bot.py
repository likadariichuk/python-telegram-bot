from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot import bot

def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def ask_bot(update: Update, _: CallbackContext) -> None:
    response = bot(update.message.text)
    update.message.reply_text(response)


def main() -> None:
    """Start the bot."""
    updater = Updater("Token")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ask_bot))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()