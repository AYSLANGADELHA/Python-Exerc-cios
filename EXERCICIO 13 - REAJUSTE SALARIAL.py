# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto.
salário = float(input('Qual o faturamento mensal do empresário Ayslan? R$'))
novo = salário + (salário * 15 / 100)

print('O empresário que ganhava R${}, com o acréscimo de 15%, passará a ganhar R$ {:.2f}'.format(salário,novo))