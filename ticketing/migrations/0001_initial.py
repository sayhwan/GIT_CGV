# Generated by Django 4.2.7 on 2023-11-22 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0002_movie_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbering', models.IntegerField(default=0)),
                ('seat', models.CharField(default='(5,5)', max_length=10)),
            ],
            options={
                'verbose_name': '극장',
                'verbose_name_plural': '극장',
                'db_table': 'Cinemas',
            },
        ),
        migrations.CreateModel(
            name='Ticketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_all', models.JSONField(default=list)),
                ('time', models.DateTimeField(verbose_name='영화 시간')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.cinemas')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'verbose_name': '예매',
                'verbose_name_plural': '예매',
                'db_table': 'tiketing',
            },
        ),
    ]