#coding: utf-8
#Problema: Faça um decorator que retorne um <strong></strong> para a string fornecida
def my_decorator (func):
    def do_stuff(s):
        return ("<strong> %s </strong>" % s)
    return do_stuff

@my_decorator
def outrodecorator(para):
	return para

if __name__ == '__main__':
   print outrodecorator("lalala")