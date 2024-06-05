'''
CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA
COM UMA CONTAGEM POR EXTENSO DE ZERO A VINTE

SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20)
E  OSTRA-LO POR EXTENSO
'''
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove','dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0<= núm <= 20:
        break
    print('TENTE NOVAMENTE. ', end = '')
print(f'Você digitou o número {cont[núm]}')