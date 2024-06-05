'''

CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS,
GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS
EM UMA LISTA. NO FINAL MOSTRE:

A) QUANTAS PESSOAS CADASTRADAS
B) A MÉDIA DE IDADE
C) UMA LISTA COM MULHERES
D) UMA LISTA COM IDADE ACIMA DA MÉDIA


'''




''' # tentativa feita por conta própria
dados = {}
cópia = []
contador = 0

while True:

    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo M/F: '))
    dados['idade'] = int(input('Idade: '))
    resp = str(input('Quer continuar ? S/N: '))
    contador = contador + 1

    if resp in 'Nn':
        break


print(dados)
dados['média'] = cópia[:]
dados['média1'] = (dados['idade']) / 2                              #jogador['gols'] = partida[:]

print(f'A quantidade de pessoas cadastradas foram {contador} pessoas !')

print(dados['média'])
'''






# resolução guanabara

galera = []
pessoa = {}
cont = 0
soma = 0
média = 0
while True:
    pessoa.clear() #para apagar a ultima pessoa cadastrada
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digita apena M ou F ')

    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade'] # somar todas as idades cadastradas
    cont = cont + 1
    galera.append(pessoa.copy()) # para fazer a cópia da pessoa cadastrada na variável galera(lista)

    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break




print('-=' * 30)
# item A
print(f'Ao todo temos {cont} pessoas cadastradas ')

# item B
média = soma/cont 
print(f'A média de idade é de {média:.1f} anos')

# item C
print('As mulheres cadastradas foram ', end= '')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']}, ', end = '')
print()

# item D
for i in galera:
    if i['idade'] > média:
        print(f'As idades acima da média foram: {i}')

















