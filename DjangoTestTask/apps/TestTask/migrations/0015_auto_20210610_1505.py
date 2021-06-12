# Generated by Django 3.2.4 on 2021-06-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTask', '0014_pic_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='pic_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Название изображения'),
        ),
        migrations.AlterField(
            model_name='pic',
            name='url',
            field=models.URLField(default='', max_length=300, null=True, verbose_name='URL ссылка на изображение'),
        ),
    ]
