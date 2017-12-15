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
from django.db.models import Q
from app.models import *

itens = Item.objects.filter(~Q(dependenciaEncontrada=None),estado=-1, dependencia__bloco__nome='Z_ANTIGO')
print(itens.count())

# s = set()
# for i in itens:
#     s.add(i.dependencia)