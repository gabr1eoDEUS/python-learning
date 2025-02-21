#Exercício Python 010: 
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

#Importando biblioteca
import math 

#Pegando as informações do user.
dinheiro = float(input('Dinheiro R$:'))
print('\n')

#Convertendo REAIS em DÓLAR
dolar = dinheiro / 3.27

print('com R${} você pode comprar US${:.2f}.'.format(dinheiro,dolar))