#Exercício Python 055: 
#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso= 0

for i in range(5):
    peso = float(input(f'Peso da {i+1}ª: '))

    if i == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso   
        
print(f'O maior peso lido foi de {maior_peso}')
print(f'O menor peso lido foi de {menor_peso}')