'''

CRIE UM PROGRAMA ONDE O USUÁRIO DIIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES
SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARENTESES ABERTOS E FECHADOS
NA ORDEM CORRETA!!!

'''


expr = str(input('Digite a expressão: '))
pilha = []

for símb in expr:
    if símb == '(':
        pilha.append('(')

    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else: 
            pilha.append(')')
            break

if len(pilha) == 0:
    print(f'Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')