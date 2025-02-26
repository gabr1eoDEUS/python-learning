#Exercício Python 034:
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. 
#Para os inferiores ou iguais, o aumento é de 15%.

#Importando bibliotecas
from colorama import Fore, Back, Style
from time import sleep
import os

#Laço de Repetição
while True:
    #Cabeçalho
    print('='*32)
    print('Calculadora de Aumento'+Fore.GREEN+' Salárial'+Style.RESET_ALL)
    print('='*32)
    print('\n')

    #Função para limpar o console
    def limpa_tela():
        os.system('cls')

    #Usando try e except para filtrar erros de digitação no console.
    try:
        #Pegando as informações do user.
        salario = float(input('Salário atual: R'+Fore.GREEN+'$'+Style.RESET_ALL))
    except ValueError:
        print('Digite apenas números válidos, por favor.')
        sleep(2)
        limpa_tela()
        continue
    print('\n')
    #Condições e lógica
    if salario > 1250.00:
        #aumento10 = (salario*0.10)
        print('Seu salário era de R${}\ncom aumento de 10%, seu novo salário é de R${}'.format(salario,(salario*0.10)+salario))
        print('\n')
    elif salario <= 1250.00:
        #aumento15 = (salario*0.15)
        print('Seu salário era de R${}\ncom aumento de 15%, seu novo salário é de R${}'.format(salario,(salario*0.15)+salario))
        print('\n')
    #Laço de repetição do programa
    while True:
        opc = str(input('DESEJA EXECUTAR NOVAMENTE? [ S / N]: ')).upper()
        if opc == 'S':
            sleep(2)
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            break
        else:
            print('O valor digitado é invalido. tente novamente!')
            limpa_tela()
            continue
    if opc == 'N':
        break