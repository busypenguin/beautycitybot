from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Service(models.Model):
    """Услуга."""

    name = models.CharField(
        max_length=100,
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Saloon(models.Model):
    """Салон красоты."""

    name = models.CharField(
        max_length=100,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='saloons',
    )
    services = models.ManyToManyField(
        Service,
        related_name='saloons',
        blank=True,
    )


class Master(models.Model):
    """Мастер."""

    name = models.CharField(
        max_length=100,
    )
    services = models.ManyToManyField(
        Service,
        related_name='masters',
        blank=True,
    )
    saloons = models.ManyToManyField(
        Service,
        related_name='masters',
        blank=True,
    )


class Sign(models.Model):
    """Запись."""

    saloon = models.ForeignKey(
        Saloon,
        on_delete=models.CASCADE,
        related_name='signs'
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='signs'
    )
    client = models.ForeignKey(
        Saloon,
        on_delete=models.CASCADE,
        related_name='signs'
    )
    time = models.TimeField()
