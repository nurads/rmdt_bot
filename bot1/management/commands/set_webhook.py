from typing import Any
from django.core.management import BaseCommand, CommandError
from django.core.management.base import CommandParser

from bot1.bot import bot
from bot1.bot2 import bot as bot2


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--bot", type=int)

    def handle(self, *args: Any, **options: Any):
        bot_number = options.get("bot")
        if bot_number == 1:
            bot.set_webhook("https://rmdt-bot.vercel.app/bot1/")
        elif bot_number == 2:
            bot2.set_webhook("https://rmdt-bot.vercel.app/bot2/")
