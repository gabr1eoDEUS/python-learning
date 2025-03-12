#Exercício Python 063: 
#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N 
#primeiros elementos de uma Sequência de Fibonacci. 

n = int(input('Quantos termos você quer mostrar? '))

f1 = 0
f2 = 1
f = 0
i = 0
print('-'*30)
while i < n:
    print(f'{f1}', end='> ')
    f = f1 + f2
    f1 = f2
    f2 = f
    i+=1 
print(' FIM')
print('-'*30)