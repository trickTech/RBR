# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20161206_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
