'''

FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS
EM UMA LISTA. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR
DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.

'''

listanum = []
maior = 0
menor = 0

for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}:  ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('=' * 30)
print(f'Você digitou os valores {listanum} ')
print(f'O maior valor digitado foi {maior} nas posições:  ',end='')

for i, v in enumerate(listanum): # i de indice e v de valor
    if v == maior:
        print(f'{i}...',end= ' ')
print()
print(f'O menor valor digitado foi {menor} nas posições  ', end = '')

for i,v in enumerate(listanum): 
    if v == menor:
        print(f'{i}...  ',end='')






#print(f' O maior número digitado foi {max(lista)}')
#print(f' O menor número digitado foi {min(lista)}') 





