# tupla num = (2, 5, 9, 1) 
'''
num = [2, 5, 9, 1]
num[2] = 3  #trocar o elemento 2 pelo valor 3

num.append(7) # acrescentar um novo valor a lista
num.sort(reverse = True)
 # reverter as ordens dos elementos e o sort para organiza-los

num.insert(2, 2) # inserir na posição/elemento 2 o valor 2

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
# num.remove(2) # remover o numero 2 primeiro da lista

print(num)
comprimento = len(num) 
print(f'Essa lista tem {comprimento} elementos')

'''
# COMEÇA AQUI
'''
valores = []  

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
'''

'''
valores.append(5)
valores.append(9)
valores.append(4)
'''

'''
for c, v in enumerate (valores): 
    print(f' Na posição {c} encontrei  {v} ! ')
print('Cheguei ao final da lista')

'''

a = [2, 3, 4, 7]
b = a[:] # cópia de todos os valores de A
b[2] = 8 # agora ira mudar somente na lista B


# b = a  # ligação e ficam iguais
# b[2] = 8 # ficam iguais
print(f'Lista A: {a}')
print(f'Lista B: {b}')