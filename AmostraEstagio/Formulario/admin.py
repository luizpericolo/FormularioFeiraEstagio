from django.contrib import admin
from AmostraEstagio.Formulario.models import Universitario

class UniversitarioAdmin(admin.ModelAdmin):
	list_display = ('nome','faculdade','email')
	

admin.site.register(Universitario, UniversitarioAdmin)

