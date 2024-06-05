'''
CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999,
QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM
DIGITADOS E QUAL FOI A SOMA ENTRE ELES.
'''

cont = 0
somaValores = 0
núm = 0
while True:
    núm = int(input('Digite um número inteiro (900 para parar):  '))
    if núm == 999:
        break 
    cont = cont + 1
    somaValores = somaValores + núm
print(f'Você digitou {cont} valores e a soma entre eles é de {somaValores} .')
