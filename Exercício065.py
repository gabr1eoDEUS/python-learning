#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

n = ''
armazenados = num = soma = maior = menor = 0
while n != 'N':
    num = int(input('Digite um número: '))
    armazenados+=1
    soma = soma + num
    total = soma / armazenados
    if num > armazenados:
        maior = num
    else:
        menor = num
    n = str(input('Quer continuar? [S/N] ')).upper()
print(f'Você digitou {armazenados} números e a média foi de {total}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')