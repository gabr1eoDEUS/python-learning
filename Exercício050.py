#Exercício Python 050: 
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

#Cabeçalho
print('Somando apenas números PARES.\n')

soma = 0
for num in range(1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        print(f'{num} é PAR\n')
        soma += n 
    else:
        print(f'{num} é ÍMPAR\n')
print(f'\nA soma entre todos os números pares é {soma}')