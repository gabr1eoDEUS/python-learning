#Exercício Python 015: 
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Importando bibliotecas
import math

#Cabealho
print('ALUGUEL de CARROS\n')

#Pegandos as informações do user.
km_percorridos = float(input('Quantos KM foram percorridos?'))
dias_alugado = float(input('Quantos dias foram alugados?'))

#Fazendo lógica
custo_por_km = km_percorridos * 0.15
custo_aluguel = dias_alugado * 60 
custo_geral = custo_por_km + custo_aluguel

print('\nVocê rodou: {}km\nPor: {:.0f} dias\nSeu custo é de: R${}'.format(km_percorridos,dias_alugado,custo_geral))