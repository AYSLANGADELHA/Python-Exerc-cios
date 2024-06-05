'''   
CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA
DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
A - OS 5 PRIMEIROS
B - OS ULTIMOS 4 COLOCADOS 
C - TIMES EM ORDEM ALFABÉTICA
D - EM QUE POSIÇÃO ESTÁ O TIME DA CHAPECOENSE.
'''

times = ('Corithians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')

print('=-'*30)
print(f'LISTA DE TIMES BRASILEIRÃO {times}')
print('=-'*30)

primeiro = (times[:5])
print(f'OS CINCO PRIMEIROS TIMES SÃO:  {primeiro} ') # ITEM A

print('='*100)

ultimos = (times[-4:])
print(f'OS ULTIMOS 4 COLOCADOS SÃO OS TIMES: {ultimos}') # ITEM B

print('='*100)

alfabética = (sorted(times))
print(f'OS TIMES NA ORDEM ALFABÉTICA SÃO: {alfabética}') # ITEM C

print('='*100)

print(f'O CHAPECOENSE ESTÁ NA {times.index('Chapecoense')+1}ª POSIÇÃO') #ITEM D
                                                        #+1 pois o chapecoense está na posição 8
                                                        




