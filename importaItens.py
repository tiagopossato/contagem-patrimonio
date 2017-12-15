import csv

# Configuracoes para usar os models do django
import os
import sys
import django
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "")))
os.environ["DJANGO_SETTINGS_MODULE"] = "inventario.settings"
django.setup()
reload(sys)
sys.setdefaultencoding("utf-8")

from app.models import Setor, DependenciaSetor, Item

filename = 'ultimo.csv'

# file = open("restantes.csv","w")
with open(filename, 'rb') as ficheiro:
    reader = csv.reader(ficheiro, delimiter='|')
    
    for linha in reader:
        try:
            try:
                dependencia, created = DependenciaSetor.objects.get_or_create(nome=linha[4])
            except Exception as e:
                print(linha)
                print(e)
                continue
            nome=linha[0]
            patrimonio=None
            try:
                patrimonio=int(linha[1])
            except Exception as e:
                pass
                # print('Patrimonio: linha %d: %s' % (reader.line_num, e))
            sipac=None
            # try:
            sipac=int(linha[2])
            # except Exception as e:
            #     print('Sipac: linha %d: %s' % (reader.line_num, e))
            it = Item(nome=nome, patrimonio=patrimonio, sipac=sipac, dependencia=dependencia)
            it.save()
        except Exception as e:
            # file.write(str(linha))
            # file.write('\n')
            print('ficheiro %s, linha %d: %s' % (filename, reader.line_num, e))
    
# file.close()