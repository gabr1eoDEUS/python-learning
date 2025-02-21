#Exercício Python 019: 
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#Importando bibliotecas
import random

#Pegando as informações do user.
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))

#Sorteando aluno
sorteio = random.choice([n1,n2,n3,n4])

#Exibindo valores na tela
print('Aluno sorteado: {}'.format(sorteio))