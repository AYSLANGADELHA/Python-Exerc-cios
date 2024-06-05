'''

FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA, QUE RECEBA AS DIMENSÕES
DE UM TERRENO RETANGULAR(LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO

'''
#FUNÇÃO ÁREA
def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m². ')



#PROGRAMA PRINCIPAL
print(' Controle de Terrenos')
print('-'*20)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)