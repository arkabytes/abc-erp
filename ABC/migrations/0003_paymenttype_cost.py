# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABC', '0002_paymenttype_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttype',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]
