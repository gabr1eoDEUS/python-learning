#Exercício Python 013: 
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#Importando bibliotecas
import math

#Cabeçalho
print('AUMENTO SALARIAL\n')

#Pegando as informações do user.
salario = float(input('Salário atual: R$'))
aumento = float(input('Porcentagem de aumento: %'))
print('\n')

#Cálculo do percentual de aumento salarial 
novosalario = salario + (salario*aumento/100)

#Exibindo resultados na tela.
print('Seu antigo salário era de: R${}\ncom aumento de %{}\nSeu novo salário é de: R${:.2f}'.format(salario,aumento,novosalario))