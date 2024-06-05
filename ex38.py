'''
Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, ambos são iguais
'''

maior = int(input('Digite o primeiro valor: '))
menor = int(input('Digite o segundo valor: '))

if maior == menor:
    print('Não existe valor maior, ambos são iguais')
elif maior > menor:
    print('O número {} é maior que o {}'. format(maior, menor))
else:
    print('O número {} é maior que o {}'.format(menor,maior))

print('FIM DO PROGRAMA, OBRIGADO !')

