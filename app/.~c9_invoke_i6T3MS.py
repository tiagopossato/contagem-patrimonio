from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.timezone import now

# @python_2_unicode_compatible
class Setor(models.Model):
    nome = models.CharField('Setor', max_length=255, unique)
    
    def __str__(self):
        return self.nome 

# @python_2_unicode_compatible
class DependenciaSetor(models.Model):
    nome = models.CharField('Dependencia de setor', max_length=255)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome 
        
# @python_2_unicode_compatible
class Item(models.Model):
    nome = models.CharField('Nome', max_length=255)
    patrimonio = models.IntegerField('Patrimonio antigo', null=True, blank=True)
    sipac = models.IntegerField('Patrimonio novo', null=True, blank=True)
    dependencia = models.ForeignKey(DependenciaSetor, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome 

# @python_2_unicode_compatible
class Aferidor(models.Model):
    nome = models.CharField('Nome', max_length=255)
    
    def __str__(self):
        return self.nome 

# @python_2_unicode_compatible
class Inventario(models.Model):
    ESTADO = (
        (-1, 'Nao encontrado'),
        (1, 'Bom'),
        (2, 'Ocioso'),
        (3, 'Danificado'),
        (4, 'Sem condicoes de uso'),
    )
    createdAt = models.DateTimeField('Criado em', default=now)
    updatedAt = models.DateTimeField('Alterado em', auto_now=True)
    estado = models.IntegerField(
        'Estado do bem', default=-1, choices=ESTADO)
    obs = models.CharField(
        'Observacao', null=True, blank=True, max_length=255)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    setor = models.ForeignKey(DependenciaSetor, on_delete=models.PROTECT)
    
    aferidores = models.ManyToManyField(Aferidor)

# class AferidorInventario(Aferidor):
#     inventario = models.ForeignKey(Inventario, on_delete=models.PROTECT)
#     class Meta:
#         verbose_name = 'Aferidor'
#         verbose_name_plural = 'Aferidores'
