#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from time import sleep
import math

fact = int(input('Digite um número: '))
print('Calcular seu fatorial')
n = fact
f = 1
while n > 0:
    print(f'{n}', end='')
    print('x' if n > 1 else '=',end='')
    f *= n
    n -=1
print(f'{f}')