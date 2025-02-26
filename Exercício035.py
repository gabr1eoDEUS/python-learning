#Exercício Python 035: 
#Desenvolva um programa que leia o comprimento de três retas 
#e diga ao usuário se elas podem ou não formar um triângulo.

#Cabeçalho
print('='*22)
print('ANALISADOR DE UM TRIÂNGULO')
print('='*22)

#Pegando as informações do user.
a = float(input('Comprimento 1: '))
b = float(input('Comprimento 2: '))
c = float(input('Comprimento 3: '))


if a+b > c and a+c > b and b+c >a:
    print(f'com {a} , {b} e {c}. Pode formar um triângulo.')
else:
    print('Com esses comprimentos não pode formar um triângulo.')