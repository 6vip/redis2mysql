# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-02 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readMysql', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readmysql',
            options={'verbose_name': 'chili'},
        ),
        migrations.AlterField(
            model_name='readmysql',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
