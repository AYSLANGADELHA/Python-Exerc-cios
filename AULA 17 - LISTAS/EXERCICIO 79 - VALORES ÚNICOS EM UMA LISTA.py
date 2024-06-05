'''

CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS
E CADASTRE-OS EM UMA LISTA. CASO O NÚMERO JÁ EXISTE LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.
NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE.


'''

lista = []


while True:
    n = int(input('Digite um valor: '))

    if n not in lista: # se o valor digitado não estiver na variavel lista, ele será add
        lista.append(n) #adicionar valor (append)
        print('Valor adicionado com sucesso')

    else:
        print('Valor duplicado... Não vou adicionar')


    r = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if r in 'Nn': # se r estiver escrito N ou n o programa vai ser encerrado
        print('PROGRAMA ENCERRADO ')
        break
        

lista.sort() # colocar a lista em ordem/crescente

print(f'Os valores digitados são {lista} ')


 










'''

    usuário = ' '
    while usuário not in 'SN':
        usuário = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]

    if usuário == 'N':
        break
print()
lista.sort()
print(f'Você digitou os valores {lista} . ')
        

print('PROGRAMA ENCERRADO')

'''