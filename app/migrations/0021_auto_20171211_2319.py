# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20171211_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Setor Responsavel'),
        ),
    ]
