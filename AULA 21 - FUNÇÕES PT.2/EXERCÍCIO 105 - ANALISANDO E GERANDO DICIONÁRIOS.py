'''

FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO notas() 
QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI
RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:


A) QUANTIDADE DE NOTAS
B) A MAIOR NOTA
C) A MENOR NOTA
D) A MÉDIA DA TURMA
E) A SITUAÇÃO (OPCIONAL)

ADICIONE TAMBÉM AS DOCSTRINGS.

'''

def notas(*n, sit=False):
    '''
    -> FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÕES DE VÁRIOS ALUNOS.

    :parametro n: UMA OU MAIS NOTAS DOS ALUNOS (ACEITA VÁRIAS)
    :parametro sit: VALOR OPCIONAL, INDICANDO SE DEVE OU NÃO ADICIONAR SITUAÇÃO
    :return:  DICIONÁRIO COM VÁRIA INFORMAÇÕES SOBRE A SITUAÇÃO DA TURMA

    '''
    r = {} #dicionário
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)

    if sit: #se situação for verdadeira
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'


    return r





# PROGRAMA PRINCIPAL

resp = notas( 5.5, 2.5, sit=True)
print(resp)
# or
# help(notas)