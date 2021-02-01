# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-01 15:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import wlpoll.models


class Migration(migrations.Migration):

    dependencies = [
        ('wlpoll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='closed_date',
            field=models.DateTimeField(blank=True, default=wlpoll.models.closed_date_default, null=True, verbose_name='date closed'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='date_voted',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='voted at'),
        ),
    ]
