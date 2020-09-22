# Generated by Django 3.1.1 on 2020-09-22 12:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20200922_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(choices=[(3, 'Гость'), (1, 'Администратор'), (2, 'Модератор')]),
        ),
    ]