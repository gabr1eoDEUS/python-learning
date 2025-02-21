#Exercício Python 016: 
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Importando bibliotecas
import math

#Pegando as informações do user.
num = float(input('Número: '))
print('\n')

#Convertendo número para porção inteira.
print('Número digitado: {}\nPorção inteira: {}\n'.format(num,math.floor(num)))