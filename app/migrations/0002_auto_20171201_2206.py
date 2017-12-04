# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-01 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='nome',
            field=models.CharField(max_length=255, unique=True, verbose_name='Setor'),
        ),
        migrations.AlterUniqueTogether(
            name='dependenciasetor',
            unique_together=set([('nome', 'setor')]),
        ),
    ]
