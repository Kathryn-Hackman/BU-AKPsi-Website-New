# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brothers', '0005_merge_20171022_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eye2EyeMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=45)),
                ('bio', models.TextField()),
                ('brother', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='brothers.Brother')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]