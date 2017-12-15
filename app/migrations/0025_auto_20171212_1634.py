# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-12 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20171212_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='dependencia',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='aferidores',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Aferidor'),
        ),
        migrations.AddField(
            model_name='item',
            name='dependenciaEncontrada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dependenciaEncontrada', to='app.DependenciaSetor'),
        ),
        migrations.AddField(
            model_name='item',
            name='estado',
            field=models.IntegerField(choices=[(-1, 'Nao encontrado'), (1, 'Bom'), (2, 'Ocioso'), (3, 'Danificado'), (4, 'Sem condicoes de uso')], default=-1, verbose_name='Estado do bem'),
        ),
        migrations.AddField(
            model_name='item',
            name='obs',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Observacao'),
        ),
        migrations.AddField(
            model_name='item',
            name='setorTmp',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Setor temporario'),
        ),
        migrations.AlterField(
            model_name='item',
            name='dependencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dependenciaOriginal', to='app.DependenciaSetor'),
        ),
        migrations.DeleteModel(
            name='Inventario',
        ),
    ]
