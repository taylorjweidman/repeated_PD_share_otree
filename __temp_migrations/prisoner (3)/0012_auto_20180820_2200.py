# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-21 02:00
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner', '0011_auto_20180820_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='round',
        ),
        migrations.AddField(
            model_name='player',
            name='round',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
    ]
