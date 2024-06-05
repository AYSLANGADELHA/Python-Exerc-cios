'''
ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER
E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA 
SEQUÊNCIA FIBONNACI.
EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('-'*30)
print('Sequência de FIBONACCI ')
print('-'*30)
n = int(input('Quantos termos você quer mostrar ? '))

t1 = 0 #sequência de fibonacci sempre começa com 0 e 1
t2 = 1 #sequência de fibonacci sempre começa com 0 e 1
print('~'*30)
print('{} -> {}'.format(t1,t2),end='')
cont = 3
while cont <= n:

    t3 = t1 + t2
    print(' -> {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' -> FIM')