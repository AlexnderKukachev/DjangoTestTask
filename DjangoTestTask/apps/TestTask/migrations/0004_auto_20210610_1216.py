# Generated by Django 3.2.4 on 2021-06-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTask', '0003_auto_20210610_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='pic',
            field=models.ImageField(default='None', upload_to=''),
        ),
        migrations.AlterField(
            model_name='pic',
            name='url',
            field=models.URLField(default='None', max_length=30, verbose_name='URL ссылка на изображение'),
        ),
    ]
