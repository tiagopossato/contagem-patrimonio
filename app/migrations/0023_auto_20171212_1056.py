# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-12 10:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20171212_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='setor',
            new_name='dependencia',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='createdAt',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='updatedAt',
        ),
    ]
