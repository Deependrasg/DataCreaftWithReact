# Generated by Django 2.0.2 on 2018-02-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataSearch', '0003_auto_20180223_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
