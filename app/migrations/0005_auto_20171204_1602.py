# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-04 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171204_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Item', to_field='sipac'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sipac',
            field=models.IntegerField(unique=True, verbose_name='Patrimonio novo'),
        ),
    ]
