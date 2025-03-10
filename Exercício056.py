#Exercício Python 056: 
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e 
#quantas mulheres têm menos de 20 anos.

#Importando bibliotecas
from time import sleep
from colorama import Fore,Back,Style
import os

#Variáveis
media = 0
homem_velho = 0
nome_homem_velho = ""
mulher = 0
def limpa_tela():
        os.system('cls')

    #Laço for e lógica
for i in range(4):
        #Cabeçalho
    print('=====================')
    print(Fore.RED+' ANALISADOR COMPLETO'+Style.RESET_ALL)
    print('=====================\n')
        #Pegando as informações dos user's.
    nome = str(input(f"Nome  {i+1}ª: "))
    idade = int(input(f"Idade {i+1}ª: "))
    print('\nF(Feminino) or M(masculino)')
    while True:
        sexo = str(input(f"Sexo  {i+1}ª: ")).upper()
            #Validando entrada input
        if sexo == 'F' or sexo == 'M':
            break
        else:
            print("Sexo inválido. Digite F ou M.")
        #Média de idade do Grupo
    media += idade
        #Verificando homem mais velho
    if idade > homem_velho and sexo  == 'M':
          homem_velho = idade
          nome_homem_velho = nome
    if sexo == 'F' and idade < 20:
          mulher +=1
        #Animação de carregamento
    print('\nArmazenando informações')
    sleep(1)
    limpa_tela()
#Exibindo resultados

print(f'\nA média de idade do grupo é de {media/4} anos.')
print(f'O homen mais velho tem {homem_velho} anos e se chama {nome_homem_velho}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')