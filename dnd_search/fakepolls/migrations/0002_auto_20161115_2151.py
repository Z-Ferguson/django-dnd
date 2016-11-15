# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 21:51
from __future__ import unicode_literals

from django.db import migrations
import csv

def combine_names(apps, schema_editor):
    with open('initial_data.csv', 'r') as f:
        fieldnames = ['hero_name', 'race', 'heroclass', 'alignment', 'age', 'height', 'level', 'background', 'faction']
        r = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        Hero = apps.get_model("fakepolls", "Hero")
        for line in r:
            print(line)
            b = Hero(**line)
            b.save()


class Migration(migrations.Migration):

    dependencies = [
        ('fakepolls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
