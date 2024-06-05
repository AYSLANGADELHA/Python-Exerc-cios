'''
CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔICO.
NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO(NÚMERO INTEIRO)
E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.

COSNIDERE QUE O CAIXA POSSUI CÉDULAS DE 50, 20, 10 E 1 REAL.
'''


print('='*40)
print('{:^40}'.format('BEM VINDO AO BANCO GADELHA'))
print('='*40)

valor = int(input('Que valor você quer sacar ? R$ '))
total = valor #montante
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédula de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='* 40)
print('Volte sempre ao banco GADELHA    ')
