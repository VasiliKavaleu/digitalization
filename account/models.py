from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """User."""
    username = None
    email = models.EmailField('Email адрес', unique=True)
    organisation = models.CharField('Организация', max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class UserResultDigitalization(models.Model):
    """Result of culculating value."""
    user = models.ForeignKey('CustomUser', verbose_name='Организация', on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField('', auto_now_add=True)
    digitalization = models.IntegerField('Цифровизация', null=True, blank=True)

    class Meta:
        verbose_name = 'Результат измерений'
        verbose_name_plural = 'Результаты измерений'

    def __str__(self):
        return self.user.organisation

