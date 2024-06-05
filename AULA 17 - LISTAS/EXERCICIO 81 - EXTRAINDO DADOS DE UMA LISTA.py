'''

CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
DEPOIS DISSO, MOSTRE:

A) QUANTOS NÚMERO FORAM DIGITADOS
B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA






'''


valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    
    
    
    
    if resp in 'Nn':
        break

valores.sort(reverse = True) # B) ordem decrescente

print()

print(f' A ordem dos números digitados em ordem decrescente é {valores}') 
print(f' Foram digitados  {len(valores)} elementos ') #A) quantos elementos/números foram digitados

if 5 in valores:
    print(' O valor 5 faz parte da lista !')
else:
    print(' O valor 5 não foi encontrado na lista')
