# Generated by Django 4.2.7 on 2023-11-26 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0011_ticketing_theater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketing',
            name='theater',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='ticketing.theater'),
        ),
    ]
