'''
Escreva um program que pergunte o salário de um
funcionário e calcule o valor do seu aumento.

Para salários superiores a R$ 1250,00,calcule
um aumento de 10%.

Para os inferiores ou iguais, o aumento de 15%.
'''

salario = float(input('Qual o seu salário atual? R$ '))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print ('Seu aumento foi de \033[4;31mR$ {:.2f}\033[m para  \033[4;32mR$ {:.2f}\033[m'.format(salario, aumento))
if salario <= 1250:
    aumento2 = salario + (salario * 15 / 100)
    print('Seu aumento foi de \033[4;31mR$ {:.2f}\033[m para  \033[4;32mR$ {:.2f}\033[m'.format(salario, aumento2))

print('Você foi promovido, PARABÉNS')


