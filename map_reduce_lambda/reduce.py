#coding: utf-8
#Escreva um script que some todos os números de 0 a 100
from operator import add #necessário para obter a função de soma
valores = range(0,101)

print reduce(add, valores)