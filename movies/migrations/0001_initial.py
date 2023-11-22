# Generated by Django 4.2.3 on 2023-11-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('age', models.IntegerField(default=0)),
                ('summary', models.TextField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '영화',
                'verbose_name_plural': '영화',
                'db_table': 'movie',
            },
        ),
    ]
