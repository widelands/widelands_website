# Generated by Django 2.2.28 on 2022-12-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wlscheduling", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="availabilities",
            name="avail_time",
            field=models.DateTimeField(
                help_text="this user is available for this whole hour"
            ),
        ),
    ]
