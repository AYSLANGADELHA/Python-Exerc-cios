''' parecido com um exercicio anterior (30 e pouco)

Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar
um triângulo.

para formar um triângulo, a soma de dois lados
devem ser menor ou igual ao terceiro lado

- equilatero: todos os lados iguaais
- isoceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

r1 = float(input('Comprimento da primeira reta : '))
r2 = float(input('Comprimento da segunda reta : '))
r3 = float(input('Comprimento da terceira reta : '))

if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo')

    #equilatero

    if r1== r2 == r3:


        print('A soma de todos os lados iguais formam um triângulo EQUILATERO')

    #isocele

    elif r1==r2 or r1==r3:

        print('A soma de apenas dois lados iguais formam um triângulo ISOCELES')

    #escaleno

    elif r1!=r2 and r2!=r3 and r3!=r1:
        print('A soma de todos os lados diferentes formam um triângulo ESCALENO')
else:
    print('Não podem formar um triângulo')