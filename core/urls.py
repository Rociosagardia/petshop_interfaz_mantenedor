from django.urls import path
from .views import index, editor_producto,lista_producto,producto_ficha


urlpatterns = [
    path('', index, name="index"),
    path('editorProducto/<action>/<id>', editor_producto, name="editorProducto"),

    path('producto_tienda/', lista_producto, name="tiendaProducto"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
]