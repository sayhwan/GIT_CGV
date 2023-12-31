# Generated by Django 4.2.7 on 2023-11-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketing',
            name='time',
        ),
        migrations.AddField(
            model_name='ticketing',
            name='date',
            field=models.TextField(default='2023', max_length=20, verbose_name='날짜'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticketing',
            name='finish_time',
            field=models.TextField(default='12:00', max_length=20, verbose_name='끝나는 시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticketing',
            name='start_time',
            field=models.TextField(default='12:00', max_length=20, verbose_name='시작 시간'),
            preserve_default=False,
        ),
    ]
