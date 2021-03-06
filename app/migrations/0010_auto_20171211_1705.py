# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20171205_2120'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aferidor',
        ),
        migrations.AddField(
            model_name='inventario',
            name='setorTmp',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Setor temporario'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.DependenciaSetor'),
        ),
    ]
