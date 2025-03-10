#Exercício Python 046: 
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#Importando bibliotecas
from time import sleep
import os
#Limpa tela
def limpa_tela():
    os.system('cls')

#Lógica
for c in range(10,-1,-1):
    #Cabeçalho
    print(' CONTAGEM REGRESSIVA \n')
    print(f'Contador: {c}')
    sleep(1)
    limpa_tela()
print('Feliz ano novo! :)')