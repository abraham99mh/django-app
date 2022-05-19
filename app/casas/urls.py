from django.urls import path
from . import views

urlpatterns = [
    path('create', views.HouseCreation.as_view(), name='house_create'),
    path('list', views.CasasList.as_view(), name='house_list'),
    path('<str:nombre>/update', views.CasasUpdate.as_view(), name='house_update')
]
