#coding:utf-8
##Crie uma lista com 10 elementos e exiba apenas aqueles que são ímpares
lista = [n for n in range(1,11) if n %2==1]
print lista

###########################################################################
##Filtre as pessoas cujo nome começam com A e exiba seus nomes
class Pessoa(object):
	def __init__(self, nome):
		self.nome = nome


pessoas = [Pessoa('Ana'), Pessoa('Daniela'), Pessoa('Alberto'), Pessoa('Alice'), Pessoa('Claudio')]
printavelComA = [pessoa.nome for pessoa in pessoas if pessoa.nome[0]=='A' ]
print printavelComA