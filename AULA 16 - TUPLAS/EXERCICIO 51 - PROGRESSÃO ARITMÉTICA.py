'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

primeiro = int(input('Primeiro Termo: ')) # de onde vai começar a progresssão aritmetica (PA)
razão = int(input('Razão: ')) #de quantos em quantos números
décimo = primeiro + (10 - 1) * razão #para descorbrir o enézimo termo de uma pa essa é a fórmula utilizada (10 - 1 * razão)

for c in range (primeiro, décimo + razão , razão):
    print('{}'.format(c), end= '-> ')
print('ACABOU)')