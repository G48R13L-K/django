from django.contrib import admin

# Register your models here.
from .models import Chamado, Categoria

# Isso faz o modelo "Chamado" aparecer no /admin
admin.site.register(Chamado)
admin.site.register(Categoria)