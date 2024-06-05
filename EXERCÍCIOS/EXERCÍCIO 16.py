# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira


#import emoji

#smiley = emoji.emojize(':smile:', language='alias')

#print(smiley)

r = float(input('Digite um número: '))
p = r//1
print('A porção inteira de {} tem a parte inteira {}'.format(r,p))
