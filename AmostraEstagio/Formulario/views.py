#encoding:utf-8
from django.shortcuts import render
from AmostraEstagio.Formulario.forms import FormularioContato
from django.http import HttpResponseRedirect
from AmostraEstagio.Formulario.models import Universitario

def formulario_contato(request):
	#processa o que está no form submetido
	context = {}
	interesses = [
		'Banco de Dados','Algoritmos','Desenvolvimento Web','Desenvolvimento Mobile',
		'Inteligência Artificial','Infraestrutura','Gerencial','Levantamento de Requisitos'
	]
	if request.method == 'POST':
		
		form = FormularioContato(request.POST)
		if form.is_valid():	
			print "Form Valido: ", form.clean()
			#print "interesse: %s" % request.POST['interesse']
			#print request.POST['interesse']
			interesses_list = get_interesses_array(request.POST['interesse'])
			
			print(interesses_list)
			
			u = Universitario()
			
			u.nome = form.cleaned_data['nome']	
			u.faculdade = form.cleaned_data['faculdade']
			u.curso = form.cleaned_data['curso']
			u.periodo = form.cleaned_data['periodo']
			u.idade = form.cleaned_data['idade']
			u.telefone = form.cleaned_data['telefone']
			u.email = form.cleaned_data['email']
			u.interesse_algoritmos = interesses_list[0]
			u.interesse_banco_de_dados = interesses_list[1]
			u.interesse_des_web = interesses_list[2]
			u.interesse_des_mobile = interesses_list[3]
			u.interesse_inteligencia_artificial = interesses_list[4]
			u.interesse_infra = interesses_list[5]
			u.interesse_gerencial = interesses_list[6]
			u.interesse_requisitos = interesses_list[7]
			u.trabalho_sta_projeto = form.cleaned_data['trabalho_sta_projeto']
			u.trabalho_sta_des_software = form.cleaned_data['trabalho_sta_des_software']
			u.trabalho_sta_pesq_des = form.cleaned_data['trabalho_sta_pesq_des']
			u.trabalho_sta_infra = form.cleaned_data['trabalho_sta_infra']
			u.materias_mais_gostou = form.cleaned_data['materias_mais_gostou']
			u.materias_menos_gostou = form.cleaned_data['materias_menos_gostou']
			u.materias_melhor_desempenho = form.cleaned_data['materias_melhor_desempenho']
			u.atividade_extracurricular = form.cleaned_data['atividade_extracurricular']	
			u.opiniao_aplicacao_relevante = form.cleaned_data['opiniao_aplicacao_relevante']					
			u.opiniao_feira = form.cleaned_data['opiniao_evento']				
			u.opiniao_stand_sta = form.cleaned_data['opiniao_stand_stoneage']					
			
			#print u
			u.save()
			return HttpResponseRedirect('/formulario/obrigado/')
		else:
			context = {'form': form, 'interesses': interesses}
			return render(request, 'formulario_cadastro.html', context)
			
	else: #prepara a página em branco pra mostrar pro usuário
		form = FormularioContato()
		
		context = {'form': form, 'interesses': interesses}
		
	return render(request, 'formulario_cadastro.html', context)
	
def formulario_obrigado(request):
	if request.method == "POST":
		return HttpResponseRedirect('/formulario')
	else:
		return render(request, 'cadastro_efetuado.html')

def get_interesses_array(interesses_string):
	#print interesses_string
	begin_pos = 0
	bar_pos = 0
	#interesse_list = [0,0,0,0,0,0,0,0]
	interesse_list = []
	interesses = [
		'Algoritmos','Banco de Dados','Desenvolvimento Web','Desenvolvimento Mobile',
		'Inteligência Artificial','Infraestrutura','Gerencial','Levantamento de Requisitos'
	]
	
	interesses_ordenados = interesses_string.upper().split("|")
	interesses_ordenados = map(lambda x: x.strip(),interesses_ordenados)
	
	print "ordenados: ", interesses_ordenados
	
	for interesse in interesses:
		search_key = interesse.decode("utf-8").upper()
		print "tentei achar: %s" % search_key
		interesse_list.append(interesses_ordenados.index(search_key))
	
	return interesse_list
