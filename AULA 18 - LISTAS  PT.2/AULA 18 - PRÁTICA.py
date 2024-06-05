''' PRIMEIOR TESTE

teste = []
teste.append('Gustavo') #posi 0
teste.append(40) #posi 1

galera = []
galera.append(teste[:]) #lista galera, add na lista teste

teste[0] = 'Maria' #assumiu posi 0
teste[1] = 22 #assumiu posi 1
galera.append(teste[:])
print(galera)

'''

''' # EXEMPLO 2

galera = [ ['João',19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade. ')

         
OU ESSE ABAIXO: 

# print(galera[2] [1]) #primeiro colchete (indice 0 de galera) 
                     #segundo colchete (indice 0 da primeira lista dentro de galera)
'''


# EXEMPLO 3

galera = []
dado = []
total_maior = 0
total_menor = 0

for cont in range (0,5):
    dado.append(str(input('NOME: ')))
    dado.append(int(input('IDADE: ')))

    galera.append(dado[:]) # cópia de dado
    dado.clear() #apagando lista dado
    
# print(galera)

for p in galera:
    if p[1] >= 21:
        print(f' {p[0]} é maior de idade. ')
        total_maior = total_maior + 1
    else: 
        total_menor = total_menor + 1
        print(f' {p[0]} é menor de idade. ')

print(f'Temos {total_maior} maiores de idade e {total_menor} menores de idade ')