# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-14 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_correcta',
            field=models.BooleanField(default=False),
        ),
    ]