'''

CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA
NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRAR
AS NOTAS DE CADA ALUNO INDIVIDUALMENTE:

'''

ficha = []

while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2 ) / 2
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('QUER CONTINUAR ? [S/N] '))

    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4} {"NOME":<10} {"MÉDIA":>8}') # (> direita) (< esquerda) (:<10 - significa alinhado a esquerda 10 espaços)
print('-' * 26)

# mostrando indice 0,1 e 2 de acordo com oq o programa pede
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')


while True:
    print('-=' * 35)
    opção = int(input('MOSTRAR NOTAS DE QUAL ALUNO ? (999 INTERROMPE): '))

    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção] [0]} são {ficha[opção] [1]} ')

print('VOLTE SEMPRE')