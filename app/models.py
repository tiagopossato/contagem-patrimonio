from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils.timezone import now


@python_2_unicode_compatible
class Bloco(models.Model):
    nome = models.CharField('Bloco', max_length=255, unique=True)
    
    def __str__(self):
        return self.nome 
    class Meta:
        verbose_name = 'Bloco'
        verbose_name_plural = 'Blocos'
        ordering = ['nome']

@python_2_unicode_compatible
class Setor(models.Model):
    nome = models.CharField('Setor / NOME ANTIGO', max_length=255, null=True, blank=True)
    nomeNovo = models.CharField('Setor / NOME ATUAL', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.nomeNovo

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

@python_2_unicode_compatible
class DependenciaSetor(models.Model):
    nome = models.CharField('Dependencia de setor / NOME ANTIGO', max_length=255, null=True, blank=True)
    nomeNovo = models.CharField('Dependencia do Setor / NOME ATUAL', max_length=255)
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT, null=True, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.nomeNovo + "("+self.nome+")" + ", bloco " +str(self.bloco) + ", " +str(self.setor)
    
    class Meta:
        # define combinacao unica
        unique_together = ('nomeNovo', 'setor')
        verbose_name = 'Dependencia de setor'
        verbose_name_plural = 'Dependencias'
        ordering = ['bloco__nome']
        
@python_2_unicode_compatible
class Item(models.Model):
    nome = models.CharField('Nome', max_length=255)
    patrimonio = models.IntegerField('Patrimonio antigo', null=True, blank=True)
    sipac = models.IntegerField('Patrimonio novo', unique=True)
    dependencia = models.ForeignKey(DependenciaSetor, related_name='dependenciaOriginal', on_delete=models.PROTECT)
    
    ESTADO = (
        (-1, 'Nao encontrado'),
        (1, 'Bom'),
        (2, 'Ocioso'),
        (3, 'Danificado'),
        (4, 'Sem condicoes de uso'),
    )
    estado = models.IntegerField(
        'Estado do bem', default=-1, choices=ESTADO)
    obs = models.CharField(
        'Observacao', null=True, blank=True, max_length=255)
    dependenciaEncontrada = models.ForeignKey(DependenciaSetor, related_name='dependenciaEncontrada', on_delete=models.PROTECT, null=True, blank=True)
    setorTmp = models.CharField('Setor temporario', max_length=255, null=True, blank=True)
    aferidores = models.CharField('Aferidor', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.nome + ', ' + str(self.estado)

# @python_2_unicode_compatible
# class Inventario(models.Model):
#     ESTADO = (
#         (-1, 'Nao encontrado'),
#         (1, 'Bom'),
#         (2, 'Ocioso'),
#         (3, 'Danificado'),
#         (4, 'Sem condicoes de uso'),
#     )
#     estado = models.IntegerField(
#         'Estado do bem', default=-1, choices=ESTADO)
#     obs = models.CharField(
#         'Observacao', null=True, blank=True, max_length=255)
#     item = models.OneToOneField(Item, to_field='sipac', on_delete=models.PROTECT)
#     dependencia = models.ForeignKey(DependenciaSetor, on_delete=models.PROTECT, null=True, blank=True)
#     setorTmp = models.CharField('Setor temporario', max_length=255, null=True, blank=True)
#     aferidores = models.CharField('Aferidor', max_length=255)

#     def __str__(self):
#         return self.item.nome + ', ' + str(self.estado)+ ', ' + str(self.dependencia) + ', ' + str(self.aferidores)