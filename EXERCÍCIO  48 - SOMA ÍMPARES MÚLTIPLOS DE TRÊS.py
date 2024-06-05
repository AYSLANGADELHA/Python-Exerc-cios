'''
FAÇA UM PROGRAMA QUE LEIA A SOMA ENTRE TODOS OS NÚMEROS
IMPARES QUE SÃO MULTIPLOS DE TRÊS E QUE SE ENCONTRAM NO
INTERVALO DE 1 ATÉ 500.
'''
soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        soma += c

        # toda vez que achar um número divisivel por 0
        # ele vai contar +1 (cont += 1)
        cont += 1


print('A soma de todos os {}  valores solicitados é {}'.format(cont,soma))
