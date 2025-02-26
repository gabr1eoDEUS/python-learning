#Exercício Python 036: 
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Importando bibliotecas
from colorama import Fore, Back, Style
from time import sleep
import os

#Laço de Repetição GERAL
while True:
    
    #Limapndo a tela
    def limpa_tela():
        os.system('cls')
    
    
    #Cabeçalho
    print(Fore.GREEN+'========================'+Style.RESET_ALL)
    print('APROVADOR DE EMPRÉSTIMOS')
    print(Fore.GREEN+'========================'+Style.RESET_ALL)
    print('\n')

    #Filtrando o input
    try:
        #Pegando as informações do user.
        casa = float(input('Qual o valor da casa? R'+Fore.GREEN+'$'+Style.RESET_ALL))
        salario = float(input('Qual o seu salário? R'+Fore.GREEN+'$'+Style.RESET_ALL))
        anos = int(input('Anos para pagar? '))
    except ValueError:
        print('Digite apenas números, por favor!')
        sleep(2)
        limpa_tela()
        continue
    print('\n')

    valor_maximo = salario * 0.30
    prestacoes = anos * 12
    valor_da_prestacao = casa / prestacoes

    if valor_da_prestacao > valor_maximo:
        print(f'Seu salário é de R${salario}, comprando uma casa de R${casa} para pagar em {anos} anos')
        print(f'Sua prestação ficará R${valor_da_prestacao:.2f}. Empréstimo '+Fore.RED+'NEGADO!'+Style.RESET_ALL)
        print('\n')
    else:
        print(f'Seu salário é de R${salario}, comprando uma casa de R${casa} para pagar em {anos} anos')
        print(f'Sua prestação ficará R${valor_da_prestacao:.2f}. Empréstimo '+Fore.GREEN+'ACEITO!'+Style.RESET_ALL)
        print('\n')
    while True:
        opc = str(input('Deseja fazer outra consulta? [S]im / [N]ao: ')).upper()

        if opc == 'S':
            limpa_tela()
            break
        elif opc == 'N':
            limpa_tela()
            sleep(2)
            break
        else:
            print('Digite apenas (S) para sim/ (N) para não. por favor!')
            limpa_tela()
            continue
    if opc == 'N':
        break
