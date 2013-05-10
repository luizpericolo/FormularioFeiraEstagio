from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def hello(request):
	return HttpResponse("Hello!")

def mostrar_formulario(request):
	t = get_template("formulario.html")
	c = Context({'url_cadastrar' : 'cadastrar/'})
	
	return HttpResponse(t.render(c))
	