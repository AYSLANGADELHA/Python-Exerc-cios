'''
Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar
um triângulo.
'''
import time
print('='*25)
print('Analisador de Triângulo')
print('='*25)




# segmentos
'''
para formar um triângulo, a soma de dois lados
devem ser menor ou igual ao terceiro lado
'''

r1 = float(input('Qual o comprimento da primeira reta: '))
r2 = float(input('Da segunda: '))
r3 = float(input('E o da terceira reta: '))
time.sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO! ')
else:
    print('Os segmentos acima não NÃO PODEM FORMAR um triângulo! ')




