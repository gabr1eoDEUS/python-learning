#Exercício Python 052: 
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Importando bibliotecas
from colorama import Fore,Back,Style

#Pegando as informações do user
n = int(input('Digite um número: '))
tot = 0
for num in range(1, n+1):
    if n % num == 0:
        print('\033[34m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print(f'{num}')
print(f'\nO número {n} foi divisível {tot} vezes.')