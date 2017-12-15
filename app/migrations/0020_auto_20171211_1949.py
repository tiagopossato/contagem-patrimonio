# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20171211_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependenciasetor',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dependencia de setor'),
        ),
        migrations.AlterField(
            model_name='dependenciasetor',
            name='nomeNovo',
            field=models.CharField(default='', max_length=255, verbose_name='Dependencia do Setor / NOME ATUAL'),
            preserve_default=False,
        ),
    ]