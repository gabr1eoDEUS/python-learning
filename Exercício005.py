#Exercício Python 005: 
#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))

suce = num + 1
ante = num - 1

print('Número digitado: {}\nSucessor: {}\nAntecessor: {}\n'.format(num,suce,ante))