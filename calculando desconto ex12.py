# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual é o preço do produto? R$ '))
novopreco = preço - (preço * 5 /100)
print('O produto que custava \033[4;31mR${}\033[m, na promoção ficará de \033[4;32mR$ {}\033[m.'.format(preço,novopreco))



