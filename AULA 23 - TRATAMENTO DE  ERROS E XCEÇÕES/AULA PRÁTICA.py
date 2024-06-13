try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a/b


except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou ! ')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero !') # tratamentos de erros com 0

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')


else:
    print(f'O resultado é {c} ')

finally:
    print('Volte sempre, muito obrigado !') #opcional



    '''

except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}!') # uma das opções de tratamento de erros.
'''
