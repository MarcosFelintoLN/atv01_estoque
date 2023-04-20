from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.listar,name='index.html'),
    path('cadastrar/',views.cadastrar,name='cadastrar_produto.html'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
    path('editar/<int:pk>/', views.editar, name='editar')
]