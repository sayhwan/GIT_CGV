from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0018_alter_ticketing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketing',
            name='user',
            field=models.JSONField(default=list),
        ),
    ]
