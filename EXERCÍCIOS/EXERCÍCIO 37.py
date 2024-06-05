#CONVERSOR DE BASES NUMÉRICAS
num = int(input('Digite um número inteiro: '))
print ('''Escolha uma das bases de conversão
                  [1] converter para BINARIO
                  [2] converter para OCTAL
                  [3] converter para HEXADECIMAL''')
opção = int(input('SUA OPÇÃO É: '))
if opção == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print ('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print(' O número {} convertido para HEXADECIMAL é {}'.format(num,hex(num)[2:]))

else:
    print('OPÇAO INVÁLIDA, TENTE NOVAMENTE')





