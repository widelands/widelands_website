# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-31 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlggz', '0002_auto_20160805_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ggzauth',
            name='password',
            field=models.CharField(blank=True, default='', max_length=80, verbose_name='ggz password'),
        ),
    ]
