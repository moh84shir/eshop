from django.db import models


class Slider(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=120)
    description = models.CharField(verbose_name='توضیحات', max_length=400)
    image = models.ImageField(verbose_name='عکس', upload_to='slider/%M')
    link = models.CharField(verbose_name='لینک', max_length=120)

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
