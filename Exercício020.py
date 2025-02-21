#Exercício Python 020: 
#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Importando as bibliotecas
import math
import random
#from random import shuffle

#Pegando as informações do user.
a1 = str(input('a1 nome: ')) 
a2 = str(input('a2 nome: '))
a3 = str(input('a3 nome: '))
a4 = str(input('a4 nome: '))

sorteando = [a1, a2, a3, a4]
random.shuffle(sorteando)

print('Alunos sorteados: {}'.format(sorteando))