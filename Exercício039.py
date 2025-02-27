#Exercício Python 039: 
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
#ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#Importando Bibliotecas
from colorama import Fore,Back,Style
from time import sleep
import os
from datetime import date

#Laço de Repetição
while True:
    #Limpa tela
    def limpando_tela():
        os.system('cls')
    ano_atual = date.today().year

    #Cabeçalho
    print(Fore.GREEN+'======================'+Style.RESET_ALL)
    print('  ALISTAMENTO MILITAR')
    print(Fore.GREEN+'======================'+Style.RESET_ALL+'\n')

    #Tratamento de entrada input
    try:
        nascimento = int(input('Ano de Nascimento: '))
    except ValueError:
        print('Digite apenas números(Inteiros). Por favor!')
        sleep(3)
        limpando_tela()
        continue

    #Condições
    anos = ano_atual-nascimento
    print(f'Quem nasceu em {nascimento} tem {anos} anos em {ano_atual}\n')
    if anos < 18:
        a = 18 -anos
        print(f'Faltam {a} anos para o alistamento')
        print(f'Seu alistameno será em {nascimento+18}\n')
        sleep(3)
    elif anos == 18:
        print(f'Você tem {anos} anos, procure uma junta militar.\n')
        sleep(3)
    elif anos > 18:
        x = nascimento+18
        print(f'Você tem {anos} anos.\nSeu ano de alistamento foi em {nascimento+18}\n')
        print(f'Passou {ano_atual-x} anos. procure uma junta militar.\n')
        sleep(3)
    
    while True:
        opc = str(input('Deseja executar novamente? [S] / [N]:')).upper()
        if opc == 'S':
            sleep(2)
            limpando_tela()
            break
        elif opc == 'N':
            limpando_tela()
            break
        else:
            print('Digite apenas [S] para sim e [N] para não. Por favor!')
            sleep(3)
            limpando_tela()
            continue
    if opc  == 'N':
        break




