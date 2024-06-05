'''
Escreva um programa para aprovar o empréstimo bancario
para a compra de uma casa. O programa vai perguntar
o 'valor da casa', o 'salário do comprador' e
em 'quantos anos' ele vai pagar.

calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então
o empréstimo será negado
'''

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
# quanto ele vai pagar por mês em tantos anos
prestacao = casa / (anos * 12)
# salário dele mais 30%
minimo = salario * 30 / 100

print('Para pagar uma casa de R$ {} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f} '.format(prestacao))


if minimo >= prestacao:
    print('Empréstimo concedido')
else:
    print('Empréstimo negado, pois excedeu 30%')


