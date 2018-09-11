# Generated by Django 2.0.2 on 2018-02-26 18:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webcampus', '0010_auto_20180227_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 29, 5043)),
        ),
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='managing.Category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 29, 1442)),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('3', 'Advanced'), ('2', 'Intermediate'), ('1', 'Elementary'), ('0', 'Beginner')], default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='managing.Locale'),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('V', 'Visible'), ('H', 'Hidden'), ('A', 'Archive')], default='H', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='trajectory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='webcampus.Trajectory'),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 29, 7691)),
        ),
        migrations.AlterField(
            model_name='step',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 29, 5669)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 28, 999961)),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 29, 7113)),
        ),
        migrations.AlterField(
            model_name='trajectory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 29, 557)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 0, 47, 29, 8409)),
        ),
    ]
