#Exercício Python 028: 
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#Importando biblioteca(s)
import random
from time import sleep
from colorama import Fore, Back, Style

#Loop
while True:
    #Cabeçalho
    print('===========================')
    print('=== JOGO da ADIVINHAÇÃO ===')
    print('===========================')
    print('\n')

    #Pegando as informações do user
    print('Tente adivinhar o número em q pensei(entre 0 e 5).\n')

    num = int(input('Digite um número entre 0 e 5:'))

    #Gerando número aleatorio
    n_aleatorio = random.randrange(0, 5)

    #Deixando mais intuitivo
    print(Fore.BLUE +'PROCESSANDO...\n'+Style.RESET_ALL)
    sleep(3)

    #Condições
    if num == n_aleatorio:
        print('Número digitado: {}'.format(num))
        print('Número GERADO: {}'.format(n_aleatorio))
        print(Fore.GREEN + 'PARABENS!' + Style.RESET_ALL)
    elif num > 5:
        print('O número digitado é maior q 5.\nTente novamente!')
    else:
        print('Número digitado: {}'.format(num))
        print('Número GERADO: {}'.format(n_aleatorio))
        print(Fore.RED +'ERROU!'+Style.RESET_ALL)
    jogar_novamente = str(input("Deseja jogar novamente? [S / N]:"))
    if jogar_novamente.upper() != 'S':
        break
