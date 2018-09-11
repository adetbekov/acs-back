# Generated by Django 2.0.2 on 2018-09-11 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcampus', '0014_auto_20180603_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 927402)),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 922573)),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('0', 'Beginner'), ('3', 'Advanced'), ('1', 'Elementary'), ('2', 'Intermediate')], default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('A', 'Archive'), ('V', 'Visible'), ('H', 'Hidden')], default='H', max_length=3),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 930903)),
        ),
        migrations.AlterField(
            model_name='step',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 928302)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 920647)),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 930145)),
        ),
        migrations.AlterField(
            model_name='trajectory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 921341)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 46, 47, 931839)),
        ),
    ]