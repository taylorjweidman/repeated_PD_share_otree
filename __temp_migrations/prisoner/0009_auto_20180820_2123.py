# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-21 01:23
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner', '0008_auto_20180820_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='cycle',
        ),
        migrations.AddField(
            model_name='subsession',
            name='cycle',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
    ]
