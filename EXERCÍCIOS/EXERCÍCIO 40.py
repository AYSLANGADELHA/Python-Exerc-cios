'''
crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final
de acordo com a média atingida:

- média abaixo de 5.0 : REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superiror: APROVADO

'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2) / 2

#REPROVADO
if media < 5:
    print('\033[4;31mVocê foi REPROVADO(A)\033[m')
    print('TENTE NOVAMENTE')
    print('Sua média é de {}'.format(media))

#RECUPERAÇÃO
elif media >= 5 and media <= 6.9: # if 7 > media >= 5
    print('\033[7;30;47mVocê ficou de RECUPERAÇÃO\033[m')
    print('TENTE NOVAMENTE')
    print('Sua média é de {}'.format(media))

#APROVADO
if media >= 7:
    print('\033[4;32mVocê foi APROVADO(A) \033[m', end = '')
    print('PARABÉNS ! ')
    print('Sua média é de {}'.format(media))

print('Tenha um bom dia!')


