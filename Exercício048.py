#Exercício Python 048: 
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.

soma = 0

for numero in range(1, 501):
    if numero % 3 == 0:
        soma += numero

print(f'A soma dos múltiplos de 3 no intervalo de 1 a 500 é {soma}')