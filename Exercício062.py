#Exercício Python 062: 
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

#Pegando as informações do user.
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
#Variáveis
c = 0
termo = 0
i = 1
nx = termo
#Lógica
while c < 10:
    termo = primeiro_termo + c * razao
    raz+=1
    print(f'{termo}', end=' >')
    c+=1
print(' PAUSA\n')
#Pegando as informações do user.
ter = int(input('Quantos termos quer mostrar a mais? '))
x = ter
#Lógica do segundo while
while i <= x:
    n = nx + i * razao
    raz+=1
    print(f'{n}', end=' >')
    i = i + 1
    if i > x:
        print(' PAUSA')
        ter = int(input('Quantos termos quer mostrar a mais? '))
        i = 1
        x = ter
        nx = n
        if ter == 0:
            break
        else:
            continue
print('\nO loop acabou.')
print(f'\nProgressão finalizada com {raz} termos mostrados')