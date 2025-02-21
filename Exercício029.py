#Exercício Python 029: 
#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

while True:
    #Importando bibliotecas
    from colorama import Fore, Back, Style
    from time import sleep
    import os

    #Limpando a tela
    def limpa_tela():
        os.system('cls')

    #Cabeçalho
    print('Multimetro v1\n')

    #Pegando as informações do user.
    km = float(input('Velocidade KM: '))

    #Deixando mais legal :)
    print('\nObtendo informações...')
    print('Aguarde, porfavor!\n')
    sleep(3)
    print('Resultado da pesquisa:\n')
    #Lógica
    if km > 80:
        print('VOCÊ foi'+Fore.RED+' multado '+Style.RESET_ALL+'por excesso de velocidade!\n')
        print('Sua multa é de R'+Fore.GREEN+'$'+Style.RESET_ALL+'{} Reais'.format((km-80)*7))
    else:
        print('VOCÊ está no limite de velocidade '+Fore.GREEN+'PERMITIDA!'+Style.RESET_ALL)

    back_ = str(input('Deseja executar uma nova consulta? [Y]es or [N]o:'))
    if back_.upper() != 'Y':
        break
    else:
        limpa_tela()