#Exercício Python 033: 
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Pegando as informações do user.
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor : '))
n3 = float(input('Terceiro valor: '))

#Condições
if n1 > n2 and n1 > n3:
    print('O maior valor digitado foi {}'.format(n1))
    if n2 < n3:
        print('O menor valor digitado foi {}'.format(n2))
    else:
        print('O menor valor digitado foi {}'.format(n3))
elif n2 > n1 and n2 > n3:
    print('O maior valor digitado foi {}'.format(n2))
    if n1 < n3:
        print('O menor valor digitado foi {}'.format(n1))
    else:
        print('O menor valor digitado foi {}'.format(n3))
elif n3 > n2 and n3 > n1:
    print('O maior valor digitado foi {}'.format(n3))
    if n2 < n1:
        print('O menor valor digitado foi {}'.format(n2))
    else:
        print('O menor valor digitado foi {}'.format(n1))
