from django.contrib import admin

# Register your models here.
from .models import Producto,Cliente,Factura,DetalleFactura

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion']
    list_display = ('descripcion','precio','stock','iva','creacion')
    ordering = ('descripcion',)
    search_fields = ('descripcion',)
    list_filter = ('descripcion',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Factura)
#USUARIO ADMINISTRADOR
#usuario: admin
#password: admin123