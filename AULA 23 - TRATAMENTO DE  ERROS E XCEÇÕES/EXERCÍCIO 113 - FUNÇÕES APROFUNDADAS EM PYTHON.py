'''

REESCREVA A FUNÇÃO leiaint() FEITA NO EXERCÍCIO 104, INCLUINDO AGORA A POSSIBILIDADE
DA DIGITAÇÃO DE UM NÚMERO DE TIPO INVÁLIDO. APROVEITE E CRIE TAMBÉM UMA FUNÇÃO
leiaFloat() COM A MESMA FUNCIONALIDADE.

'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        
        except (ValueError, TypeError): # se for erro de valor ou de tipo
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue # para o voltar para dentro do laço novamente
            
        except (KeyboardInterrupt):
            print('\033[32mEntrada de dados interrompida pelo usuário.\033[m')
            return 0

        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
    

        except (KeyboardInterrupt):
            print('\n\033[32mUsuário preferiu não digitar esse número.\033[m')
            return 0
        
        else:
            return n
    








n1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}  ')

