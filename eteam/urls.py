"""eteam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from website.views import IndexTemplateView
from website.views import PessoaListView
from website.views import PessoaCreateView
from website.views import EquipaListView
from website.views import EquipaCreateView
from website.views import MembrosCreateView
#from website.views import MembrosUpdateView
from website.views import MembrosDeleteView
app_name = "website"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='index'),
    path('pessoas/', PessoaListView.as_view(), name = 'website/lista_pessoas'),
    path('equipas/', EquipaListView.as_view(), name='website/lista_equipas'),
    path('pessoa/cadastrar', PessoaCreateView.as_view(), name = 'cadastrar_pessoa'),
    path('equipa/criar/', EquipaCreateView.as_view(), name = 'website/criar_equipa'),
    path('membros/adicionar/', MembrosCreateView.as_view(), name = 'website/adicionar_membros'),
    path('membros/remover/<pk>', MembrosDeleteView.as_view(), name ='remover_membros'),
]
