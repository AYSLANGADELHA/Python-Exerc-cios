'''
CRIE UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO
E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:

a - quantas vezes apareceu o valor 9
b - em que posição foi digitado o primeiro valor 3
c - quais foram os números pares

'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))

todos = (n1,n2,n3,n4)
print(todos)

print('=' * 30)
print('INICIANDO ANÁLISE EM TUPLAS')
print('=' * 30)

valor9 = (todos.count(9)) # para poder saber quantas vezes o valor 9 apareceu
print(f'O valor 9 apareceu {valor9} vezes') 

                                #index

 # para poder achar a posição do número 3 e o +1 para ignorar a posição 0 
if 3 in todos: # para não dar erro quando n existir número 3
    posi3 = todos.index(3) + 1 # para poder achar a posição do número 3 e o +1 para ignorar a posição 0
    print(f'O valor 3 foi digitado na {posi3}ª posição')
else:
    print('O número 3 não foi encontrado')


print('Os valores pares digitados foram',end = ' ')

for c in todos:
    if c % 2 == 0:     
             # para localizar quais números pares foram digitados
        print(c, end=', ')

