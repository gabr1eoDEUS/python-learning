

n = int(input('Informe um número: '))
print('\nANALISANDO O NÚMERO....\n')
n_str = str(n).zfill(4)  # Completa com zeros 
n_str = n_str

unidade = n_str[3]
dezena = n_str[2]
centena = n_str[1]
milhar = n_str[0]

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))