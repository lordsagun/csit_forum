# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-13 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0004_auto_20181213_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(help_text='Use the following format: 2066', max_length=4),
        ),
    ]
