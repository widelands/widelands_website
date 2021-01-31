# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-31 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlhelp', '0002_auto_20190410_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='size',
            field=models.CharField(choices=[('S', 'small'), ('M', 'medium'), ('B', 'big'), ('I', 'mine'), ('P', 'port'), ('H', 'headquarters')], max_length=1),
        ),
        migrations.AlterField(
            model_name='building',
            name='type',
            field=models.CharField(choices=[('P', 'productionsite'), ('W', 'warehouse'), ('M', 'militarysite'), ('T', 'trainingsite'), ('m', 'market')], max_length=1),
        ),
    ]
