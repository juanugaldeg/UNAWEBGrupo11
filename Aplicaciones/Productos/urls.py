from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('registrarProductos/', views.registrarProductos),
    path('edicionProductos/<codigo>', views.edicionProductos),
    path('editarProductos/', views.editarProductos),
    path('eliminarProductos/<codigo>', views.eliminarProductos)
]