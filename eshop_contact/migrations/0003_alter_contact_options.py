# Generated by Django 4.0.3 on 2022-03-27 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_contact', '0002_alter_contact_first_name_alter_contact_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
    ]