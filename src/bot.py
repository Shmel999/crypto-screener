import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

class Bot:
    def __init__(self, token: str):
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher
        self.setup_handlers()

    def setup_handlers(self):
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('stop', self.stop))

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text('Bot has started!')
        logging.info('Bot started')

    def stop(self, update: Update, context: CallbackContext):
        update.message.reply_text('Bot is stopping...')
        logging.info('Bot stopped')
        self.updater.stop()

    def run(self):
        logging.info('Bot is running...')
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    import os
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = Bot(TOKEN)
    bot.run()