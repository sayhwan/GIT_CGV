# Generated by Django 4.2.3 on 2023-11-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_director_options_remove_director_old_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='born',
        ),
        migrations.AddField(
            model_name='director',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
