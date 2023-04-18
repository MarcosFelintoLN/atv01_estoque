from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('cadastrar/',views.cadastrar,name='cadastrar_produto.html')
]