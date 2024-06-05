'''
faça um programa que leia o ano de nascimento
de um jovem e informe de acordo com sua idade:

- se ele ainda vai se alistar ao serviço militar

- se é a hora de se alistar

- se já passou do tempo do alsitamento

seu programa também deverá mostrar o tempo que
falta ou que ja passou do prazo.

'''
from datetime import date
nascimento = float(input(' Qual o seu ano de nascimento: '))
idade = date.today().year - nascimento
# tempo que falta para poder se alistar

print('Hoje você tem {:.0f} anos. '.format(idade))

if idade < 18:
    print('Você ainda não pode se alistar')
    print('Ainda faltam {:.0f} ano(s). '.format(18 - idade))
elif idade >= 18:
    print('Você já pode se alistar !')
    print('Já passou do tempo do alistamento a {:.0f} ano(s)'. format(idade - 18))
    print('\033[4;31mCORRE QUE AINDA DA TEMPO\033[m')
print('Tenha um bom dia!')








