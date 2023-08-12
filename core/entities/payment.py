from django.db import models
from . import get_declension
from .assignment import Assignment


class Payment(models.Model):
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        verbose_name='назначение'
    )
    volume = models.IntegerField(
        'количество тренировок',
        default=0
    )
    dt = models.DateTimeField('дата и время оплаты')
    image_width = models.IntegerField(
        'ширина картинки',
        blank=True
    )
    image_height = models.IntegerField(
        'высота картики',
        blank=True
    )
    receipt = models.ImageField(
        'фотография чека',
        upload_to='receipts/%Y/',
        width_field='image_width',
        height_field='image_height'
    )
    _training_declension = staticmethod(get_declension(
        'тренировка',
        'тренировки',
        'тренировок'
    ))

    def __str__(self):
        declension = self._training_declension(
            getattr(self, 'volume')
        )
        return f'{self.volume} {declension} - {self.assignment}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'платежи'
