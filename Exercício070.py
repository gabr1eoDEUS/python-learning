#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 
print('LOJA PREÇO BAIXO')
print('-'*17)
gastos = maior1000 = 0
precobaixo = 999999999
nproduto = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    if preco > 1000:
        maior1000+=1
    gastos += preco
    if preco < precobaixo:
            nproduto = produto
            precobaixo = preco
    opc = ''
    while opc != 'S' and opc != 'N':
        opc = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if opc == 'N':
        break
print(f'Total de gastos: R${gastos}')
print(f'{maior1000} produtos custam mais de R$1000.')
print(f'O produto mais barato foi {nproduto} que custa R${precobaixo}')