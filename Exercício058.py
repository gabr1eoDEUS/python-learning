#Exercício Python 058: 
#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, 
#mostrando no final quantos palpites foram necessários para vencer.

import random

maquina = random.randint(0,10)
user = 0
palpites = 0

while user != maquina:
        #Cabeçalho
    print('===========================')
    print('=== JOGO da ADIVINHAÇÃO ===')
    print('===========================')
    print('\n')
        #Pegando as informações do user
    user = int(input('Digite um número: '))
        #Lógica
    if user == maquina:
        print(f'\nUser : {user}')
        print(f'Máquina: {maquina}')
    elif user > maquina:
        palpites +=1
        print(f'\nUser : {user}')
        print(f'\nQuase lá, tente um número mais baixo ;)\n')
    else:
        palpites +=1
        print(f'\nUser : {user}')
        print(f'\nQuase lá, tente um número mais alto ;)\n')

print(f'Parabéns, você GANHOU!\nForam precisos {palpites} palpite(s) para ganhar.')

