from django.db import models



class Degree(models.Model):
    """Показатель разновидности - степень"""
    TYPE_OF_BUSINESS_PROCESS = [
        ('M', 'Управления'),
        ('B', 'Основные'),
        ('A', 'Вспомогательные'),
    ]
    name = models.CharField('Наименование показателя - степень', max_length=200)
    description = models.TextField('Описание', null=True)
    applying = models.BooleanField('Соответствие деятельности организации', default=False, null=True, blank=True)
    question = models.TextField('Вопрос', null=True)
    multiple_answer = models.BooleanField('Множественный ответ', null=False)
    business_process = models.CharField('Вид бизнес-процесса', choices=TYPE_OF_BUSINESS_PROCESS, max_length=20, null=True, blank=True)


    class Meta:
        verbose_name = 'Показатель - степень'
        verbose_name_plural = 'Показатели - степень'

    def __str__(self):
        return self.name


class AnswerChoice(models.Model):
    """Вариант ответа"""
    answer = models.CharField('Ответ', max_length=500)
    question = models.ForeignKey(Degree, verbose_name='Вопрос', on_delete=models.SET_NULL, null=True)
    choise = models.BooleanField('Выбор', default=False, null=True, blank=True)
    value = models.SmallIntegerField('Значения для расчета', null=False)


    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.answer
