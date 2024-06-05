'''
DESENVOLVA UM PROGRAMA QUE LEIA NOME, IDADE E SEXO DE 4 PESSOA.
NO FINAL DO PROGRAMA, MOSTRE:

-A MÉDIA DE IDADE DO GRUPO
-QUAL É O NOME DO HOMEM MAIS VELHO.
'''
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range (1,5):  
    print(' -----{}ª PESSOA -----'.format(p)) 
    nome = str(input(' NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F] :  ')).strip()
    somaidade = somaidade + idade 
    if p == 1 and sexo in 'Mm': 
        maioridadehomem = idade
        nomevelho = nome

    #se sexo ainda estiver dentro de 'Mm'
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade 
        nomevelho = nome



médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos\n'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format (maioridadehomem, nomevelho))

    
