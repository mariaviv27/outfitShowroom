from django.contrib import admin
from .models import Estilo, Ocasion, Outfit

class EstiloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion') 
    search_fields = ('nombre', 'descripcion')

class OcasionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion') 
    search_fields = ('nombre', 'descripcion')

class OutfitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion') 
    search_fields = ('nombre', 'estilo', 'ocasion')


admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Ocasion, OcasionAdmin)
admin.site.register(Outfit, OutfitAdmin)


