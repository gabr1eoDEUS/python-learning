#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos
m18 = h = m = 0
sexo = opc = ''
while True:
    idade = int(input('Idade: '))
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo [F/M]: ')).upper()
        if sexo == 'M':
            h+=1
    if sexo == 'F' and idade < 20:
        m+=1
    elif idade > 18:
        m18+=1
    while opc != 'S' and opc != 'N':
        opc = str(input('Quer continuar? [S/N]: ')).upper()
        if opc == 'S':
            opc = ''
            sexo = ''
            break
    if opc == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m} mulher(es) com mais de 20 anos.')