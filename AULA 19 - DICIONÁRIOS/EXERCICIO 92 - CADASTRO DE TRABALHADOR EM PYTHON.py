'''

CRIE UM PROGRAMA QUE LEIA:

- NOME
- ANO DE NASCIMENTO
- CARTEIRA DE TRABALHO

E CADASTRE-OS (COM IDADE) EM UM DICIONÁRIO SE POR ACASO A CARTEIRA DE TRABALHO FOR DIFERENTE DE ZERO
O DICIONÁRIO RECEBERÁ TAMBÉM O:

- ANO DE CONTRATAÇÃO
- SALÁRIO

CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.

'''

from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))

nasc = int(input('Ano de Nascimento: ')) # não estou cadastrando o ano de nascimento

dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 NÃO TEM): '))


if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - datetime.now().year)
print('-=' * 30)

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')