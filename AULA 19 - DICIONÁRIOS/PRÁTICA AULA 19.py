estado = {} # ou {}
brasil = []

for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))

    brasil.append(estado.copy()) #copy serve para copiar um elemento
#print(brasil)


for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


























'''  # 2º EXEMPLO
brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}

estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[1] ['sigla'])


'''


















'''
pessoas = {'NOME': 'GUSTAVO', 'SEXO': 'M', 'IDADE': 22}

pessoas['PESO'] = 98.5

'''

 # del pessoas['SEXO'] SERVE PARA APAGAR O VALOR (SEXO)
# print(f'O {pessoas['NOME']} tem {pessoas ['IDADE']} anos')

# print(pessoas.items())


'''
for k,v in pessoas.items():         #VARRER A VARIÁVEL
    print(f' {k} = {v}')
'''
