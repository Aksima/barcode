from django.conf import settings
from django.db import models
from django.forms import ModelForm
from . import GENDERS, SUFFIX_FOR_GENDER, with_names_for_methods


class Coach(models.Model):
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='связанный аккаунт',
        primary_key=True
    )
    gender = models.CharField(
        'пол',
        max_length=1,
        choices=GENDERS,
        null=True
    )
    image_width = models.IntegerField(
        'ширина картинки',
        blank=True
    )
    image_height = models.IntegerField(
        'высота картики',
        blank=True
    )
    photo = models.ImageField(
        'фотография',
        upload_to='people/',
        width_field='image_width',
        height_field='image_height'
    )
    about = models.TextField(
        'о себе',
        blank=True,
        default=''
    )

    class Meta:
        verbose_name = 'тренер'
        verbose_name_plural = 'тренеры'

    @with_names_for_methods
    class MyMeta:
        name = 'coach'
        verbose_name_genitive = 'тренера'
        verbose_name_plural_genitive = 'тренеров'

    def __str__(self):
        return (
            getattr(self.account, 'get_full_name')()
            or ('Без''ымя''нн' + SUFFIX_FOR_GENDER[self.gender])
        )


class AddCoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['account', 'photo', 'about']


class EditCoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['photo', 'about']
