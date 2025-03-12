#xercício Python 057: 
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Cabeçalho validação de dados
print(' VALIDAÇÃO DE DADOS\n')
n = 0
while n != 1:
    sexo = str(input('Sexo: ')).upper()
    if sexo == 'M' or sexo == 'F':
        n = 1
    else:
        print('\nApenas F ou M, por favor.')

print('\nSaiu do loop')