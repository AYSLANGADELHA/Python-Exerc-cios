# escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodados.

k = float(input('Quantos Km foram percorridos? '))
d = int(input('Quantos dias alugados? '))

QD = k * 0.15 + d * 60

print(' Por {}km percorridos em {} dias alugados, o cliente deverá pagar um valor de R${:.1f}'.format(k, d , QD))
