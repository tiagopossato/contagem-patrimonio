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


from django.utils.encoding import python_2_unicode_compatible

from app.models import Setor, DependenciaSetor, Item

def main():
    file = open("restantes.csv","w")

    itens = Item.objects.all()

    for item in itens:
        #try:
            # linha = [item.nome if item.nome else '',
            #             str(item.patrimonio) if item.patrimonio else '',
            #             str(item.sipac) if item.sipac else '',
            #             item.dependencia.setor.nome if item.dependencia.setor else '',
            #             item.dependencia.nome if item.dependencia else '',
            #             str(item.estado) if item.estado else '',
            #             item.obs if item.obs else '',
            #             item.dependenciaEncontrada.nome if item.dependenciaEncontrada else '',
            #             item.aferidores if item.aferidores else '']
        print item 
            # file.write(item)
            # file.write('\n')
            # break
        #except Exception as e:
        #    print e
        #    break
    file.close

main()