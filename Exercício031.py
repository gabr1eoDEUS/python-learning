#Exercício Python 031: 
#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 para viagens mais longas.

#Importando bibliotecas
from colorama import Fore, Back, Style
from time import sleep
import os

#Loop
while True:
    #Cabeçalho
    print('='*22)
    print(Fore.GREEN+'  $'+Style.RESET_ALL+'CUSTO POR '+Fore.BLUE+'VIAGEM   '+Style.RESET_ALL)
    print('='*22),print('\n')
    print('   TABELA DE PREÇOS:\nR'+Fore.GREEN+'$'+Style.RESET_ALL+'0,50'' por KM (Até 200Km)\nR'+Fore.GREEN+'$'+Style.RESET_ALL+'0,45 (Viagens mais longas)\n')
    #Limpando a tela
    def limpa_tela():
        os.system('cls')


    #Pegando as informações do user.
    try:
        d_km = float(input('Qual a distância da viagem: '))
        print('\n')
    except ValueError:
        print('Digite apenas números por favor.')
        sleep(2)
        continue
    #Fazendo lógica
    if d_km <= 200:
        print('Você rodou menos ou igual a 200Km.\n')
        print('Seus KM: {}'.format(d_km))
        print('Total: R${}'.format(d_km * 0.50))
    elif  d_km > 200:
        print('Você rodou mais q 200KM.\n')
        print('Seus KM: {}'.format(d_km))
        print('Total: R{}'.format(d_km * 0.45))
    while True:
        opc = str(input('DESEJA EXECUTAR NOVAMENTE? [S]im / [N]ao:')).upper()
        if opc == 'S':
            limpa_tela()
            break
        elif opc == 'N':
            sleep(2)
            limpa_tela()
            break
        else:
            print('Valor inválido. Tente novamente!')
            sleep(2)
            limpa_tela()
    if opc == 'N':
        break
