from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import *
from AmostraEstagio.Formulario.views import formulario_contato, formulario_obrigado

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AmostraEstagio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^hello/$', hello),
	#url(r'^formulario/$', mostrar_formulario),
	url(r'^formulario/$', formulario_contato),
	url(r'^formulario/obrigado/$', formulario_obrigado),

    url(r'^admin/', include(admin.site.urls)),
)
