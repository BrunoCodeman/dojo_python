#coding:utf-8
##Crie uma lista com 10 elementos e exiba apenas aqueles que são ímpares
lista = xrange(1,11)
print [i for i in lista if i %2 != 0]


###########################################################################
class Pessoa(object):
	def __init__(self, nome):
		self.nome = nome

##Filtre as pessoas cujo nome começam com A e exiba seus nomes
pessoas = [Pessoa('Ana'), Pessoa('Daniela'), Pessoa('Alberto'), Pessoa('Alice'), Pessoa('Claudio')]

pessoas_com_a = [p.nome for p in pessoas if p.nome.startswith('A')]

print pessoas_com_a