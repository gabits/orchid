# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 22:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_media_video_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractportfoliowork',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 20, 22, 50, 41, 812608, tzinfo=utc), null=True),
        ),
    ]
