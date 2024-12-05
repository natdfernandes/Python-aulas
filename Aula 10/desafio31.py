#Desenvolva um programa que pergunte a distancia de uma viagem em km.
#Calcule o preço preço da passagem, cobrando R$0,50 por km para viagens de até 200km
#E R$0,45 para viagens mais longas

distancia = float(input('Digite a distancia de uma viagem em km: '))
passagem = (distancia - 200) *0.50
distancialonga = (distancia + 200) * 0.45

if passagem<=200:
    print('Você pagará R$: {}'.format(passagem))
else:
    print('Você pagará a mais R$: {}'.format(distancialonga))