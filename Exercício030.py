#Exercício Python 030: 
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#Importando bibliotecas
from time import sleep
import os
from colorama import Fore, Back, Style

while True:
    def limpa_tela():
        os.system('cls')
    
    
    #Cabeçalho
    print('=' * 14)
    print(Fore.BLUE+'PAR'+Style.RESET_ALL+ ' ou '+Fore.YELLOW+'ÍMPAR'+Style.RESET_ALL)
    print('=' * 14,'\n')

    #Pegando as informações do user
    try:
        num = int(input('Digite um número: '))
        print('\n')
    except ValueError:
        print('Digite apenas números.')
        sleep(3)
        limpa_tela()
        continue

    div = num % 2

    if div == 0:
        print('{} é'.format(num)+Fore.BLUE+' PAR'+Style.RESET_ALL+'\n')
    else:
        print('{} é'.format(num)+Fore.YELLOW+' ÍMPAR'+Style.RESET_ALL+'\n')

    opc = str(input('Deseja executar novamente? [S / N]: '))
    if opc.upper() == 'S':
        sleep(2)
        limpa_tela()
    elif opc.upper() == 'N':
        limpa_tela()
        break
    else:
        limpa_tela()