# Generated by Django 4.2.7 on 2023-11-26 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0008_area_theaters_alter_area_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Theather',
            new_name='Theater',
        ),
    ]
