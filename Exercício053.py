#Exercício Python 053: 
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

palavra = str(input('Digite uma frase: ')).lower().replace(' ', '')
frase_invertida = ''

for i in range(len(palavra) - 1, -1, -1):
    frase_invertida += palavra[i]

print(f'O inverso de {palavra} é {frase_invertida}\n')

if palavra == frase_invertida:
    print(f'A frase {palavra} é um POLÍNDROMO\n')
else:
    print(f'A frase {palavra} não é um POLÍNDROMO')