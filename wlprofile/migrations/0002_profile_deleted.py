# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-13 21:23


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wlprofile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]
