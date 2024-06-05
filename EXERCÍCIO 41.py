'''
a confederação Nacional de Natação precisa
de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo
com a idade:

- Até 9 anos MIRIM
- Até 14 anos INFANTIL
- Até 19 anos JUNIO
- Até 20 anos SENIOR
- Acima de 20 anos MASTER
'''
from datetime import date
# idade = int(input('Qual a idade do atleta ? '))
# nascimento = int(input('Qual o ano de nascimento ? '))
atual = date.today().year
nascimento = int(input('Qual o ano de nascimento:  '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))



if idade <= 9:
    print('O atleta de até {} anos se encaixa na categoria MIRIM '.format(idade))
elif idade <= 14:
    print('O atleta de até {} anos se encaixa na categoria INFANTIL '.format(idade))
elif idade <= 19:
    print('O atleta de até {} anos se encaixa na categoria JUNIO'.format(idade))
elif idade <= 25:
    print('O atleta de até {} anos se encaixa na categoria SENIOR'.format(idade))
elif idade > 25:
    print('O atleta acima de 20 anos só participará da categoria MASTER')

