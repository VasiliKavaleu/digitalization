from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """User."""
    username = None
    email = models.EmailField('Email адрес', unique=True)
    organisation = models.CharField('Организация', max_length=100)
    industry = models.ForeignKey('Industry', verbose_name='Отрасль', on_delete=models.SET_NULL, null=True)

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
    digit_value_main_bp = models.IntegerField('Цифровизация основных БП', null=True, blank=True)
    digit_value_manage_bp = models.IntegerField('Цифровизация БП управления', null=True, blank=True)
    digit_value_auxiliary_bp = models.IntegerField('Цифровизация вспомогательных БП', null=True, blank=True)

    class Meta:
        verbose_name = 'Результат измерений'
        verbose_name_plural = 'Результаты измерений'

    def __str__(self):
        return self.user.organisation + ' ' + str(self.date_added)

class IndicatorMainBP(models.Model):
    total_digitalization_value = models.ForeignKey('UserResultDigitalization', verbose_name='Показатели основных БП', on_delete=models.CASCADE)
    name = models.TextField('Частный показатель основных БП')
    value_of_indicator = models.DecimalField('Значение частного показателя', max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = 'Частный показатель основных БП'
        verbose_name_plural = 'Частные показатели основных БП'

    def __str__(self):
        return self.total_digitalization_value.user.organisation

class IndicatorManageBP(models.Model):
    total_digitalization_value = models.ForeignKey('UserResultDigitalization', verbose_name='Показатель БП управления', on_delete=models.CASCADE)
    name = models.TextField('Частный показатель БП управления')
    value_of_indicator = models.DecimalField('Значение частного показателя', max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = 'Частный показатель БП управления'
        verbose_name_plural = 'Частные показатели БП управления'

    def __str__(self):
        return self.total_digitalization_value.user.organisation

class IndicatorAuxiliaryBP(models.Model):
    total_digitalization_value = models.ForeignKey('UserResultDigitalization', verbose_name='Показатель вспомогальных БП', on_delete=models.CASCADE)
    name = models.TextField('Частный показатель БП управления')
    value_of_indicator = models.DecimalField('Значение частного показателя', max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = 'Частный показатель вспомогательных БП'
        verbose_name_plural = 'Частные показатели вспомогательных БП'

    def __str__(self):
        return self.total_digitalization_value.user.organisation


class Industry(models.Model):
    name = models.TextField('Отрасль')

    class Meta:
        verbose_name = 'Отрасль/функциональная сфера'
        verbose_name_plural = 'Отрасли/функциональные сферы'

    def __str__(self):
        return self.name
