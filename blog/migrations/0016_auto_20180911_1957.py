# Generated by Django 2.0.2 on 2018-09-11 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180911_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 466031)),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('S', 'Secret'), ('O', 'Own'), ('P', 'Public')], default='D', max_length=3),
        ),
    ]