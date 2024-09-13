from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


# Create your models here.
class Contact(models.Model):
    tg_id = models.BigIntegerField()
    bot_number = models.PositiveSmallIntegerField(default=1)
    chat_id = models.BigIntegerField()
    phone_number = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255, null=True, blank=True)
    stream = models.CharField(max_length=255, default="General")
    reg_completed = models.BooleanField(default=False)
    join_approved = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    selected_class = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self) -> str:
        return f"{self.first_name}:{self.tg_id}"


class Management(models.Model):
    name = models.CharField(default="Admin")
    registration_open = models.BooleanField(default=True)

    @staticmethod
    def getInstance():
        return Management.objects.get_or_create(pk=1)[0]

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admin"

    def __str__(self) -> str:
        return "Admin:{self.pk:02d}"
