#Exercício Python 072: 
#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
#de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
from num2words import num2words

num = int(input('Digite um número entre 0 e 20: '))
#n = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,78,19,20)
while num > 20 or num < 0:
    num = int(input('Tente novamente. Digite um número entre0 e 20: '))
extenso = num2words(num, lang='pt_BR')
print(f'Você digitou o número {extenso}')