import logging
import os
from dotenv import load_dotenv
from bot import CryptoScreenerBot

load_dotenv()

logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    bot = CryptoScreenerBot(os.getenv('TELEGRAM_BOT_TOKEN'))
    bot.start()