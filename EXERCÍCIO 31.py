viagem = str(input('Qual o destino da viagem? '))
distancia = int(input('Qual a distancia da sua viagem em km ? '))
cobrar = distancia * 0.50
cobrar2 = distancia * 0.45

if distancia <= 200:
    print('O valor da viagem será R${:.2f}'.format(cobrar))
if distancia > 200:
    print('O valor da viagem será R${:.2f}'.format(cobrar2))



