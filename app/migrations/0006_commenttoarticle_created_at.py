# Generated by Django 3.1.5 on 2021-01-23 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210121_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenttoarticle',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 13, 29, 25, 755995)),
        ),
    ]