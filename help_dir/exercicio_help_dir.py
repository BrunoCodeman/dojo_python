#coding: utf-8
##Crie uma classe com um inicializador, um método que conte até 10 
## e imprima os números enquanto isso. A classe e os métodos devem
## ter docstring os descrevendo. No fim do script, exiba os 
##atributos e a documentação da classe

class Contador():
    """ Classe contadora """
    
    def __init__(self):
        pass

    def contar(self):
    	""" Método contador """
    	for x in xrange(1,11):
    		print(x)
    	  
if __name__ == "__main__":
    c = Contador()
    c.contar()

    print dir(c)
    help(c)