# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateTimeField()),
                ('read_time', models.IntegerField(default=0)),
                ('language', models.CharField(choices=[('English', 'English'), ('Vietnamese', 'Vietnamese'), ('Japanese', 'Japanese')], default='English', max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]