from django.db import models

TIER_AS_WORD = [
    'нулевая', 'первая', 'вторая', 'трет', 'четвертая',
    'пятая', 'шестая', 'седьмая', 'восьмая', 'девятая',
    'десятая', 'одиннадцатая', 'двенадцатая',
    'тринадцатая', 'четырнадцатая', 'пятнадцатая',
    'шестнадцатая', 'семнадцатая', 'восемендцатая',
]


class Tier(models.Model):
    number = models.PositiveIntegerField(
        'номер уровня испытаний',
        unique=True
    )
    starting_age = models.IntegerField(
        'минимальный возраст',
        blank=True,
        null=True
    )
    boundary_age = models.IntegerField(
        'пограничный возраст',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'ступень'
        verbose_name_plural = 'ступени'

    def __str__(self):
        return TIER_AS_WORD[int(str(self.number))] + ' ступень'
