# escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
c = float(input('informe a temperatura em ºC: '))
f = (9 * c) / 5 + 32

print('O valor {:.0f}ºC  em Fahrenheit é {:.0f}ºF! '.format(c,f))
