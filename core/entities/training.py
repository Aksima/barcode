import datetime
from django.db import models
from django.forms import ModelForm
from .assignment import Assignment
from . import with_names_for_methods

GRADES = [
    ('A', 'отлично'),
    ('B', 'хорошо'),
    ('C', 'удовлетворительно'),
    ('D', 'неудовлетворительно'),
    ('F', 'плохо')
]
SCHEDULED = 'S'
ACCEPTED = 'A'
DECLINED = 'D'
COMPLETED = 'C'
STATUSES = [
    (SCHEDULED, 'Запланирована'),
    (ACCEPTED, 'Подтверждена'),
    (DECLINED, 'Отменена'),
    (COMPLETED, 'Завершена'),
]


class Training(models.Model):
    label = models.CharField(
        'заголовок',
        max_length=55,
        default='Новая'
    )
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='назначение'
    )
    dt = models.DateTimeField('дата и время начала тренировки')
    duration = models.DurationField(
        'продолжительность тренировки',
        default=datetime.timedelta(hours=1)
    )
    description = models.TextField(
        'описание',
        blank=True,
        default=''
    )
    coach_approval = models.CharField(
        'статус тренировки (тренер)',
        max_length=1,
        choices=STATUSES,
        blank=True,
        null=True
    )
    coach_notes = models.TextField(
        'замечания тренера',
        blank=True,
        default=''
    )
    coach_grade = models.CharField(
        'оценка тренера',
        max_length=1,
        choices=GRADES,
        blank=True,
        null=True
    )
    member_comment = models.TextField(
        'комментарий занимающегося',
        blank=True,
        default=''
    )
    member_approval = models.CharField(
        'статус тренировки (занимающийся)',
        max_length=1,
        choices=STATUSES,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'тренировка'
        verbose_name_plural = 'тренировки'

    @with_names_for_methods
    class MyMeta:
        name = 'training'
        verbose_name_genitive = 'тренировки'
        verbose_name_plural_genitive = 'тренировок'

    def __str__(self):
        return self.label


class AddTrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ['label', 'assignment', 'dt', 'duration', 'description']


class EditTrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = [
            'label',
            'description',
            'coach_approval',
            'coach_notes',
            'coach_grade',
            'member_comment',
            'member_approval'
        ]
