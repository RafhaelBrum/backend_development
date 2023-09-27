from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('helloworld/', views.helloworld, name='helloworld'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('pagina-list/', views.PaginaListView.as_view(), name='pagina-list'),
    path('criar-topico/', views.criar_topico, name='criar-topico'),
    path('criar-produto/', views.criar_produto, name='criar-produto'),
    path('lista-produtos/', views.lista_produtos, name='lista-produtos'),
    path('help/', views.HelpView.as_view(), name='helpView')
]
