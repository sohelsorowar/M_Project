# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-07-11 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0002_create_meeting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_meeting',
            name='id',
        ),
        migrations.AlterField(
            model_name='create_meeting',
            name='meeting_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]