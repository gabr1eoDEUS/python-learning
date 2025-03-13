#Exercício Python 067: 
#Faça um programa que mostre a tabuada de vários números, um de cada vez, 
#para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo. 

n = t = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for var in range(0,10):
        var +=1
        print(f'{n} x {var} = {n * var}')

print('O valor digitado é negativo, programa encerrado.')