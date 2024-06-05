'''

FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA()
QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM
COM TAMANHO ADAPTÁVEL.

'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)





# Programa principal
escreva('AYSLAN DE SOUZA GADELHA')
escreva('LARA DE OLIVEIRA SILVA QUEIROZ')