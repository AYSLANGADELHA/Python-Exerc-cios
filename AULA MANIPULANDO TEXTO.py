# manipulando texto

FATIAMENTO

frase = ('Curso em vídeo Python')

frase[9]
frase[9:13]
frase[9:21]
frase[9:21:2] - pulando de 2 em 2
frase[:5] - do 0 ao 5
frase[15:] - do 15 ao final
frase[9::3] - começa no 9 até o final, pulando de 3 em 3

#COMPRIMENTO

len(frase)
frase.count('o') - contar quantas vezes aparece a vogal 'o'
frase.count('o', 0, 13) - quantos "o" tem até o 13

frase.find('deo') - encontrar onde começa o "deo"
frase.find('android') - quando não existir a palavra na variável vai ser = -1

'curso' in frase

#TRANSFORMAÇÃO

frase.replace('Python', 'Android') trocar/substituir
frase.upper() - todas maiúsculas
frase.lower() - todas minúsculas
frase.capitalize() - todas ficam minusculas e primeira letra da frase fica maiuscula
frase.title() - todas palavras das quebras ficam com a primeira letra maiusculas

FRASE =    APRENDA PYTHON

frase.strip() - remove todos os espaços inuteis
frase.rstrip() - remove todos os espaços da direita
frase.lstrip() - remove todos os espaços da esquerda

#DIVISÃO

FRASE = CURSO EM VÍDEO PYTHON

frase.split() - onde tiver espaço vai ser criado uma divisão

#JUNÇÃO

'-'.join(frase) - junta todos os elementos da frase usando o separador '-'
