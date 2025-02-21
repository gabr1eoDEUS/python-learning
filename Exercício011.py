#Exercício Python 011: 
#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Importando a biblioteca
import math

#Pegando as informações do user.
lp = float(input('Largura da Parede: '))
ap = float(input('Altura da Parede: '))
print('\n')

#Verificando a largura e altura da parede.
lpap = lp * ap

#Verificando quanto de tinta será necessária.
litros = lpap / 2

#Exibindo os resultados na tela.
print('Largura da Parede: {}m\nAltura da Parede: {}m\nSua parede tem uma área de: {}m²\nTintia necessária em litros: {:.2f}m² litros\n'.format(lp,ap,lpap,litros))