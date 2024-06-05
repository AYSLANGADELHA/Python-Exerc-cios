'''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO
O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR 999, 
QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM
DIGITADOS E QUAL FOI A SOMA ENTRE ELES.
'''
núm = cont = soma = 0
núm = int(input('Digite um número, [999 se deseja encerrar o programa]: '))
while núm != 999:
    soma += núm
    cont = cont + 1
    núm = int(input('Digite um número, [999 se deseja encerrar o programa]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))


    

        
          
                    
    