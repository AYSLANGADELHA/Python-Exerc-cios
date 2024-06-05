# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um retangulo. Calcule e mostre o cumprimento da hipotenusa.

from math import pow

x = float(input('Qual o comprimento do Cateto Oposto: '))
z = float(input('Qual o comprimento do Cateto Adjacente: '))
h = pow(x,2) + pow(z,2)
print (' A hipotenusa vai medir {}'.format(h))
