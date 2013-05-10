from django.db import models

class Universitario(models.Model):
	nome = models.TextField()
	faculdade = models.TextField()
	curso = models.TextField()
	periodo = models.IntegerField()
	idade = models.IntegerField()
	telefone = models.TextField()
	email = models.EmailField()
	
	interesse_algoritmos = models.IntegerField()
	interesse_banco_de_dados = models.IntegerField()
	interesse_des_web = models.IntegerField()
	interesse_des_mobile = models.IntegerField()
	interesse_inteligencia_artificial = models.IntegerField()
	interesse_infra = models.IntegerField()
	interesse_gerencial = models.IntegerField()
	interesse_requisitos = models.IntegerField()
	
	trabalho_sta_projeto = models.BooleanField()
	trabalho_sta_des_software = models.BooleanField()
	trabalho_sta_pesq_des = models.BooleanField()
	trabalho_sta_infra = models.BooleanField()
	
	materias_mais_gostou = models.TextField()
	materias_menos_gostou = models.TextField()
	materias_melhor_desempenho = models.TextField()
	
	atividade_extracurricular = models.TextField()
	opiniao_aplicacao_relevante = models.TextField()
	
	opiniao_feira = models.TextField()
	opiniao_stand_sta = models.TextField()