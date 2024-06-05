'''
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS.
O PORGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR.
MOSTRE TAMBÉM:
- QUAL É O TOTAL DE GASTO NA COMPRA
- QUANTOS PRODUTOS CUSTAM MAIS DE 1000 REAIS
- QUAL É O NOME DO PRODUTO MAIS BARATO

'''

print('-' * 60 )
print('                 MERCADINHO DO AYSLAN                '               )
print('-' * 60)
total = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Qual o nome do produto: '))
    preço = float(input('Quanto custa o produto: R$ '))
    cont = cont + 1
    total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not  in 'SN':
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))

print(f'O total da compra foi {total}')

print(f'Temos {totmil} produtos custando acima de R$ 1000 ')

print(f'O produto mais barato foi {barato} e custa R$ {menor:.2f} ')
       
















print('Acabou')
