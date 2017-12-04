# -*- coding: cp1252 -*-
import csv, sys

# Configuracoes para usar os models do django
import os
import sys
import django
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "")))
os.environ["DJANGO_SETTINGS_MODULE"] = "inventario.settings"
django.setup()

from app.models import Item, Inventario

filename = 'todos.csv'

with open(filename, 'rb') as ficheiro:
    reader = csv.reader(ficheiro, delimiter='|')
    
    for linha in reader:
        try:
            if(len(linha)<11):
                # print(linha)
                # print('ficheiro %s, linha %d, tem menos do que 11 posicoes\n' % (filename, reader.line_num))
                continue
            estado = unicode(linha[7], 'utf-8')
            obs  = unicode(linha[8], 'utf-8')
            setor = unicode(linha[9], 'utf-8')
            aferidores= unicode(linha[10], 'utf-8')
            sipac=None
            try:
                sipac=int(unicode(linha[2], 'utf-8'))
            except Exception as e:
                # print(linha)
                # print('Sipac: linha %d: %s' % (reader.line_num, e))
                continue
                
            it = Inventario(estado=estado, obs=obs, item_id=sipac, setor=setor, aferidores=aferidores)
            it.save()
        except Exception as e:
            print('ficheiro %s, linha %d: %s' % (filename, reader.line_num, e))