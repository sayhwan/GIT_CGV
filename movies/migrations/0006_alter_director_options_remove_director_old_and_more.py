# Generated by Django 4.2.3 on 2023-11-25 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_director_movie_director'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='director',
            options={'verbose_name': '감독', 'verbose_name_plural': '감독'},
        ),
        migrations.RemoveField(
            model_name='director',
            name='old',
        ),
        migrations.AddField(
            model_name='director',
            name='born',
            field=models.DateField(default=datetime.date.today),
        ),
    ]