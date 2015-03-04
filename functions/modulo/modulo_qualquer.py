#coding: utf-8

from datetime import datetime as datahora

def que_horas_sao():
	print('executando no dia %s, às %s horas' %(datahora.now().date(),datahora.now().time()))