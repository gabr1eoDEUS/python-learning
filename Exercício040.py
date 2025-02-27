#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

#Importando  bibliotecas
from colorama import Fore,Back,Style
from time import sleep
import os

#Laço de Repetiçao
while True:
    
    #Limpador de Tela
    def limpa_tela():
        os.system('cls')
    

    #Cabeçalho
    print(Fore.LIGHTBLUE_EX+'=================='+Style.RESET_ALL)
    print(' CALCULANDO MÉDIA')
    print(Fore.LIGHTBLUE_EX+'=================='+Style.RESET_ALL+'\n')

    #Tratamento de entrada input 
    try:
        #Pegando as informações do user.
        nota1 = float(input('Primeira Nota: '))
        nota2 = float(input('Segunda Nota : '))
    except ValueError:
        print('Digite apenas números(Inteiros) válidos, por favor.')
        sleep(3)
        limpa_tela()
        continue
    #Caso o aluno digite uma nota maior q 10
    if nota1 and nota2 >= 11:
        print('\nDigite apenas notas menores ou igual 10.')
        sleep(3)
        limpa_tela()
        continue
    media = (nota1+nota2) / 2
    #Condições
    if media >= 7.0:
        print(f'Sua média foi de {media:.1f}\nParabéns, você foi '+Fore.GREEN+'APROVADO'+Style.RESET_ALL+'\n')
    elif media >= 5.0 and media <= 6.9:
        print(f'Sua média foi de {media:.1f}\nVocê ficou de '+Fore.YELLOW+'RECUPERAÇÃO'+Style.RESET_ALL+'\n')
    elif media < 5.0:
        print(f'Sua média foi de {media:.1f}\nVocê foi '+Fore.RED+'REPROVADO'+Style.RESET_ALL+'\n')
    
    #Laço de Repetição menor
    while True:
        opc = str(input('Deseja executar novamente? [S] / [N]: ')).upper()
        if opc == 'S':
            sleep(3)
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            break
        else:
            print('\nDigite apenas [S] para sim ou [N] para não. por favor!')
            sleep(3)
            limpa_tela()
    if opc == 'N':
        break