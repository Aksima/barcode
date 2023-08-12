from django.db import models
from . import GENDERS
from .tier import Tier
from .challenge import Challenge


class Standard(models.Model):
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    gender = models.CharField(
        'пол',
        max_length=1,
        choices=GENDERS,
        null=True
    )
    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE,
        verbose_name='испытание'
    )
    bronze = models.IntegerField(
        'требуемый показатель (бронза)'
    )
    silver = models.IntegerField(
        'требуемый показатель (серебро)'
    )
    gold = models.IntegerField(
        'требуемый показатель (золото)'
    )

    models.UniqueConstraint(
        fields=(tier, gender, challenge),
        name='%(app_label)s_%(class)s'
    )

    class Meta:
        verbose_name = 'норматив'
        verbose_name_plural = 'нормативы'

    def __str__(self):
        return f'{self.tier} ()'
