'''
faça um programa que leia o primeiro termo e a razão de uma PA
mostrando os 10 primeiros termos da progressão usando WHILE
'''
print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: ')) #de onde vai começar a PA
razão = int(input('RAZÃO DA PA:  ')) # de quantos em quantos vai pular essa PA
#arit = primeiro + (10-1) * razão # para descobrir o enézimo termo

termo = primeiro
cont = 1


while cont <= 10:
    print(' {} -> '.format(termo),end='')
    termo = termo + razão 
    cont = cont + 1

print('FIM')
