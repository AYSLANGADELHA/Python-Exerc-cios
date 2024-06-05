''''
Crie um programa que leia dois valores e mostre um menu
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 -sair do programa
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')     
    opção = int(input('Qual sua opção ? '))
    if opção == 1: #SOMAR
        soma = n1+n2
        print('A soma entre {} e {} é igual a {}'.format(n1,n2,soma))
        
    elif opção == 2: # MULTIPLICAR
        multiplicação = n1*n2
        print('{} x {} é igual a {}'.format(n1,n2,multiplicação))


    elif opção == 3: # MAIOR NÚMERO
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
        

    elif opção == 4: # NOVOS NÚMEROS
        print('informe os números novamente ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opção == 5: # SAIR DO PROGRAMA
        print('FINALIZANDO PRGRAMA...')
    else:
        print('Opção inválida, TENTE NOVAMENTE !!!')

print('FIM DO PROGRAMA! Volte sempre!!')


