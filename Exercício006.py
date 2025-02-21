#Exercício Python 006: 
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Importand biblioteca
import math

#Pegando as informações do user.
num = int(input('Digite um número: '))
print('\n')

#Calculos v1
dobro = num * 2
triplo = num * 3
#Raiz Quadrada com a biblioteca
raiz = math.sqrt(num)
#Raiz Quadrada sem a biblioteca
'raiz = n ** (1/2)'

print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}\n'.format(dobro,triplo,raiz))