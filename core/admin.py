from django.contrib import admin

# Register your models here.
from .models import Chamado, Categoria, Pessoa, Equipamento

# Isso faz o modelo "Chamado" aparecer no /admin
admin.site.register(Chamado)
admin.site.register(Categoria)
admin.site.register(Equipamento)
admin.site.register(Pessoa)