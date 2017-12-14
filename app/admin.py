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

# class ItemInline(admin.StackedInline):
#     model = Item
#     can_delete = False
#     can_add = False
#     verbose_name_plural = 'Itens'
#     extra = 0
    
class DependenciaSetorAdmin(admin.ModelAdmin):
    def quantidadeItensAntes(self, obj):
        return int(Item.objects.filter(dependencia = obj).count())
        
    def quantidadeItensEncontrados(self, obj):
        return int(Item.objects.filter(dependenciaEncontrada = obj).count())
    # inlines = (ItemInline,)
    list_display = ('nome', 'nomeNovo', 'setor','bloco','quantidadeItensAntes','quantidadeItensEncontrados')
    list_filter = ('setor','bloco',)
    list_per_page = 400
    # ordering = ('-quantidadeItens',)
    
# class InventarioAdmin(admin.ModelAdmin):
#     # def localizacao(self, obj):
#     #     if(obj.setorTmp==None):
#     #         return obj.dependencia
            
#     #     if(len(obj.setorTmp)==0):
#     #         return obj.item.dependencia.nome
#     #     else:
#     #         return obj.dependencia
#     # def bloco(self, obj):
#     #     if(obj.dependencia == None):
#     #         return "Sem Bloco"
#     #     else:
#     #         return obj.dependencia.bloco
            
#     readonly_fields = ('item',)
#     list_display = ('item', 'item_id', 'estado','dependencia','setorTmp','obs','aferidores',)
#     list_filter = ('estado','dependencia','setorTmp','aferidores','obs',)
#     search_fields = ['setorTmp', 'item__nome','item__id']
#     ordering = ()

class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome','sipac','dependencia','estado','aferidores',)
    # list_filter = ('dependencia','dependenciaEncontrada','estado','aferidores','dependencia__bloco','dependenciaEncontrada__bloco')
    readonly_fields = ('nome','dependencia','patrimonio', 'sipac',)
    list_filter = ('dependenciaEncontrada','dependenciaEncontrada__bloco','estado','aferidores','dependencia','dependencia__bloco',)
    # search_fields = ['sipac','aferidores']#, 'nome','id', 'obs', 'patrimonio']
    list_per_page = 8000
    ordering = ('dependenciaEncontrada__bloco__nome','patrimonio',)

admin.site.register(Setor, SetorAdmin)
admin.site.register(DependenciaSetor,DependenciaSetorAdmin)
# admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Bloco)
admin.site.site_header = 'Relatorio de Inventario'
admin.site.site_title = 'IFC'
