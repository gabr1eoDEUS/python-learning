#Exercício Python 073: 
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense
campeonato = ('Atlético-MG','Bahia','Botafogo','Bragantino',
'Ceará','Corinthians','Cruzeiro','Flamengo',
'Chapecoense','Fortaleza','Grêmio','Internacional',
'Juventude','Mirassol','Palmeiras','Santos',
'Sport','São Paulo','Vasco','Vitória')
print('Lista de times do Brasileirão:')
print(campeonato)
print('='*125)
print(f'5 primeiros colocados: {campeonato[0:6]}')
print('='*125)
print(f'4 últimos são: {campeonato[-4:]}')
print('='*125)
print('Times em ordem alfabética: ')
print(sorted(campeonato))
print('='*125)
print(f'O Chapecoense está na {campeonato.index('Chapecoense')+1}ª posição')