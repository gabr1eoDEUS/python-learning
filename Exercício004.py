#Exercício Python 004: 
#Faça um programa que leia algo pelo teclado e mostre na tela 
#o seu tipo primitivo e todas as informações possíveis sobre ele.

x = str(input('Digite algo: '))

print('O tipo primitivo é: ',type(x))
print(f'{x}: é ALFANUMÉRICO? ', x.isalnum())
print(f'{x}: são LETRAS? ',x.isalpha())
print(f'{x}: são NÚMEROS? ',x.isnumeric())
print(f'{x}: todas as são MAIÚSCULAS? ',x.isupper())