'''
FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS
SÓ ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO
NOVAMENTE ATÉ TER UM VALOR CORRETO.
'''
sexo = str(input('Qual o seu sexo ? [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, digite novamente: ')).strip().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

    
     

