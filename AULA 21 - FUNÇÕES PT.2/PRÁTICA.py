def par(n=0):
    if  n % 2 == 0:
        return True
    
    else:
        return False


num = int(input('Digite um número: '))

if par(num):
    print('É PAR')

else:
    print('NÃO É PAR')



























# DEFINIÇÃO DE FUNÇÃO PARA OS 2 PRIMEIROS EXEMPLOS:

# def fatorial (num = 1):
    # f = 1
    # for c in range (num, 0, -1):
        # f = f * c
    
    # return f

#------------------------------------------------------#


# 1º EXEMPLO

# n = int(input('Digite um número: '))
# print(f' O fatorial de {n} é igual a {fatorial(n)}')
#------------------------------------------------------#

# 2º EXEMPLO

# f1 = fatorial(5)
# f2 = fatorial(3)
# f3 = fatorial(6)

# print(f'{f1} -> {f2} -> {f3}')
#------------------------------------------------------#