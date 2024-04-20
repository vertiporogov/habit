from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=300, verbose_name='имя', **NULLABLE)
    is_active = models.BooleanField(default=True)
    chat_id = models.CharField(max_length=100, verbose_name='чат айди телеграмм', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
