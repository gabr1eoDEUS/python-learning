#Exercício Python 051: 
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))


for c in range(9):
    termo = primeiro_termo + c * razao
    print(f'{termo}', end=' >')
print(' Acabou os termos!')