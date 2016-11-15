# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=25)),
                ('race', models.CharField(max_length=20)),
                ('heroclass', models.CharField(max_length=25)),
                ('alignment', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('background', models.CharField(max_length=200)),
                ('faction', models.CharField(max_length=200)),
            ],
        ),
    ]
