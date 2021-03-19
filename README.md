# python-telegram-bot
[Python telegram bot examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples)


Start with the simple Echo bot to test the connection. 
Echo bot replies with the same text that it receives from the client.

Create telegram-bot.py file:

    from telegram import Update
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

    def start(update: Update, _: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        update.message.reply_text('Hi!')


    def help_command(update: Update, _: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help!')


    def echo(update: Update, _: CallbackContext) -> None:
        update.message.reply_text(update.message.text)


    def main() -> None:
        """Start the bot."""
        updater = Updater("1773606014:AAFFffgjGc6aS9bHvN18VlJsqyCQjaY2pSE")

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        updater.start_polling()

        updater.idle()


    if __name__ == '__main__':
        main()
    
To connect to telegram you need a Token. Find BotFather in the search and text him.
You need to create a new bot. Text /help. Follow the instructions to create a new bot. You will receive token automatically after bot creation.

    pip install python-telegram-bot

Your Token goes in to the main() function:

    def main() -> None:
      """Start the bot."""
      updater = Updater("1773606014:AAFFffgjGc6aS9bHvN18VlJsqyCQjaY2pSE")

Now, let's update echo function to reply custom messages.
Rename it to ask_bot (make sure to change the name evrywhere in the file):

    def ask_bot(update: Update, _: CallbackContext) -> None:
    response = bot(update.message.text)
    
 bot() is a function the takes the user's message; does something with it; and store the result in response variable
    update.message.reply_text(response)
    
Run the file. Your bot should reply with custom messages.👌🏼
