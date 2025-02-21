#Exercício Python 012: 
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Importando a biblioteca
import math

#Cabeçalho
print('CALCULADORA DE DESCONTOS\n')

#Preço do produto sem o desconto
print('Preço do produto sem o desconto.')
#Pegando as informações do user.
produto = float(input('Informe o preço do produto R$'))
desconto = float(input('Informe de quanto é o desconto: %'))
print('\n')

#Lógica de calculos
descontando = produto - (produto * desconto/100)
#des = produto - descontando


#Exibindo os resultados na tela.
print('PRODUTO SEM O DESCONTO: \nPRODUTO:R${}\nPRODUTO COM DESCONTO: \nDESCONTO DE %{}\nVALOR COM DESCONTO APLICADO:R${:.2f}\n'.format(produto,desconto,descontando))