#Exercício Python 064: 
#Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


soma = 0
a = 0
n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n < 999:
        a+=1
        soma = soma + n
        print(soma)
    
    
print(f'A quantidade de números digitados foi de {a} números.')
print(f'A soma entres esse números foi de {soma}.')