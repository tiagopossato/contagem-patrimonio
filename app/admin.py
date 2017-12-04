from django.contrib import admin
from app.models import *

class DependenciaSetorInline(admin.StackedInline):
    model = DependenciaSetor
    can_delete = True
    verbose_name_plural = 'Dependencia do setor'
    extra = 0

class SetorAdmin(admin.ModelAdmin):
    inlines = (DependenciaSetorInline,)

admin.site.register(Setor, SetorAdmin)
admin.site.register(DependenciaSetor)
admin.site.register(Inventario)
admin.site.register(Item)
admin.site.register(Aferidor)
# Register your models here.