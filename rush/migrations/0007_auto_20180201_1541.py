# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-01 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0006_rushapplication_application_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='rushapplication',
            name='picture',
            field=models.ImageField(default=None, upload_to='rush_pics/', null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rushapplication',
            name='resume',
            field=models.FileField(default=None, upload_to='rush_resumes/', null=True),
            preserve_default=False,
        ),
    ]