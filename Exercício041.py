#Exercício Python 041:
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
#e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

#Importando Bibliotecas
import os
from colorama import Fore,Back,Style
from time import sleep
from datetime import date

#Laço de Repetição
while True:
    #Variáveis usaveis
    ano_atual = date.today().year

    #Limpador de logs
    def limpador():
        os.system('cls')

    #Cabeçalho
    print('='*32)
    print('CONFEDERAÇÃO'+Fore.GREEN+' NACIONAL '+Style.RESET_ALL+'DE '+Fore.BLUE+'NATAÇÃO'+Style.RESET_ALL)
    print('='*32,'\n')
    print(Fore.CYAN+'   ANALISADOR de CATEGORIA\n'+Style.RESET_ALL)
    #Filtrando entrada input
    try:
        nascimento = int(input('Ano de Nascimento: '))
    except ValueError:
        print('\nDigite apenas números(Inteiros), Por favor.')
        sleep(3)
        limpador()
        continue
    #Convertendo um número para str
    nascimento_str = str(nascimento)
    #Verificando se tem 4 digitos ou são maior q 4 digitos e se os valores são positivos
    if len(nascimento_str) < 4 or len(nascimento_str) > 4 or nascimento < 0:
        print('\nDigite apenas valores positivos.')
        print(f'\n4 digitos para o [Ano de nascimento] EX: {ano_atual}')
        sleep(5)
        limpador()
        continue
    #Verificando a idade atual
    idade = ano_atual - nascimento
    
    #Condições
    if idade <= 9:
        print(f'Idade: {idade} anos\nCATEGORIA: MIRIM\n')
    elif idade > 9 and idade <= 14:
        print(f'Idade: {idade} anos\nCATEGORIA: INFANTIL\n')
    elif idade > 14 and idade <= 19:
        print(f'Idade: {idade} anos\nCATEGORIA: JÚNIOR\n')
    elif idade > 19 and idade <= 25:
        print(f'Idade: {idade} anos\nCATEGORIA: SÊNIOR\n')
    elif idade > 25:
        print(f'Idade: {idade} anos\nCATEGORIA: MASTER\n')
    #Laço de Repetição menor
    while True:
        opc = str(input('Deseja executar novamente? [S] / [N]: ')).upper()
        if opc == 'S':
            sleep(2)
            limpador()
            break
        elif opc == 'N':
            limpador()
            break
        else:
            print('Valor digitado inválido.\nPor favor, digite apenas [S] para sim ou [N] para não.\n')
            sleep(4)
            limpador()
            continue
    if opc == 'N':
        break