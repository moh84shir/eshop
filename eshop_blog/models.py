from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    subject = models.CharField(max_length=400, verbose_name='موضوع')
    description = models.CharField(max_length=400, verbose_name='توضیجات')
    text = models.TextField(verbose_name='متن')
    author: User = models.OneToOneField(
        User, models.CASCADE, verbose_name='نویسنده')
    created = models.DateTimeField(
        verbose_name='زمان ایجاد', auto_now_add=True)
    photo = models.ImageField(upload_to='blog/', null=True, verbose_name='عکس')

    def get_author_fullname(self):
        return self.author.get_full_name()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.title
