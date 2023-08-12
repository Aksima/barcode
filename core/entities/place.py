from django.db import models


class Place(models.Model):
    name = models.CharField(
        'название',
        max_length=22,
        unique=True,
        default=''
    )

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.name
