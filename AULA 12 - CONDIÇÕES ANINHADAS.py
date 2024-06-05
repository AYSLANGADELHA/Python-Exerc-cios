'''
Aula 12 - Condições Aninhadas
'''
nome = input('Qual o seu nome? ').capitalize()
if nome == 'Ayslan':
    print('Que nome diferente! ')
elif nome == 'Lara':
    print('Que nome lindo! ')
elif nome in ('Gustavo Claudia Janaina Janaína Ieda Glaucineide'):
    print('Que nome feminino! ')
else: print('Que nome normal! ')
