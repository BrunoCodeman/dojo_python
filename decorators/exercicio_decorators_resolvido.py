#coding: utf-8
#Problema: Faça um decorator que retorne um <strong></strong> para a string fornecida

def label_decorator(func):
   def func_wrapper(name):
       return "<label>{0}</label>".format(func(name))
   return func_wrapper

@label_decorator
def ola_pessoa(nome):
	return 'olá, %s' % nome

if __name__ == '__main__':
	print ola_pessoa('bruno')

