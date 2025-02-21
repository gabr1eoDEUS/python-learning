#Exercício Python 014: 
#Escreva um programa que converta uma temperatura digitando em graus Celsius
#e converta para graus Fahrenheit.

#Importando bibliotecas
import math

#Cabeçalho
print('CONVERSOR de GRAUS CELSIUS EM FAHRENHEIT\n')

#Pedindo as informações ao user.
celsius = float(input('Graus em °C:'))
print('\n')

#Convertendo os valores obtidos.
fahrenheit = (celsius*9/5) + 32

#Exibindo os valores na tela.
print('Graus em °F:{}'.format(fahrenheit))