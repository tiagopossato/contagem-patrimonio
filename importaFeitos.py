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

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from app.models import *

filename = 'todos.csv'
file = open("feitos-erro.csv","w")
with open(filename, 'rb') as ficheiro:
    reader = csv.reader(ficheiro, delimiter='|')
    
    for linha in reader:
        try:
            if(len(linha)<5):
                print(linha)
                print('ficheiro %s, linha %d, tem menos do que 5 posicoes\n' % (filename, reader.line_num))
                continue
            estado = linha[1]
            obs  = linha[2]
            setorTmp = linha[3]
            aferidores= linha[4]
            
            sipac=None
            try:
                sipac=int(linha[0])
            except Exception as e:
                print(linha)
                print('Sipac: linha %d: %s' % (reader.line_num, e))
                continue

            dependencia = None
            try:
                dependencia = DependenciaSetor.objects.get(nome=setorTmp)
                print(setorTmp)
                print(dependencia.nome)
            except Exception as e:
                if 'matching query does not exist' not in e.message:
                    print(linha)
                    print('DependenciaSetor: linha %d: %s' % (reader.line_num, e))

            try:
                it = Inventario(estado=estado, obs=obs, item_id=sipac, setorTmp=setorTmp, dependencia=dependencia, aferidores=aferidores)
                # it.save()
            except IntegrityError as e: 
                if 'UNIQUE constraint' in e.message:
                    id = Inventario.objects.get(item_id=sipac)
                    print(id)
                    # if(id.estado==1 and id.aferidores==""):
                    #     # print(id)
                    #     # id.estado = estado
                    #     # id.obs = obs
                    #     # id.setorTmp = setorTmp
                    #     id.aferidores = aferidores
                    #     # id.dependencia = dependencia
                    #     id.save()
                    # else:
                    #     print(id)
                    #     # print('Inventario: linha %d: %s' % (reader.line_num, e))
                    #     file.write(str(linha))
                    #     file.write("\n")
                        
        except Exception as e:
            print('ficheiro %s, linha %d: %s' % (filename, reader.line_num, e))
            file.write(str(linha))
            file.write("\n")
file.close()