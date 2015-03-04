#coding: utf-8

##Crie um script que através do shell cria um pasta chamada 'diretorio', 
##cria um arquivo usando a função built-in python, escreve 'Olá, mundo'
## no arquivo e lista o conteúdo da pasta com as permissões

import os
os.system("mkdir diretorio")
arquivo = open("arquivo.txt", "w")
arquivo.write("Ola, mundo")
arquivo.close()

os.system("ls -la")
