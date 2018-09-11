# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-26 18:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180226_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 15, 31, 89787)),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('S', 'Secret'), ('D', 'Draft'), ('O', 'Own'), ('P', 'Public')], default='D', max_length=3),
        ),
    ]