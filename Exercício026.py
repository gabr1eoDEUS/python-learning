#Exercício Python 026: 
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

#Pegando as informações do user.
frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))
