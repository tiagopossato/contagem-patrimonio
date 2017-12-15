from django.contrib import admin
from app.models import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class DependenciaSetorInline(admin.StackedInline):
    model = DependenciaSetor
    can_delete = True
    verbose_name_plural = 'Dependencia do setor'
    extra = 0

class SetorAdmin(admin.ModelAdmin):
    inlines = (DependenciaSetorInline,)
    list_display = ('nomeNovo', 'nome')
    ordering = ('-nomeNovo',)

class ItemInline(admin.StackedInline):
    model = Item
    can_delete = False
    can_add = False
    verbose_name_plural = 'Itens'
    extra = 0
    
class DependenciaSetorAdmin(admin.ModelAdmin):
    inlines = (ItemInline,)
    list_display = ('nome', 'nomeNovo', 'setor','bloco',)
    list_filter = ('setor','bloco',)
    ordering = ('bloco',)
    
class InventarioAdmin(admin.ModelAdmin):
    # def localizacao(self, obj):
    #     if(obj.setorTmp==None):
    #         return obj.dependencia
            
    #     if(len(obj.setorTmp)==0):
    #         return obj.item.dependencia.nome
    #     else:
    #         return obj.dependencia
    # def bloco(self, obj):
    #     if(obj.dependencia == None):
    #         return "Sem Bloco"
    #     else:
    #         return obj.dependencia.bloco
            
    readonly_fields = ('item',)
    list_display = ('item', 'item_id', 'estado','dependencia','setorTmp','obs','aferidores',)
    list_filter = ('estado','dependencia','setorTmp','aferidores','obs',)
    search_fields = ['setorTmp', 'item__nome','item__id']
    ordering = ()

class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sipac', 'dependenciaOriginal', 'dependenciaEncontrada','estado','setorTmp','obs','aferidores',)
    list_filter = ('dependencia','dependencia__bloco',)
    ordering = ('dependencia',)
    
admin.site.register(Setor, SetorAdmin)
admin.site.register(DependenciaSetor,DependenciaSetorAdmin)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Bloco)
