# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-20 22:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABC', '0021_auto_20180119_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 20, 22, 31, 56, 679163)),
        ),
        migrations.AddField(
            model_name='event',
            name='notice_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 20, 22, 31, 56, 679289)),
        ),
        migrations.AddField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_days',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='task',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='task',
            name='notice_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 20, 22, 31, 56, 683205)),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
