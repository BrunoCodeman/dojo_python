#coding: utf-8
from modulo.modulo_qualquer import que_horas_sao

class MyClass:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	#método protected
	def _print_a(self):
		print('a vale %s' %str(self.a))	

	#método private
	def __print_b(self):
		print('b vale %s' %str(self.b))
	
	def method(self):
		self._print_a()
		self.__print_b()

	@classmethod
	def class_method(cls, a, b):
		print(a + b)

	@staticmethod
	def static_method(a, b):
		print(a + b)

if __name__ == '__main__':
	que_horas_sao()
	MyClass.class_method(3,4)
	MyClass.static_method(5,6)
	
	objeto = MyClass(1, 2)
	objeto.method()
	objeto.static_method(3,4)
	print objeto.__dict__
