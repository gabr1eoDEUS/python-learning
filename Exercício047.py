#Exercício Python 047: 
#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#Cabeçalho
print('Números pares usando FOR\n')

#Lógica
for pares in range(2, 51, 2):
    print(f'Números pares: {pares}')
print('\nFinal do programa.')