# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 09:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20171212_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloco',
            options={'ordering': ['nome'], 'verbose_name': 'Bloco', 'verbose_name_plural': 'Blocos'},
        ),
        migrations.AlterModelOptions(
            name='dependenciasetor',
            options={'ordering': ['bloco__nome'], 'verbose_name': 'Dependencia de setor', 'verbose_name_plural': 'Dependencias'},
        ),
    ]
