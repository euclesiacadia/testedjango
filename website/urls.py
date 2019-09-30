from django.urls.conf import include
#from django.contrib import admin
from django.urls import path
from . import views
app_name = "website"
urlpatterns = [
    path('',views.index,name = "index"),
    path('cadastra_pessoa',views.cadastra_pessoa, name="cadastra_pessoa"),
    path('lista_pessoas',views.lista_pessoas,name = "lista_pessoas"),
]