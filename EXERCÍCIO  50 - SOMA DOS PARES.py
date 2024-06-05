'''
DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS
E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
SE O VALOR DIGITADO FOR ÍMPAR.
DESCONSIDERE
'''
soma = 0
cont = 0


for c in range (0,6+1):
    if c % 2 == 0:
        soma = soma + c
        cont = cont + 1
print('Existem {} números pares e a soma de todos os números é {} . '.format(cont, soma))













