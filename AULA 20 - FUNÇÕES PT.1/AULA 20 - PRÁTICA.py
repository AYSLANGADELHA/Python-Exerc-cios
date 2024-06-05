'''  1º exemplo

def lin():                  #DEFINIÇÃO DE UMA FUNÇÃO
    print('-=' * 30)

lin()                       # QUANDO FOR ESCREVER UMA LINHA, É SÓ CHAMAR A FUNÇÃO
print(' CURSO EM VÍDEO  ')
'''



# 2º exemplo (PARÂMETROS)
'''
def mensagem(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)

mensagem('CURSO EM VÍDEO')
'''





# 3º exemplo
'''

def titulo(txt):
    print('-'*40)
    print(txt)
    print('-'*40)

titulo('            EU SOU O MELHOR             ')

'''



# 4º exemplo
'''
def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')





# Programa Principal
soma(b=4,a=5)
'''

# SEM AS FUNÇÕES DEF
# a = 4
# b = 5
# s = a + b
# print(s)

# a = 8
# b = 9
# s = a + b
# print(s)

# a = 2
# b = 1
# s = a + b
# print(s)


'''
def contador(*núm):     # * serve para dizer que não sabe quantos números são
    tam =len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')



contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1




valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)









