# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20170905_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
    ]
