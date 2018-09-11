# Generated by Django 2.0.2 on 2018-09-11 13:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('managing', '0016_auto_20180911_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rightnow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=30)),
                ('mood', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(choices=[('P', 'Public'), ('O', 'Own'), ('A', 'Archive')], default='P', max_length=3)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 9, 11, 19, 57, 45, 477755))),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='managing.Locale')),
            ],
        ),
    ]