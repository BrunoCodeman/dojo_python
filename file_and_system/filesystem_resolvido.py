#coding: utf-8

##Crie um script que através do shell cria um pasta chamada 'diretorio', 
##cria um arquivo usando a função built-in python, escreve 'Olá, mundo'
## no arquivo e lista o conteúdo da pasta com as permissões
import os
caminho_do_arquivo = '%s/diretorio' %os.getcwd()
os.system('mkdir %s' % caminho_do_arquivo)
arquivo = open('%s/arquivo.txt' % caminho_do_arquivo,'w')
arquivo.write('Olá, mundo')
arquivo.close()
os.system('cd %s && ls -ll' % caminho_do_arquivo)
