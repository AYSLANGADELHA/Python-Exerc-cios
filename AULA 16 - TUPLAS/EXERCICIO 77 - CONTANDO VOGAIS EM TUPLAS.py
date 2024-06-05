'''

CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS
(NÃO USAR ACENTOS). DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA
QUAIS SÃO AS SUAS VOGAIS.

'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')