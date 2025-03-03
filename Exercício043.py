#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

#Importando bibliotecas
from colorama import Fore,Back,Style
from time import sleep
import os

#Laço de Repetição principal
while True:
    #Limpa tela
    def limpa_tela():
        os.system('cls')

    #Cabeçalho
    print(Fore.YELLOW+'=========================================='+Style.RESET_ALL)
    print(' Índice de Massa Corporal (IMC Calculator)')
    print(Fore.YELLOW+'=========================================='+Style.RESET_ALL+'\n')
    
    #Filtrando a entrada input
    try:
        peso = float(input('Peso  : '))
        altura = float(input('Altura: '))
    except ValueError:
        print('\nDigite apenas números, por favor!\n')
        sleep(3)
        limpa_tela()
        continue

    #Organização para melhor experiencia
    print('ANALISANDO INFORMAÇÕES: \n'+Fore.BLUE+'AGUARDE!'+Style.RESET_ALL+'\n')
    sleep(3)

    #Condições e lógica
    a_quadrado = altura * altura
    imc = peso / a_quadrado

    if imc < 18.5:
        print(f'\nSeu PESO: {peso}\nSua ALTURA: {altura}m\nSeu IMC é de: {imc:.2f}')
        print('Você está'+Fore.RED+' ABAIXO '+Style.RESET_ALL+ 'do peso.\n')
    elif imc >= 18.5 and imc <= 25:
        print(f'\nSeu PESO: {peso}\nSua ALTURA: {altura}m\nSeu IMC é de: {imc:.2f}')
        print('Você está no peso'+Fore.GREEN+' IDEAL.'+Style.RESET_ALL+'\n')
    elif imc > 25 and imc <= 30:
        print(f'\nSeu PESO: {peso}\nSua ALTURA: {altura}m\nSeu IMC é de: {imc:.2f}')
        print('Você está com'+Fore.YELLOW+' SOBREPESO.'+Style.RESET_ALL+'\n')
    elif imc > 30 and imc <= 40:
        print(f'\nSeu PESO: {peso}\nSua ALTURA: {altura}m\nSeu IMC é de: {imc:.2f}')
        print('Você está com'+Fore.RED+' OBESIDADE.'+Style.RESET_ALL+'\n')
    elif imc > 40:
        print(f'\nSeu PESO: {peso}\nSua ALTURA: {altura}m\nSeu IMC é de: {imc:.2f}')
        print('Você está com'+Fore.RED+' OBESIDADE MÓRBIDA.'+Style.RESET_ALL+'\n')
    
    #Laço de repetição menor
    while True:
        opc = str(input('Deseja executar novamente? [S] or [N]: ')).upper()
        if opc == 'S':
            sleep(2)
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            break
        else:
            print('\nPor favor, digite apenas [S] para sim e [N] para não.')
            sleep(3)
            limpa_tela()
            continue
    if opc == 'N':
        break