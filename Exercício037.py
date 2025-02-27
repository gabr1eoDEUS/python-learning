#Exercício Python 037: 
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.

#Importando bibliotecas
from colorama import Fore, Back, Style
from time import sleep
import os

#laço de Repetição
while True:

    #Limpando a tela
    def limpa_tela():
        os.system('cls')


    #Cabeçalho
    print(Fore.BLUE+'======================'+Style.RESET_ALL)
    print(' CONVERSOR DE NÚMEROS ')
    print(Fore.BLUE+'======================'+Style.RESET_ALL)

    print('OBS: DIGITE APENAS NÚMEROS INTEIROS, POR FAVOR!\n')
    
    #Pegando as informações do user.
    try:
        num = int(input('Digite um número: '))
        print('\n')
        digito = int(input('Selecione:\n[1] BINÁRIO [2]OCTAL [3]HEXADECIMAL: '))
        print('\n')
    except ValueError:
        print('\n'+Fore.RED+'Digite apenas números, por favor'+Style.RESET_ALL+'!')
        sleep(2)
        limpa_tela()
        continue
    
    if digito == 1:
        print('\nVocê selecionou BINÁRIO:\n')
        print('CARREGANDO...\n')
        sleep(3)
        print(f'{num} convertido para BINÁRIO é: {bin(num)[:2]}\n\n')
    elif digito == 2:
        print('\nVocê selecionou OCTAL:\n')
        print('CARREGANDO...\n')
        sleep(3)
        print(f'{num} convertido para OCTAL é: {oct(num)[2:]}\n\n')
    elif digito == 3:
        print('\nVocê selecionou HEXADECIMAL:\n')
        print('CARREGANDO...\n')
        sleep(3)
        print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}\n\n')
    else:
        print('Por favor, selecione apenas uma das opções de 1 até 3.\n')
        sleep(2)
    while True:
        opc = str(input('Deseja executar novamente? [S]im / [N]ao: ')).upper()
        if opc == 'S':
            sleep(2)
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            break
        else:
            print('Digite apenas (S) para sim / (N) para não.')
            sleep(2)
            limpa_tela()
            continue
    if opc == 'N':
        break





