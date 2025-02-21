#Exercício Python 027: 
#Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente.

#Pegando as informações do user.
nome = str(input('Digite seu nome: ')).upper().strip()
nome_separada = nome.split()

#Fazendo lógica
print('Seu nome completo é: {}'.format(nome))
print('Primeiro nome: {}'.format(nome_separada[0]))
print('Último nome: {}'.format(nome_separada[-1]))