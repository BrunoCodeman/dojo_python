#coding: utf-8
##Crie uma classe com um inicializador, um método que conte até 10 
## e imprima os números enquanto isso. A classe e os métodos devem
## ter docstring os descrevendo. No fim do script, exiba os 
##atributos e a documentação da classe

class MinhaClasse:
	'''
		Classe MinhaClasse
	'''
	def __init__(self):
		'''
			Método inicializador
		'''
		pass

	def conta_ate_dez(self):
		'''
			Método que conta até dez
		'''
		for i in range(0,11):
			print i


if __name__ == '__main__':
	objeto = MinhaClasse()
	objeto.conta_ate_dez()
	print '%s \n\n' % dir(objeto)
	help(objeto)
