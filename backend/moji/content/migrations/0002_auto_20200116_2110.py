# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-16 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='numCom',
            new_name='numComs',
        ),
    ]
