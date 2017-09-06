# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170903_0940'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='object_id',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.SlugField(unique=True),
        ),
    ]
