# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# considerando que o Dólar é =  3.27

c1 = int(input('Quanto de dinheiro Joãozinho tem na carteira? R$ '))
dólar = c1/5.27
euros = c1/5.59
print('Com R${:.2f} dólares ,Joãozinho consegue comprar R${:.2f} dólares e {:.2f} euros!'.format(c1,dólar,euros))
