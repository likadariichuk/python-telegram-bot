# python-telegram-bot
[Python telegram bot examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples)


Start with the simple Echo bot to test the connection. 
Echo bot replies with the same text that it receives from the client.

    pip install python-telegram-bot

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
        updater = Updater("Token")

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        updater.start_polling()

        updater.idle()


    if __name__ == '__main__':
        main()
    
To connect to Telegram you need a Token. Find BotFather in the search and text him /help. Follow the instructions to create a new bot. You will receive Token automatically after bot creation.  

![BotFather](https://user-images.githubusercontent.com/59927776/111807810-a5702800-88d3-11eb-995d-b6c89bc89c56.png)

Place your Token in the main() function:

    def main() -> None:
      """Start the bot."""
      updater = Updater("Token")
      
Run the file. Your bot should work and echo what you text.

![Echo](https://user-images.githubusercontent.com/59927776/111807880-b751cb00-88d3-11eb-9d7f-4084fb77a859.png)

Now we need to update echo() function to return custom text.
Rename echo() function to ask_bot() (make sure to change the name everywhere in the file):

    def ask_bot(update: Update, _: CallbackContext) -> None:
        response = bot(update.message.text)
        update.message.reply_text(response)
    
 bot() is a function that takes in the user's message; does something with it, and stores the result in **response** variable
        
Run the file. Your bot should reply with custom messages.👌🏼
