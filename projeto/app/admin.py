from django.contrib import admin
from .models import Topico, Pagina, RegistroAcesso, Produto, Filme, Cliente

admin.site.register(Topico)
admin.site.register(Pagina)
admin.site.register(RegistroAcesso)
admin.site.register(Produto)


class FilmeAdmin(admin.ModelAdmin):
    fields = ['titulo','ano', 'duracao']
    search_fields = ['titulo', 'ano']
    list_filter = ['titulo', 'duracao']
    list_display = ['titulo', 'duracao','ano']

class ClienteAdmin(admin.ModelAdmin):
    fields = ['nome','sobrenome', 'email']
    search_fields = ['nome', 'sobrenome', 'email']
    list_filter = ['nome','sobrenome','email']
    list_display = ['nome','sobrenome','email']

admin.site.register(Filme, FilmeAdmin)
admin.site.register(Cliente, ClienteAdmin)
