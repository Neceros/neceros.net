# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160529_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='published',
        ),
    ]
