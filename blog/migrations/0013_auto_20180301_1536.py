# Generated by Django 2.0.2 on 2018-03-01 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180228_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 1, 15, 36, 43, 917630)),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Public'), ('S', 'Secret'), ('O', 'Own')], default='D', max_length=3),
        ),
    ]
