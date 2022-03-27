from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    subject = models.CharField(max_length=120, verbose_name='موضوع')
    first_name = models.CharField(max_length=120, verbose_name='نام')
    last_name = models.CharField(max_length=120, verbose_name='فامیلی')
    text = models.TextField(verbose_name='متن پیام')

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.title