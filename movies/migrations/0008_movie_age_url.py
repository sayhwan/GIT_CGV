# Generated by Django 4.2.3 on 2023-11-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_remove_director_born_director_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='age_url',
            field=models.CharField(default='/', max_length=2000),
        ),
    ]
