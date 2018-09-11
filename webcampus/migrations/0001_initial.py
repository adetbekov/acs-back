# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 19:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webcampus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 47, 34, 974499))),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('degree', models.CharField(choices=[('3', 'Advanced'), ('2', 'Intermediate'), ('0', 'Beginner'), ('1', 'Elementary')], default='0', max_length=3)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=webcampus.models.upload_location)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('H', 'Hidden'), ('A', 'Archive'), ('V', 'Visible')], default='H', max_length=3)),
                ('price', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 47, 34, 971386))),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='managing.Category')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='managing.Locale')),
                ('students', models.ManyToManyField(blank=True, related_name='course_students', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='HtmlBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 47, 34, 976790))),
            ],
            options={
                'verbose_name': 'Html блок',
                'verbose_name_plural': 'Html блоки',
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 47, 34, 975056))),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcampus.Chapter')),
                ('done', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Шаг',
                'verbose_name_plural': 'Шаги',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('icon_name', models.CharField(default='', max_length=30)),
                ('color', models.CharField(default='#34495e', max_length=30)),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 47, 34, 970547))),
            ],
            options={
                'verbose_name': 'Субъект',
                'verbose_name_plural': 'Субъекты',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 47, 34, 976260))),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcampus.Step')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=255)),
                ('visible', models.BooleanField(default=True)),
                ('duration', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 1, 18, 1, 47, 34, 977424))),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcampus.Step')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.AddField(
            model_name='htmlblock',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcampus.Step'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(blank=True, related_name='course_subjects', to='webcampus.Subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='course_tags', to='managing.Tag'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webcampus.Course'),
        ),
    ]
