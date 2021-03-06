# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nccg', '0002_auto_20171022_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='NCCGAdvisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=300)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NCCGClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NCCGPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=300)),
                ('bio', models.TextField()),
                ('linkedin', models.CharField(max_length=300)),
            ],
        ),
    ]
