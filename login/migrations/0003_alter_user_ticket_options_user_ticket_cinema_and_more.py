# Generated by Django 4.2.1 on 2023-11-27 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_ticket_user_user_ticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_ticket',
            options={'verbose_name': '유저 티켓'},
        ),
        migrations.AddField(
            model_name='user_ticket',
            name='cinema',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_ticket',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_ticket',
            name='movie',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_ticket',
            name='theater',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='user_ticket',
            table='user_ticket',
        ),
    ]
