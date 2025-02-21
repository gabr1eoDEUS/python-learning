#Exercício Python 024: 
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Nome da cidade: ')).lower()
dv_cidade = cidade.split()


if 'santo' in cidade:
    print('Cidade {} tem SANTO no nome.'.format(cidade))
    if dv_cidade[0] == "santos":
        print('{} começa com SANTO(S).'.format(cidade))
    else:
        print('{} não começa com SANTO(S).'.format(cidade))
    
else:
    print('Cidade {} não tem SANTO no nome.'.format(cidade))