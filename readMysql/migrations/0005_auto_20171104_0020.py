# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('readMysql', '0004_readmysql__json'),
    ]

    operations = [
        migrations.AddField(
            model_name='readmysql',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='\u63d2\u5165\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='readmysql',
            name='upadte_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name=''),
        ),
    ]
