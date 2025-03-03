#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, 
#acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

#Importando bibliotecas
from colorama import Fore,Back,Style
from time import sleep
import os

#Laço de Repetição
while True:

    #Limpando a tela
    def limpa_tela():
        os.system('cls')
    
    #Cabeçalho
    print(Fore.CYAN+'==============================='+Style.RESET_ALL)
    print('  ANALISADOR de TRIÂNGULOS v2')
    print(Fore.CYAN+'==============================='+Style.RESET_ALL+'\n')


    #Filtragem de entrada 
    try:
        #Pegando as informações do user.
        a = float(input('Comprimento 1: '))
        b = float(input('Comprimento 2: '))
        c = float(input('Comprimento 3: '))
    except ValueError:
        print('Por favor, digite apenas números válidos.\n')
        sleep(3)
        limpa_tela()
        continue

    #Condições
     # Verifica se é possível formar um triângulo
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print(f'com comprimentos de {a} , {b} e {c}. pode se formar um triângulo ' + Fore.BLUE + 'EQUILÁTERO.' + Style.RESET_ALL)
        elif a == b or a == c or b == c:
            print(f'com comprimentos de {a} , {b} e {c}. pode se formar um triângulo ' + Fore.BLUE + 'ISÓSCELES.' + Style.RESET_ALL)
        else:
            print(f'com comprimentos de {a} , {b} e {c}. pode se formar um triângulo ' + Fore.BLUE + 'ESCALENO.' + Style.RESET_ALL)
    else:
        print(f'com comprimentos de {a} , {b} e {c}. '+Fore.RED+'NÃO'+Style.RESET_ALL+' pode se formar um triângulo.')

    #Laço de Repetição menor
    while True:
        opc =str(input('Deseja executar novamente? [S] or [N]: ')).upper()
        if opc == 'S':
            sleep(3)
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            break
        else:
            print('\nPor favor, digite apenas [S] para SIM ou [N] para NÃO.')
            sleep(3)
            limpa_tela()
            continue
    if opc == 'N':
        break