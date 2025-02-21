#Exercício Python 007: 
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#Importando bibliotecas
import math

#Pegando as informações do user.
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
print('\n')

#Fazendo calculos
calculo = (n1  + n2) / 2

#Exibindo resultados na tela
print('Nota 1: {}\nNota 2: {}\nMédia: {:.1f}\n'.format(n1,n2,calculo))