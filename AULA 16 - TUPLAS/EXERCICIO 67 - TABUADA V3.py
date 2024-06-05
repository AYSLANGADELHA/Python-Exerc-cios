'''
FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR
DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR
NEGATIVO'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO')