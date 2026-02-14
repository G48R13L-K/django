"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from core.views import fechar_categoria, home, listarChamados, fechar_chamado, novaCategoria, novoChamado
from core.views import editar_chamado, editar_categoria, api_chamados
from core.views import ListarCategoriaView

urlpatterns = [
path('admin/', admin.site.urls), 
path('', home),
path('lista_chamados/', listarChamados),
path('novo_chamado/', novoChamado),
path('fechar-chamado/<int:id>', fechar_chamado, name='fechar-chamado'),
path('lista-categorias/', ListarCategoriaView.as_view(), name='listar-categorias'),
path('nova_categoria/', novaCategoria),
path('fechar-categoria/<int:id>', fechar_categoria, name='fechar-categoria'),
path('editar_chamado/<int:id>', editar_chamado, name='editar_chamado'),
path('editar_categoria/<int:id>', editar_categoria, name='editar_categoria'),
path('api/chamados/', api_chamados, name='listar-chamados-api')
]