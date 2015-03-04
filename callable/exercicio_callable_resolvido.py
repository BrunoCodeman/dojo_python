#coding: UTF-8
##Crie um script que obtenha todos os atributos da classe cachorro,
## separe métodos e atributos em listas diferentes e os exiba em sequência

class Cachorro(object):

	def __init__(self, nome='Luke Skywalker', raca='Cocker Spaniel'):
		self.nome = nome
		self.raca = raca

	def latir(self):
		print('woof!')

	def lamber_a_cara_do_dono(self):
		print('Melhor limpar essa baba...')


if __name__ == '__main__':
	cao = Cachorro()
	atributos = dir(cao)
	metodos, propriedades = [],[]
	for atributo in atributos:
		print atributo
		if callable(getattr(cao,atributo)):
			metodos.append(atributo)
		else:
			propriedades.append(atributo)
	print(['%s: metodo' % item for item in metodos])
	print(['%s: propriedade' % item for item in propriedades])
