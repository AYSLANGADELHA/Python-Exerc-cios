# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print('A dimensão da parede é de {}x{} e sua área corresponde a {}m². Que precisará de {}l de tinta'.format(largura,altura,area,tinta))
