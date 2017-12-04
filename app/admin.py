from django.contrib import admin
from app.models import *

class DependenciaSetorInline(admin.StackedInline):
    model = DependenciaSetor
    can_delete = True
    verbose_name_plural = 'Dependencia do setor'
    extra = 0

class SetorAdmin(admin.ModelAdmin):
    inlines = (DependenciaSetorInline,)


class InventarioAdmin(admin.ModelAdmin):
    def setor_mod(self, obj):
        if(obj.setor == None):
            return obj.item.dependencia.nome
        else:
            return obj.setor

    readonly_fields = ('estado','obs','item','createdAt','updatedAt',)
    list_display = ('item', 'estado','obs','setor_mod','aferidores',)
    list_filter = ('estado','setor','aferidores',)
    ordering = ()

admin.site.register(Setor, SetorAdmin)
admin.site.register(DependenciaSetor)
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Item)
admin.site.register(Aferidor)
# Register your models here.

