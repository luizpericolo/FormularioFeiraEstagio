from django import forms

class FormularioContato(forms.Form):

	#error_css_class = 'error'

	#dados pessoais
	nome = forms.CharField(max_length=150, label="Nome: ")
	faculdade = forms.CharField(initial="UFRJ", label="Faculdade: ")
	curso = forms.CharField(label="Curso: ")
	periodo = forms.IntegerField(max_value=15, label="Periodo: ")
	idade = forms.IntegerField(max_value=100, label="Idade: ")
	telefone = forms.CharField(required=False, label="Telefone: ")
	email = forms.EmailField(max_length=100, label="Email: ")
	
	#dados academicos
	trabalho_sta_projeto = forms.BooleanField(required=False, initial=False, label='Projeto(Clientes Externos)', widget=forms.CheckboxInput(attrs={'class':'checkbox'}))
	trabalho_sta_des_software = forms.BooleanField(required=False, initial=False, label='Desenvolvimento de Software', widget=forms.CheckboxInput(attrs={'class':'checkbox'}))
	trabalho_sta_pesq_des = forms.BooleanField(required=False, initial=False, label='Pesquisa e Desenvolvimento', widget=forms.CheckboxInput(attrs={'class':'checkbox'}))
	trabalho_sta_infra = forms.BooleanField(required=False, initial=False, label='Infraestrutura', widget=forms.CheckboxInput(attrs={'class':'checkbox'}))
	
	materias_mais_gostou = forms.CharField(required=True, label="Matérias que você MAIS gostou no seu curso: (Abreviações estão valendo)", widget=forms.Textarea)
	materias_menos_gostou = forms.CharField(required=True, label="Matérias que você MENOS gostou no seu curso: (Abreviações estão valendo)", widget=forms.Textarea)
	materias_melhor_desempenho = forms.CharField(required=True, label="Matérias que você teve o MELHOR desempenho: (Abreviações estão valendo)", widget=forms.Textarea)
	
	atividade_extracurricular = forms.CharField(required=True, label="Você já participou de alguma atividade extracurricular? (p.e. Maratona de programação, OBI, Grupo de Robótica)", widget=forms.Textarea)
	
	#dados do evento
	opiniao_evento = forms.CharField(required=True, label="O que você achou do evento?", widget=forms.Textarea)
	opiniao_stand_stoneage = forms.CharField(required=True, label="O que você achou do 'stand' da StoneAge?", widget=forms.Textarea)
	opiniao_aplicacao_relevante = forms.CharField(required=True, label="Lenvando em consideração tudo que você conhece sobre tecnologia, qual a tecnologia mais revolucionária que você lembra?", widget=forms.Textarea)