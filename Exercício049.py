#Exercício Python 049: 
#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#Cabeçalho
print('Tabuada v2 (FOR)\n')
#Pegando as informações do user
num = int(input('Digite um número: '))

for var in range(0,10):
    var += 1
    print(f'{num} x {var} = {num*var}')