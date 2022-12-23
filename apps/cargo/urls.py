from django.urls import path
from .views import * 

urlpatterns = [
    path('cargo/', cargo, name='cargo'),
    path('cadastro/', cadastro, name='cadastroCargo'),
    path('delete/', deleteCargo, name='delete'),
    path('editar/', editarCargo, name='editar'),

]