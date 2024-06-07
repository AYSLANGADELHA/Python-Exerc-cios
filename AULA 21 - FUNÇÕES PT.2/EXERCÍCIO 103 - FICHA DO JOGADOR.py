'''

FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBE
DOIS PARÂMETROS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.

O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, 
MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.


'''

def ficha(jog = '<desconhecido>' , gols = 0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato')
    
    









# PROGRAMA PRINCIPAL
n = str(input('Nome do Jogador: '))
g = str(input('Quantos gols ele fez: '))

# PARA SABER SE A VARIÁVEL g PODE SER UM NÚMERO
if g.isnumeric(): 
# SE g FOR NÚMERICO O g PASSARÁ A SER UM INT DE g
    g = int(g)  

else:
    g = 0

# SE TIROU TODOS OS ESPAÇOS E AI ELE FICOU VAZIO, vou chamar a ficha de um jeito
if n.strip() == '': 
    ficha(gols=g)

# SE NÃO, VOU CHAMAR DE OUTRO
else:
    ficha(n , g)

