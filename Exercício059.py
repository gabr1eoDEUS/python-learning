#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor :'))

sair = 0
while sair != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair')
    opc = int(input('Qual é a opção? '))

    if opc == 1:
        print('\nEscolhida: Soma')
        print(f'{n1} + {n2} = {n1+n2}\n')
    elif opc == 2:
        print('\nEscolhida: multiplicar')
        print(f'{n1} x {n2} = {n1*n2}\n')
    elif opc == 3:
        if n1 > n2:
            print('\nEscolhida: maior')
            print(f'{n1} é maior que {n2}\n')
        else:
            print(f"{n2} é maior que {n1}\n")
    elif opc == 4:
        print('\nInforme os novos valores.\n')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor :'))
    elif opc == 5:
        sair = 5