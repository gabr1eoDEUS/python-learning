#Exercício Python 068: 
#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    escolha_jogador = input('Par ou Ímpar? [P/I]: ').upper()
    
    computador = random.randint(1, 10)
    total = jogador + computador

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} deu ', end='')
    print('PAR' if total % 2 == 0 else 'IMPAR')

    if (total % 2 == 0 and escolha_jogador == 'P') or (total % 2 != 0 and escolha_jogador == 'I'):
        print('Você VENCEU!')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break

    print('Vamos jogar novamente...')

print(f'Você ganhou {vitorias} vezes.')