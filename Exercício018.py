#Exercício Python 018: 
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do 
#seno, cosseno e tangente desse ângulo

#Importando bibliotecas
import math

#Pegando as informações do user.
angulo = float(input('Angulo: '))
print('\n')

#Fazendo lógica

seno = math.sin(math.radians(angulo)) 
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

#Exibindo valores na tela
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}\n'.format(seno,cosseno,tangente))