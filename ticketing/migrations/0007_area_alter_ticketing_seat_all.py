# Generated by Django 4.2.3 on 2023-11-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0006_alter_ticketing_movie_times_alter_ticketing_seat_all'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='ticketing',
            name='seat_all',
            field=models.JSONField(default=list),
        ),
    ]