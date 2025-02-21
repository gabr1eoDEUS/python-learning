#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

#Pegando as informações do user
nome = str(input('Nome completo: ')).strip()

removedor_de_espacos = nome.replace(" ","") 
separador_de_nome = nome.split()

#Print apenas para organização
print('\n')

#Fazendo lógica
print('NOME COM LETRAS MAIÚSCULAS: {}'.format(nome.upper()))
print('NOME COM LETRAS MINÚSCULAS: {}'.format(nome.lower()))
print('TOTAL DE LETRAS(SEM CONSIDERAR ESPAÇOS): {}'.format(len(removedor_de_espacos)))
print('QUANTAS LETRAS TEM O PRIMEIRO NOME: {}'.format(len(separador_de_nome[0])))
