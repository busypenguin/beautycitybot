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
        blank=True,
        related_name='saloons',
    )
    services = models.ManyToManyField(
        Service,
        related_name='saloons',
        blank=True,
    )

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


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
        related_name='saloon_masters',
        blank=True,
    )

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Sign(models.Model):
    """Запись."""

    saloon = models.ForeignKey(
        Saloon,
        on_delete=models.CASCADE,
        related_name='saloon_signs'
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='master_signs'
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='client_signs'
    )
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ('start',)

    def __str__(self) -> str:
        return (
            f'{self.client} записан в салон {self.saloon}'
            f' к мастеру {self.master}'
        )
