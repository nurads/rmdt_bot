from typing import Any
from django.core.management import BaseCommand, CommandError
from django.core.management.base import CommandParser

from bot1.bot import bot


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> str | None:
        bot.set_webhook("https://")
