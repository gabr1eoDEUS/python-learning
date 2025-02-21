#Exercício Python 008: 
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#Importando bibliotecas
import math

#Cabeçalho
print('Convertendo METROS em MILÍMETROS e CENTÍMETROS\n')

#Pegando as informações do user.
metros = float(input('METROS:'))
print('\n')

#Fazendo calculos
mili = metros * 1000
cen = metros * 100

#Exibindo resultados na tela.
print('METROS: {}m\nMILÍMETROS: {}mm\nCENTÍMETROS:{}cm\n'.format(metros,mili,cen))