# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 19:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0003_auto_20180118_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 50, 10, 155281)),
        ),
        migrations.AlterField(
            model_name='locale',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 50, 10, 156216)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 50, 10, 155742)),
        ),
    ]