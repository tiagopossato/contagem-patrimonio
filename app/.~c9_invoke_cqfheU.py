from django.contrib import admin
from app.models import *

class DependenciaSetorInline(admin.StackedInline):
    model = DependenciaSetor
    can_delete = True
    verbose_name_plural = 'Dependencia do setor'
    extra = 0

class SetorAdmin(admin.ModelAdmin):
    inlines = (DependenciaSetorInline,)

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'patrimonio', 'sipac', 'dependencia',)
    list_display = ('nome', 'patrimonio', 'sipac', 'dependencia',)
    ordering = ('patrimonio',)
    list_filter = ('dependencia',)

    def has_delete_permission(self,requestt, obj=None):
        return False

    def has_add_permission(self,request):
        return False

class InventarioAdmin(admin.ModelAdmin):
    readonly_fields = ('item', 'estado', 'obs', 'createdAt','updatedAt','aferidores','setor',)
    list_display = ('item', 'estado', 'setor','createdAt', 'aferidores',)
    ordering = ('item',)
    list_filter = ('setor','aferidores','estado',)

    def has_delete_permission(self,requestt, obj=None):
        return False

    def has_add_permission(self,request):
        return False
        
# class AferidorInventarioInline(admin.StackedInline):
#     model = Aferidor
#     can_delete = True
#     verbose_name_plural = 'Usuario'
#     extra = 0

# class InventarioAdmin(admin.ModelAdmin):
#     inlines = (AferidorInventarioInline,)

admin.site.register(Setor, SetorAdmin)
admin.site.register(DependenciaSetor)
admin.site.register(Inventario,InventarioAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Aferidor)
# Register your models here.
