# Generated by Django 2.0.2 on 2018-09-11 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcampus', '0015_auto_20180911_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 472717)),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 469507)),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('3', 'Advanced'), ('2', 'Intermediate'), ('1', 'Elementary'), ('0', 'Beginner')], default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('H', 'Hidden'), ('A', 'Archive'), ('V', 'Visible')], default='H', max_length=3),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 474985)),
        ),
        migrations.AlterField(
            model_name='step',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 473306)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 468260)),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 474489)),
        ),
        migrations.AlterField(
            model_name='trajectory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 468727)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 475612)),
        ),
    ]