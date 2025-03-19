#Exercício Python 074: 
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.]
from random import randint
x = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
xt = (x)
maior = xt[0]
menor = xt[0]
print(f'O valores sorteados foram: {xt}')
for i in xt:
    if i > maior:
        maior = i
    if i < menor:
        menor = i 
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')