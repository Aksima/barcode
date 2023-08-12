from django.db import models


class Unit(models.Model):
    name = models.CharField(
        'название',
        max_length=33,
        unique=True,
        default='-'
    )

    class Meta:
        verbose_name = 'единица измерения'
        verbose_name_plural = 'единицы измерения'

    def __str__(self):
        return self.name
