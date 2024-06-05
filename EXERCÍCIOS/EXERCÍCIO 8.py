#exercício 8
# km hm dam m dm cm mm
a1 = float(input('Quantos metros você utilizou de cerâmica no seu imóvel?'))

x = a1*100    #centimetros
y = a1*1000   # milímetros
dm = a1*10
dam = a1/10
hm = a1/100
km = a1/1000
print('O valor em centímetros equivalem a {}cm, em milímetros equivalem a {}mm, em decímetros é {}, em decametro é {}, em hectometro é {} e em quilometros é {}'.format(x,y,dm,dam,hm,km))
