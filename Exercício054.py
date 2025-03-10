#Exercício Python 054: 
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior = 0
menor = 0

for i in range(0,7):
    pessoas = int(input(f'Em que ano nasceu a {i+1}ª pessoa? '))
    x = 2017 - pessoas
    if x >= 18:
        maior = maior + 1
    elif x < 18:
        menor = menor + 1
print(f'\nAo todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')
