frase = str(input(' Digite um frase: ')).strip().upper() #eliminou espações inuteis
palavras = frase.split() # foi criado uma divisão em espaços
junto = ''.join(palavras) # juntou as palavras (sem espaços)
inverso = ''
# a frase ao inverso no for
for letra in range(len(junto) - 1 , -1, -1):#len é para saber o comprimento da frase
 # a frase ao inverso no (FOR)              #o primeiro -1 é para pegar a ultima letra        
                                            #o segundo - 1 é para ir até a primeira letra
    #frase ao contrario                     #o terceiro - 1 é para ir voltando uma letra
    inverso = inverso + junto[letra]
if inverso == junto:
    print(junto, inverso)
    print('Temos um PALÍNDROMO')
else:
    print(junto, inverso)
    print('A frase digitada NÃO É UM PALÍNDROME')
