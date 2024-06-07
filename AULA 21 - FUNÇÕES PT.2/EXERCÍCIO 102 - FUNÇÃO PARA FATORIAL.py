'''

CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL()
QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE
O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERÁ
UM VALOR LÓGICO(OPCIONAL) INDICANDO SE SERÁ MOSTRADO
OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL

'''

def fatorial(n, show=False):   #show=False é um parâmetro opcional
    fatorial = 1
    for c in range(n, 0 , -1):
        if show: # se show=True
            print(c, end='')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end ='')
        fatorial = fatorial * c
    return fatorial








# PROGRAMA PRINCIPAL
print(fatorial(5, show=True))
print(fatorial(5))
