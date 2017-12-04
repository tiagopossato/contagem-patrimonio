# -*- coding: cp1252 -*-
import csv, sys

# Configuracoes para usar os models do django
import os
import sys
import django
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "")))
os.environ["DJANGO_SETTINGS_MODULE"] = "inventario.settings"
django.setup()

from app.models import Setor, DependenciaSetor, Item

filename = 'itens.csv'

with open(filename, 'rb') as ficheiro:
    reader = csv.reader(ficheiro, delimiter='|')
    
    for linha in reader:
        try:
            # setor = Setor(nome = unicode(linha[3], 'utf-8')) #linha[3].decode('utf8').encode('ascii', errors='ignore')
            # setor.save()
            setor = Setor.objects.get(nome=linha[3])
            dependencia = DependenciaSetor.objects.get(nome=unicode(linha[4], 'utf-8'),setor=setor)
            nome=unicode(linha[0], 'utf-8')
            patrimonio=None
            try:
                patrimonio=int(unicode(linha[1], 'utf-8'))
            except Exception as e:
                print('Patrimonio: linha %d: %s' % (reader.line_num, e))
            sipac=None
            try:
                sipac=int(unicode(linha[2], 'utf-8'))
            except Exception as e:
                print('Sipac: linha %d: %s' % (reader.line_num, e))
            it = Item(nome=nome, patrimonio=patrimonio, sipac=sipac, dependencia=dependencia)
            it.save()
        except Exception as e:
            print('ficheiro %s, linha %d: %s' % (filename, reader.line_num, e))