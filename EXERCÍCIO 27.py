frase = str(input('Digite seu nome: ')).strip()
nome = frase.split()[0]
ultimo = frase.rsplit()[-1]
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome))
print('Seu último nome é {}'.format(ultimo))






