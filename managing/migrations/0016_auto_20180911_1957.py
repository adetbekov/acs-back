# Generated by Django 2.0.2 on 2018-09-11 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0015_auto_20180911_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 464294)),
        ),
        migrations.AlterField(
            model_name='locale',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 465253)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 464777)),
        ),
    ]