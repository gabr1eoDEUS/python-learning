#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
#Pegando as informações do user.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor : '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Último valor  : '))
#Adicionando as variáveis a TUPLA.
x = (n1,n2,n3,n4)
nove = 0
print(f"Você digitou os valores {x}")
for i in x:
    if i == 9:
        nove+=1
print(f'O valor 9 apareceu {nove} vez(es)')
if 3 in x:
    print(f"O valor 3 apareceu na {x.index(3)+1}ª posição")
else:
    print(f"O valor 3 não foi digitado em nenhuma posição.")
pares = []
for n in x:
    if n % 2 == 0:
        pares.append(n)
print(f"Os valores pares digitados foram {pares}")