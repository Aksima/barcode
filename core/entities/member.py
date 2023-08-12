import datetime
from django.conf import settings
from django.db import models
from django.forms import ModelForm
from . import GENDERS, SUFFIX_FOR_GENDER, with_names_for_methods


class Member(models.Model):
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='связанный аккаунт',
        primary_key=True
    )
    name_genitive = models.CharField(
        'фамилия и имя в родительном падеже',
        max_length=250,
        default=''
    )
    birth_date = models.DateField('дата рождения')

    def get_age(self):
        current_date = datetime.datetime.today()
        current_year = current_date.year
        current_month = current_date.month
        current_day = current_date.day
        birth_year = getattr(self.birth_date, 'year')
        birth_month = getattr(self.birth_date, 'month')
        birth_day = getattr(self.birth_date, 'day')
        age = current_year - birth_year
        if (
                (current_month, current_day)
                < (birth_month, birth_day)
        ):
            age -= 1
        return age

    age = property(
        fget=get_age,
        doc='Возраст (количество полных лет).'
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
        verbose_name = 'занимающийся'
        verbose_name_plural = 'занимающиеся'

    @with_names_for_methods
    class MyMeta:
        name = 'member'
        verbose_name_genitive = 'занимающегося'
        verbose_name_plural_genitive = 'занимающихся'

    def __str__(self):
        return (
            getattr(self.account, 'get_full_name')()
            or ('Без''ымя''нн' + SUFFIX_FOR_GENDER[self.gender])
        )


class AddMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = [
            'account',
            'birth_date',
            'gender',
            'photo',
            'about'
        ]


class EditMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['photo', 'about']
