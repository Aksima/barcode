from django.db import models


class Ability(models.Model):
    name = models.CharField(
        'название',
        max_length=22,
        unique=True,
        default=''
    )

    class Meta:
        verbose_name = 'способность'
        verbose_name_plural = 'способности'

    def __str__(self):
        return self.name