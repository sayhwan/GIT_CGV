# Generated by Django 4.2.7 on 2023-11-26 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0009_rename_theather_theater'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': '지역', 'verbose_name_plural': '지역'},
        ),
        migrations.AlterModelOptions(
            name='theater',
            options={'verbose_name': '영화관', 'verbose_name_plural': '영화관'},
        ),
        migrations.AlterModelTable(
            name='area',
            table='area',
        ),
        migrations.AlterModelTable(
            name='theater',
            table='theater',
        ),
    ]