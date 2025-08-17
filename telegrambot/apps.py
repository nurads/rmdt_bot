from django.apps import AppConfig

class TelegrambotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegrambot'

    def ready(self):
        # Leave empty for now, do NOT import bot here
        pass
