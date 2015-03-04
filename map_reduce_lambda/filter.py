#coding: utf-8
#Escreva um script que filtre os números positivos dentro da lista abaixo
valores = [10, 4, -1, 3, 5, -9, -11]

def pos(n):
	
	if n > 0:
	    return n

print filter(pos, valores)