'''

CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA voto() QUE VAI 
RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA
RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO

NEGADO - OPCIONAL - OBRIGATÓRIO NAS ELEIÇÕES

'''




def voto(ano):
   from datetime import date
   anoAtual = date.today().year
   idade = anoAtual - ano

   if idade < 16:
      return f'Com {idade} anos: NÃO VOTA !'
   
   elif 16 <= idade < 18 or idade > 65:
      return f'Com {idade} anos: VOTO OPCIONAL ! '
   
   else:
      return f'Com {idade} anos: VOTO OBRIGATÓRIO !'
   



anoNasc = int(input('Para saber seu status de voto, digite o ano em que você nasceu: '))
print(voto(anoNasc))
      
      


