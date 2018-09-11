# Generated by Django 2.0.2 on 2018-09-11 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcampus', '0016_auto_20180911_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 313108)),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 309789)),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('3', 'Advanced'), ('1', 'Elementary'), ('0', 'Beginner'), ('2', 'Intermediate')], default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('A', 'Archive'), ('V', 'Visible'), ('H', 'Hidden')], default='H', max_length=3),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 316289)),
        ),
        migrations.AlterField(
            model_name='step',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 313840)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 308479)),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 315308)),
        ),
        migrations.AlterField(
            model_name='trajectory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 308987)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 20, 0, 45, 317287)),
        ),
    ]