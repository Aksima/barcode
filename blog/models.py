from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    title = models.CharField('заголовок', max_length=222)
    text = models.TextField('содержимое')
    created_date = models.DateTimeField('дата создания', default=timezone.now)
    published_date = models.DateTimeField('дата публикации', blank=True, null=True)

    def get_is_cut(self):
        return getattr(self.text, 'count')('\n') != 0

    is_cut = property(
        fget=get_is_cut,
        doc='Сокращенный текст.'
    )

    def get_cut(self):
        return getattr(self.text, 'splitlines')()[0]

    cut = property(
        fget=get_cut,
        doc='Сокращенный текст.'
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
