#Exercício Python 038: 
#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

#Importando bibliotecas
from colorama import Fore,Back,Style
from time import sleep
import os

#Laço de Repetição
while True:
    
    #Cabeçalho
    print('Exercício 38 de PYTHON\n')
    print('=====================')
    print('Comparando os NÚMEROS')
    print('=====================''\n')
    
    #Limpando a tela
    def limpa_tela():
        os.system('cls')

    #Filtrando a entrada no input
    try:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor : '))
    except ValueError:
        print('\nDigite apenas números(Inteiros). por favor!\n')
        sleep(2)
        limpa_tela()
        continue

    #Condições
    if n1 > n2:
        print('AGUARDE\nComparando os RESULTADOS:\n')
        print(f'{n1} é maior que {n2}\n')
        print('O primeiro valor é maior.\n')
    elif n2 > n1:
        print('AGUARDE\nComparando os RESULTADOS:\n')
        print(f'{n2} é maior que {n1}\n')
        print('O segundo valor é maior.\n')
    else:
        print('AGUARDE\nComparando os RESULTADOS:\n')
        print(f'{n1} e {n2} tem o mesmo valor.\n')
    
    while True:
        opc = str(input('Deseja executar novamente? [S / N]: ')).upper()
        if opc == 'S':
            limpa_tela()
            sleep(2)
            break
        elif opc == 'N':
            limpa_tela()
            break
        else:
            print('Digite apenas [S] para sim ou [N] para não. Por favor!')
            sleep(3)
            limpa_tela()
            continue
    if opc == 'N':
        break
    
    
    

