#coding: utf-8
##Dada a lista de instâncias da classe pessoa, filtre as pessoas que são maiores de idade

class Pessoa:
	def __init__(self,nome, idade):
		self.nome = nome
		self.idade = idade

pessoas = [Pessoa('Bruno', 29), Pessoa('Gabriel', 24), Pessoa('Clara', 9), Pessoa('Antonia', 1)]
