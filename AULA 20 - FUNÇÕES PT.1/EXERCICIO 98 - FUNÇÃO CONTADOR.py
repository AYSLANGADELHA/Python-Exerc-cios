'''

FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR()
QUE RECEBA TRÊS PARAMêTROS: INÍCIO, FIM E PASSO. SEU PROGRAMA
TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:

A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA


# flush=True (para não ligar o bush de tela)

'''
from time import sleep

def contador(i, f, p):

    if p < 0:          # TRANSFORMANDO PASSO NEGATIVO EM POSITIVO
        p = p * -1     # PARA NÃO DA ERRO NO ITEM C, CASO O PASSO SEJA NEGATIVO.


    if p == 0:
        p = 1          # PARA NÃO OCORRER DE DA ERRO QUANDO O PASSO FOR 0



    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)



    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont = cont + p
        print('FIM')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end = '', flush=True)
            sleep(0.5)
            cont = cont - p
        print('FIM')
    

#Programa Principal
contador(1, 10, 1)  # RESPOSTA ITEM A

contador(10, 0, 2) # RESPOSTA ITEM B

print('-' * 20)

# RESPOSTA ITEM C
print('Agora é sua vez de personalizar a contagem ! ')
ini = int(input('INICIO:  '))
fim = int(input('FIM:     '))
passo = int(input('PASSO: '))

contador(ini, fim, passo)


