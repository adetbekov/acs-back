# Generated by Django 2.0.2 on 2018-02-26 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0010_auto_20180227_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 28, 995033)),
        ),
        migrations.AlterField(
            model_name='locale',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 28, 995972)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 28, 995514)),
        ),
    ]