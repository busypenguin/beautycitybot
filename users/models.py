from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        max_length=50,
        unique=True
    )
    first_name = models.CharField(
        max_length=50,
    )
    phone_number = models.CharField(
        max_length=20,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username', )

    def __str__(self):
        return self.username
