# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 19:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcampus', '0002_auto_20180118_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 48, 19, 865260)),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 48, 19, 862109)),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('3', 'Advanced'), ('2', 'Intermediate'), ('0', 'Beginner'), ('1', 'Elementary')], default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('V', 'Visible'), ('H', 'Hidden'), ('A', 'Archive')], default='H', max_length=3),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 48, 19, 867557)),
        ),
        migrations.AlterField(
            model_name='step',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 48, 19, 865821)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 48, 19, 861254)),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 48, 19, 867033)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 48, 19, 868188)),
        ),
    ]
