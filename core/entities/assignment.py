from django.db import models
from .coach import Coach
from .member import Member
from .place import Place


class Assignment(models.Model):
    coach = models.ForeignKey(
        Coach,
        on_delete=models.CASCADE,
        verbose_name='тренер'
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        verbose_name='занимающийся'
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='место'
    )

    models.UniqueConstraint(
        fields=(coach, member, place),
        name='%(app_label)s_%(class)s'
    )

    class Meta:
        verbose_name = 'назначение'
        verbose_name_plural = 'назначения'

    def __str__(self):
        name_genitive = getattr(self.member, 'name_genitive')
        return f'{self.place} {name_genitive} ({self.coach})'
