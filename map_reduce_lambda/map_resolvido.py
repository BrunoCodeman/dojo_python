#coding: utf-8
##Data uma lista de números, gere outra lista de numeros com a raiz quadrada desses números
import math
lista1 = [1, 4, 9, 16, 25]
lista2 = map(math.sqrt, lista1)
print lista2