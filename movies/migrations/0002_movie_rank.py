# Generated by Django 4.2.3 on 2023-11-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
