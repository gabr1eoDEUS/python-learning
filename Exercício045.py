#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

#Importando bibliotecas
import random
import os
from time import sleep

#Laço de repetição maior
while True:
    def limpa_tela():
        os.system('cls')
    #Cabeçalho
    print('  JOKENPÔ')
    print('Suas opções: ')
    print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')


    #Randomizando a jogada
    #jokenpo = ['PEDRA','PAPEL','TESOURA']
    maquina = random.randint(0,2)

    #Pegando as informações do user
    try:
        jogada = int(input('Escolha: '))
    except ValueError:
        print('\nDigite apenas números por favor.')
        sleep(3)
        continue
    if jogada > 2 or jogada < 0:
        print('Apenas jogadas entre 0 e 2, por favor!')
        sleep(2)
        limpa_tela()
        continue
    #Animação
    print('JO'),sleep(1)
    print('KEN'),sleep(1)
    print('PÔ\n'),sleep(1)
    if jogada == maquina:
        print('\nSua jogada: PEDRA\nJogada da Máquina: PEDRA')
        print('EMPATOU!\n')
    elif jogada == 0:
        if maquina == 1:
            print('\nSua jogada: PEDRA')
            print('Jogada da Máquina: PAPEL\nMáquina venceu!\n')
        else:
            print('\nSua jogada: PEDRA')
            print('Jogada da Maquina: TESOURA\nVocê venceu!\n')
    if jogada == 1 and jogada == maquina:
        print('\nSua jogada: PAPEL\nJogada da Máquina: PAPEL')
        print('EMPATOU!\n')
    elif jogada == 1:
        if maquina == 0:
            print('\nSua jogada: PAPEL')
            print('Jogada da Máquina: PEDRA\nVocê venceu!\n')
        else:
            print('\nSua jogada: PAPEL')
            print('Jogada da Maquina: TESOURA\nMáquina venceu!\n')
    if jogada == 2 and jogada == maquina:
        print('\nSua jogada: TESOURA\nJogada da Máquina: TESOURA')
        print('EMPATOU!\n')
    elif jogada == 2:
        if maquina == 1:
            print('\nSua jogada: TESOURA')
            print('Jogada da Máquina: PAPEL\nVocê venceu!\n')
        else:
            print('\nSua jogada: TESOURA')
            print('Jogada da Maquina: PEDRA\nMáquina venceu!\n')

    while True:
        opc = str(input('Deseja executar novamente? [S] para sim / [N] para não: ')).upper()
        if opc == 'S':
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            
        else:
            print('Valor digitado inválido.')
            sleep(3)
            continue
    if opc == 'N':
        break