from django.contrib import admin
from.models import Maestro,Equipo,Competidores,Torneo

# Register your models here.

class MaestroAdmin(admin.ModelAdmin):
    list_display =['nombre','apellido','grado','telefono']
    search_fields=['nombre','apellido','grado']
    list_filter=['grado']
    list_per_page=10

admin.site.register(Maestro,MaestroAdmin)
admin.site.register(Equipo)
admin.site.register(Competidores)
admin.site.register(Torneo)
