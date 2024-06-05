print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: ')) #de onde vai começar a PA
razão = int(input('RAZÃO DA PA:  ')) # de quantos em quantos vai pular essa PA
#arit = primeiro + (10-1) * razão # para descobrir o enézimo termo

termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} -> '.format(termo),end='')
        termo = termo + razão 
        cont = cont + 1

    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais ? '))

print('Progressão finalizada com {} termos'.format(total))


