#escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80km mostre uma mensagem dizendo que ele foi multado
#a mulda custa 7 reais por cada Km acima do limite

velocidade = float(input('A quantos km/h você se encontra no seu carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80km/h!')
    print('Sua multa é de R${:.2f}'.format(multa))
else:
    print('Tenha um ótimo dia, dirija com segurança.')


