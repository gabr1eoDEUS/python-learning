#Exercício Python 025: 
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Nome completo: ')).upper()
silva = 'SILVA' in nome

print('{} tem SILVA no nome?'.format(nome.upper()))
print(silva)