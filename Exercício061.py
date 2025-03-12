#Exercício Python 061: 
#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

c = 0

while c < 10:
    termo = primeiro_termo + c * razao
    print(f'{termo}', end=' >')
    c+=1
print(' Acabou os termos!')