# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-14 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_question_question_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.IntegerField(default=0),
        ),
    ]