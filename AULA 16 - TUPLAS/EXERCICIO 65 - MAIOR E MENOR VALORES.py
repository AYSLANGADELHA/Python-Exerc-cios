'''
CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES
E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO
SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
'''
resp = 'S'
soma = 0
quantValores = 0
média = 0
maior = 0
menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma = soma + núm
    quantValores = quantValores + 1
    if quantValores == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    

    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
média = soma/quantValores
print('Você digitou {} números e a média foi {} '.format(quantValores, média))
print('O maior número foi {} e o menor número foi {}'.format(maior,menor))



