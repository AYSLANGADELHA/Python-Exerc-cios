'''
AULA DE CORES

style : 0
        1
        4
        7
'''
# print('\033[35mOlá mundo')
#a = 3
#b = 5
#print('Os valores são \033[1;32;40m{}\033[m e \033[1;36;40m{}\033[m'.format(a,b))
'''
nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;35m', nome, '\033[4;35m'))
'''
# lógica de cores mais avançada
nome = 'Ayslan'
cores = {'azul': '\033[4;34;40m',
         'amarelo':'\033[1;35m',
         'verde': '\033[4;32m'}
print('Prazer em te conhecer {}{}{}!!!\033[m'.format(cores['verde'], nome, cores['azul']))






