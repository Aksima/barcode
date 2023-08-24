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

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def get_title_with_author(self):
        title = str(self.title)
        first_name = getattr(self.author, 'first_name')
        last_name = getattr(self.author, 'last_name')
        if first_name:
            if last_name:
                return f'{title} (автор: {last_name} {first_name})'
            return f'{title} (автор: {first_name})'
        return title

    title_with_author = property(
        fget=get_title_with_author,
        doc='Заголовок с указанием автора.'
    )

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
