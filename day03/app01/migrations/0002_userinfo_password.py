# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-29 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default='123', max_length=32),
        ),
    ]
