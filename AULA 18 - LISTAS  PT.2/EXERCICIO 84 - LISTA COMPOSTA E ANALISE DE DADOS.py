'''

FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS
GUARDANDO TUDO EM UMA LISTA. NO FINAL MOSTRE:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.

'''
#forma que tentei resolver e não consegui
'''
peso = []
pessoa = []
quantidade_pessoas = 0
while True:
    pessoa.append(str(input('NOME: ')))
    peso.append(int(input('IDADE: ')))
    resp = str(input('Quer continuar ? [S/N]'))

    for p in pessoa:
        quantidade_pessoas = quantidade_pessoas + 1
    

    if resp in 'Nn':
        break

print('=-='*30)
print('ANÁLISE ENCERRADA')

print(f'Foram cadastradas {quantidade_pessoas} pessoas.')

'''

# GUANABARA ENSINANDO

temporária = [] #lista temporária
principal = []  #lista principal

maior_peso = 0
menor_peso = 0
while True:
    temporária.append(str(input('NOME: '))) # adicionar na lista temporária o nome de uma pessoa
    temporária.append(float(input('PESO: '))) # adicionar na lista temporária a idade da pessoa
    if len(principal) == 0:
        maior_peso = menor_peso = temporária[1] 
    else:
        if temporária[1] > maior_peso: # se indice 1 da lista temporária for maior que maior peso, maior peso será temporaria i1
            maior_peso = temporária[1]
        if temporária[1] < menor_peso: # se i1 da lista temporária for menor que o menor peso, menor peso serpa temporária i1
                                        #i1 = indice 1            
            menor_peso = temporária[1]



    principal.append(temporária[:]) # para fazer uma cópia da lista temporária na principal(fica uma lista dentro de outra lista)
    temporária.clear() # para apagar a lista temporaria




    resp = str(input('Quer continuar ? [S/N]'))
    if resp in 'Nn':
        break

print('=-'*30)
print(f'Os dados foram {principal}')
print(f'Ao todo, você cadastrou {len(principal)} pessoas. ') #resolução item A)
print(f'O maior peso registrado é {maior_peso}Kg. Peso de ', end = '') #resolução item B)


for p in principal:
    if p[1] == maior_peso:
        print(f'[{p[0]}], ', end = '') # nome da pessoa com maior peso

print() 
print(f'O menor peso registrado é {menor_peso}Kg. Peso de ', end = '')
for p in principal:
    if p[1] == menor_peso:
        print(f'[{p[0]}], ', end='') # nome da pessoa com menor peso


''' RESOLUÇÃO DOS ITENS B E C EM FORMA DE KG

print(f'O maior peso registrado é {maior_peso}Kg') #resolução item B) em kg
print(f'O menor peso registrado é {menor_peso}Kg') #resolução item C) em kg

'''
