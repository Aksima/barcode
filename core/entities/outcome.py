from django.db import models
from .member import Member
from .challenge import Challenge


class Outcome(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        verbose_name='занимающийся'
    )
    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE,
        verbose_name='испытание'
    )
    date = models.DateField('дата испытания')
    result = models.IntegerField('результат')

    class Meta:
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'

    def __str__(self):
        return f'{self.member} - {self.challenge.name}'
