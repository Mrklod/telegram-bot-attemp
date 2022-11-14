import logging
from telegram.ext import *

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(updater:Updater, context:CallbackContext):
    mytext = "Привіт {}".format(updater.message.chat.first_name)
    updater.message.reply_text(mytext)

def chat(updater:Updater, context:CallbackContext):
    text = 'hi'

    updater.message.reply_text(text)

def main():
    update = Updater('5668214541:AAFoa7JzrDib1aD0SM0C2al4J_GsxK6gbYU')

    update.dispatcher.add_handler(CommandHandler('start',start_bot))
    update.dispatcher.add_handler(MessageHandler(Filters.text,chat))

    update.start_polling()
    update.idle()

if __name__ == '__main__':
    logging.info('Bot start')
    main()