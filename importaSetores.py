"""
1- selecionar tudo na planilha 
2- desmesclar
3- copiar todo o conteudo util na mesma planilha
4- apagar as duas primeiras linhas de cabecalho
5- salvar o csv
6- subir csv no c9


"""
import csv
import urllib2
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
from app.models import *


saida = urllib2.urlopen("https://script.google.com/macros/s/AKfycbxLjGP751AJZzwhJTzxkAlsUFpcZBt2gWZwzxcnYxw6QC1ZAks/exec").read()

filename = 'setores.csv'
setor=None
bloco=None
# with open(filename, 'rb') as ficheiro:
#     reader = csv.reader(ficheiro, delimiter='|')
reader = saida.split('\n')
print(len(reader))
i = 0
for linha in reader:
    # print(linha)
    try:
        linha = linha.split('|')
        # print(linha)
        nomeBloco = linha[0]
        nomeSetor = linha[3]
        nomeDependenciaNovo = linha[2]
        nomeAnterior = linha[1]
            
        try:
            if(nomeBloco != ""):
                bloco=Bloco.objects.get(nome=nomeBloco)
        except Exception as e:
            print('Bloco nao encontrado: %s' % (e))
            # print(bloco)
            pass
            # continue
        
        try:
            if(nomeSetor != ""):
                setor=Setor.objects.get(nomeNovo=nomeSetor)
        except Exception as e:
            print('Setor nao encontrado: %s' % (e))
            # s = Setor(nomeNovo=nomeSetor)
            # s.save()
            # print(s)
            continue
            
        
        # try:
        #     it = DependenciaSetor.objects.get(nome__iexact=nomeAnterior)
        #     it.nome = nomeAnterior
        #     it.nomeNovo=nomeDependenciaNovo
        #     it.bloco=bloco
        #     it.setor=setor
        #     it.save()
        #     # print("salvou: " + str(it))
        # except Exception as e:
        #     # print(str(e))
        #     # print("Ainda nao existe")
        try:
            it = DependenciaSetor(nome=nomeAnterior, nomeNovo=nomeDependenciaNovo, bloco=bloco, setor=setor)
            it.save()
            i = i+1
            print(it)
        except IntegrityError as e: 
            if 'Unique constraint' in e.message:
                continue
        except Exception as e:
            print(linha)
            print('DependenciaSetor: %s' % (e))
            continue
    
    except Exception as e:
        print(e)
        print(linha)
        # print('ficheiro %s, linha %d: %s' % (filename, reader.line_num, e))

print(i)