# Generated by Django 2.0.2 on 2018-02-28 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0011_auto_20180227_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 28, 8, 39, 31, 70556)),
        ),
        migrations.AlterField(
            model_name='locale',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 28, 8, 39, 31, 71434)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 28, 8, 39, 31, 70992)),
        ),
    ]
