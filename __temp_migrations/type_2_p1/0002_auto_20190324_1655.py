# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-24 20:55
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('type_2_p1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='other_decision',
        ),
        migrations.AddField(
            model_name='group',
            name='group_decision',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='group_decision',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
