from django.db import models


class Setting(models.Model):
    title = models.CharField(verbose_name='عنوان سایت', max_length=120)
    description = models.TextField(verbose_name='توضیحات')
    email = models.EmailField(verbose_name='ایمیل پشتیبانی')
    phone = models.CharField(verbose_name='تلفن پشتیبانی', max_length=11)
    addr = models.TextField(verbose_name='آدرس فروشگاه')
    logo = models.ImageField(verbose_name='لوگوی سایت', upload_to='logo', null=True)

    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.title
