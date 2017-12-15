# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20171211_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependenciasetor',
            name='nomeNovo',
            field=models.CharField(default='', max_length=255, verbose_name='NOME ATUAL/Dependencia do Setor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setor',
            name='nome',
            field=models.CharField(max_length=255, unique=True, verbose_name='Setor Responsavel'),
        ),
    ]
