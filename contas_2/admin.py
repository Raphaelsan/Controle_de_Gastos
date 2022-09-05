from django.contrib import admin
from contas_2.models import Categoria, Transacao, Fonte\
    #, Credito

admin.site.register(Categoria)
admin.site.register(Transacao)
# admin.site.register(Credito)
admin.site.register(Fonte)

# Register your models here.
