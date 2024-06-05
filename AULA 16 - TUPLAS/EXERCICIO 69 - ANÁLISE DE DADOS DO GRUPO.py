'''
CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA
CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU N CONTINUAR.
NO FINAL MOSTRE: 
A- QUANTAS PESSOAS TEM MAIOR DE 18 ANOS
B- QUANTOS HOMENS FORAM CADASTRADOS 
C- QUANTAS MULHERES TEM MENOS DE 20 ANOS.
'''

maior = 0
homem = 0
mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        maior = maior + 1
    
    if sexo == 'M':
        homem = homem + 1
    
    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1


    

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer contiuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'Existem {mulheres} mulheres com menos de 20 anos')




