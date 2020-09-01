from django.db import models


class Degree(models.Model):
    """Indicator degree type."""
    name = models.TextField('Наименование частного показателя')
    description = models.TextField('Описание', blank=True)
    question = models.TextField('Вопрос', blank=True)
    multiple_answer = models.BooleanField('Предпологает множественный ответ', null=False)
    indicator_of_share = models.BooleanField('Показатель доля', null=False)

    class Meta:
        verbose_name = 'Частный показатель'
        verbose_name_plural = 'Частные показатели'

    def __str__(self):
        return self.name


class AnswerChoice(models.Model):
    """Answer choice for indicator Degree."""
    answer = models.TextField('Ответ')
    question = models.ForeignKey(Degree, verbose_name='Показатель', on_delete=models.SET_NULL, null=True)
    value = models.FloatField('Значения для расчета', null=False)

    class Meta:
        verbose_name = 'Вариант ответа для показателя - степень'
        verbose_name_plural = 'Варианты ответа для показателя - степень'

    def __str__(self):
        return self.answer


class AnswerInput(models.Model):
    """Answer input type for indicator share."""
    question = models.ForeignKey(Degree, verbose_name='Вопрос', on_delete=models.SET_NULL, null=True)
    quantity = models.TextField('Вопрос для для определения доли')
    total_quantity = models.TextField('Вопрос для определения общего количества')


    class Meta:
        verbose_name = 'Рассчетные значения для показателя - доля'
        verbose_name_plural = 'Рассчетные значения для показателя - доля'

    def __str__(self):
        return self.quantity