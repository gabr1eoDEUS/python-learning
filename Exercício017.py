#Exercício Python 017: Faça um programa que leia o 
#comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.

#Importando bibliotecas
import math

#Pegando as informações do user.
co = float(input('Cateto oposto: '))
ca = float(input('Cateto Adjacente: '))
print('\n')

#Calculando os valores
hipotenusa = math.hypot(co,ca)

#Exibindo os valores na tela.
print('Sua Hipotenusa é de: {:.2f}'.format(hipotenusa))