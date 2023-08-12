from django.db import models
from .ability import Ability
from .unit import Unit


class Challenge(models.Model):
    name = models.CharField(
        'описание',
        max_length=55,
        unique=True,
        default=''
    )
    ability = models.ForeignKey(
        Ability,
        on_delete=models.CASCADE,
        verbose_name='проверяемое качество'
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        verbose_name='единица измерения'
    )

    class Meta:
        verbose_name = 'испытание'
        verbose_name_plural = 'испытания'

    def __str__(self):
        return self.name
