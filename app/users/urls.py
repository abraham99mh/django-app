from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('lados/', views.la_dos, name='la_dos'),
    path('create', views.UserCreation.as_view(), name='user_create')
]