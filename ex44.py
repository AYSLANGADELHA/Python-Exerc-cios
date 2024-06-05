'''
Elabore um programa que calcule o valor a ser
pago por um produtro, considerando o seu
preço normal, e condição de pagamento:

- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

valor = float(input('Qual o valor do produto? R$ '))
print('Qual será a forma de pagamento? \n 1 - À vista dinheiro/cheque \n 2 - À vista no cartão \n 3 - Em até 2x no cartão \n 4 - 3x ou mais no cartão ')
pagamento = int(input('Qual a forma de pagamento ? '))

# dinheiro / cheque: 10% desconto
if pagamento == 1:
    valor = valor - (valor* (10/100))
    print('Você recebeu um desconto de 10%')

# a vista cartão: 5% desconto
elif pagamento == 2:
    valor = valor - (valor * (5/100))
    print('Você recebeu um desconto de 5%')
# 2x no cartão : preço normal
elif  pagamento == 3:
    valor = valor / 2
    print('O produto ficar parcelado em 2x de R${:.2f}'.format(valor))
    # 3x ou mais no cartão: 20% de juros
elif pagamento == 4:
    valor = valor + (valor * (20/100))
    quanpar = (int(input('Quantas parcelas ? ')))
    parcela = valor / quanpar
    print('O produto custará R$ {:.2f} com parcelas de R$ {:.2f} + juros de 20% . '.format(valor, parcela))

#valor do produto
print('O produto custará R$ {:.2f}'.format(valor))








