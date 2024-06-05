''' 
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER
E MOSTRE O SEU FATORIAL
'''

#-> USANDO O MÓDULO 
# from math import factorial 
# n = int(input('Digite qual número você quer fatorar: '))
# f = factorial(n)

# print('O fatorial de {} é {} .'.format(n,f))
#-> USANDO O MÓDULO

#MATEMÁTICAMENTE

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1 #fator nulo de multiplicação é 1
print('Calculand {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1

print('{}'.format(f))



