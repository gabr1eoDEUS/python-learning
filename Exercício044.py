#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

#Importando bibliotecas
from colorama import Fore,Back,Style
from time import sleep
import os
import emoji

#Laço de Repetição principal
while True:
    
    #Limpa tela
    def limpa_tela():
        os.system('cls')
    
    #Cabeçalho
    print(Fore.BLUE+'========================'+Style.RESET_ALL)
    print("🛒 SUPERMERCADO SILVA 🛒 ")
    print(Fore.BLUE+'========================'+Style.RESET_ALL+'\n')
    
    #Filtrando entrada input
    try:
        produto = float(input('Preço do produto: R'+Fore.GREEN+'$'+Style.RESET_ALL))
    except ValueError:
        print('\nDigite apenas números válidos, por favor!')
        sleep(3)
        limpa_tela()
        continue
    #Escolhendo a forma de pagamento:
    print('\nForma de pagamento: \n')
    print('À VISTA/CHEQUE       Selecione:[ 1 ]     OBS: 10%'' de desconto.')
    print('À VISTA NO CARTÃO    Selecione:[ 2 ]     OBS:  5%'' de desconto.')
    print('2x NO CARTÃO         Selecione:[ 3 ]     OBS:  Preço formal.')
    print('3x OU MAIS NO CARTÃO Selecione:[ 4 ]     OBS: 20%'' de Juros.')
    print('VER TODAS AS OPÇÕES  Selecione:[ 5 ]')
    
    #Escolha do user
    while True:
        #Filtrando escolha do user
        try:
            escolha = int(input('\nSelecione sua opção: '))
        except ValueError:
            print('Digite apenas números válidos, porfavor.')
            continue
        #Verificando se a escolha está dentro do intervalo entre 1 e 5
        if escolha > 0 and escolha <= 5:
            break
        else:
            print('Digite apenas valores entre 1 e 5, por favor')
            continue
        
    #Condições e lógica
    if escolha == 1:
        desconto10 = (produto*0.10)
        print(f'\nVocê selecionou À VISTA/CHEQUE:\nValor do produto: R${produto}\nValor do produto com desconto de 10%: R${produto - desconto10}')
    elif escolha == 2:
        desconto5 = (produto*0.05)
        print(f'\nVocê selecionou À VISTA NO CARTÃO:\nValor do produto: R${produto}\nValor do produto com desconto de 5%%: R${produto - desconto5}')
    elif escolha == 3:
        duasvezes = produto/2
        print(f'\nVocê selecionou 2X no CARTÃO (OBS: Preço formal):\nValor do produto: R${produto}\nValor do produto em 2x (2 parcelas de {duasvezes}) no cartão: R${produto}')
    elif escolha == 4:
        while True:
            #Filtrando a entrada input
            print('OBS: parcelamento acima de 2x, por favor.')
            try:
                dividir = int(input('\nQuantas vezes deseja dividir? '))
            except ValueError:
                print('Digite apenas números válidos por favor. entre 3x e 12x no parcelamento.')
                sleep(3)
                continue
            if dividir > 2 and dividir <=12:
                valor_juros = produto * 0.20
                juros = produto + valor_juros
                print(f'\nVocê selecionou 3x ou mais no cartão: 20% de juros:\nValor do produto: R${produto}\nDivido em {dividir}x, suas parcelas são de R${juros/dividir} cada parcela, totalizando um valor de R${produto+valor_juros}')
                break
            else:
                print('Por favor, selecione uma opção válida e entre 3x a 12x no parcelamento.')
                sleep(3)
                continue
    elif escolha == 5:
        desconto10 = (produto*0.10)
        desconto5 = (produto*0.05)
        duasvezes = produto/2
        print('\nVocê selecionou VER TODAS AS OPÇÕES\n')
        print(f'\nÀ VISTA/CHEQUE:\nValor do produto: R${produto}\nValor do produto com desconto de 10%: R${produto - desconto10}')
        print(f'\nÀ VISTA NO CARTÃO:\nValor do produto: R${produto}\nValor do produto com desconto de 5%%: R${produto - desconto5}\n')
        print(f'\n2X no CARTÃO (OBS: Preço formal):\nValor do produto: R${produto}\nValor do produto em 2x (2 parcelas de {duasvezes}) no cartão: R${produto}')
        dividir = int(input('\nQuantas vezes deseja dividir? '))
        if dividir <= 12:
            valor_juros = produto * 0.20
            juros = produto + valor_juros
            print(f'\n3x ou mais no cartão: 20% de juros:\nValor do produto: R${produto}\nDivido em {dividir}x, suas parcelas são de R${juros/dividir} cada parcela, totalizando um valor de R${produto+valor_juros}')
    else:
        print('Por favor, selecione uma opção válida.')
        sleep(3)
        limpa_tela()
        continue

    while True:
        opc = str(input('\nDeseja executar novamente? [S] or [N]:')).upper()
        if opc == 'S':
            limpa_tela()
            break
        if opc == 'N':
            limpa_tela()
            break
        else:
            print('\nSelecione uma opção válida, [S] para sim ou [N] para não.')
            continue
    if opc == 'N':
        break   