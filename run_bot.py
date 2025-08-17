import os
import django
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "botproject.settings")
django.setup()

from telegrambot.bot import bot   # now this works ✅

if __name__ == "__main__":
    bot.polling(non_stop=True)
