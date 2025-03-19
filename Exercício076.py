#Exercício Python 076: 
#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Cabeçalho
print('-'*33)
print('       LISTAGEM DE COMPRAS')
print('-'*33)
lista = ('Lápis                   R$   1.75',
'Borracha                R$   2.00',
'Caderno                 R$  15.90',
'Estojo                  R$  25.00',
'Transferidor            R$   4.20',
'Compasso                R$   9.99',
'Mochila                 R$ 120.32',
'Canetas                 R$  22.30',
'Livro                   R$  34.90')
for cont in range(0,len(lista)):
    print(lista[cont])
print('-'*33)