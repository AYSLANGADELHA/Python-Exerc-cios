'''
exercicio 43: Desenvolva uma lógica que leia o peso
e a altura de uma pessoa (IMC) e mostre seu status,de
acordo com a tabela abaixo:

- Abaixo de 18.5 : abaixo do peso
- Entre 18.5 e 25 : peso ideal
- 25 até 30 : sobrepeso
- 30 até 40 : obesidade
- Acima de 40 : obesidade mórbida

para calcular o IMC é: peso em kg / altura**2

'''
print('Para calcular seu IMC, ', end = '')
peso = float(input('digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m)  '))
imc = peso / (altura **2)
print('Seu imc é {:.1f}'.format(imc))

if imc < 18.5 :
    print('Você está abaixo do peso ! ')

elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal !')

elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso !')

elif imc >= 30 and imc < 40:
    print('Você está com obesidade ! ')

else:
    print('Você atingiu a obesidade mórbida,', end='')
    print('acima de 40, se cuide !!! ')





