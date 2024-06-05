from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range (1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nascimento

    if idade >= 18:
        totmaior = totmaior + 1
        #print('Essa pessao tem {} anos'.format(idade),end='')
        #print(' e por isso é de maior')

    else:
        totmenor = totmenor + 1
        #print('Essa pessoa tem {} anos'.format(idade), end='')
        #print(' e por isso é de menor')
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))


