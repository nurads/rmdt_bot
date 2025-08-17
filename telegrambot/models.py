# models.py
from django.db import models

class Contact(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    chat_id = models.BigIntegerField()
    bot_number = models.IntegerField(default=2)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    reg_completed = models.BooleanField(default=False)
    selected_class = models.CharField(max_length=100, blank=True, null=True)
    stream = models.CharField(max_length=50, blank=True, null=True)
    amount_to_pay = models.IntegerField(default=1000)


class Management(models.Model):
    registration_open = models.BooleanField(default=True)

    @classmethod
    def getInstance(cls):
        # Always return the first instance, or create if none
        instance, _ = cls.objects.get_or_create(id=1)
        return instance
