# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-27 21:54
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner', '0018_auto_20180827_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='round',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
