#Exercício Python 009: 
#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

#Importando biblioteca
import math

#Cabeçalho
print('TABUADA\n')

#Pegando informações do user.
num = int(input('Número: '))
print('\n')

#Exibindo valores na tela
print('===============')
print('{}  x  1 = {}'.format(num,(num * 1)))
print('{}  x  2 = {}'.format(num,(num * 2)))
print('{}  x  3 = {}'.format(num,(num * 3)))
print('{}  x  4 = {}'.format(num,(num * 4)))
print('{}  x  5 = {}'.format(num,(num * 5)))
print('{}  x  6 = {}'.format(num,(num * 6)))
print('{}  x  7 = {}'.format(num,(num * 7)))
print('{}  x  8 = {}'.format(num,(num * 8)))
print('{}  x  9 = {}'.format(num,(num * 9)))
print('{}  x 10 = {}'.format(num,(num * 10)))
print('===============')