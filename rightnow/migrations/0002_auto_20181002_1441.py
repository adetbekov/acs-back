# Generated by Django 2.0.2 on 2018-10-02 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rightnow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rightnow',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 14, 41, 5, 890301)),
        ),
        migrations.AlterField(
            model_name='rightnow',
            name='status',
            field=models.CharField(choices=[('A', 'Archive'), ('P', 'Public'), ('O', 'Own')], default='P', max_length=3),
        ),
    ]
