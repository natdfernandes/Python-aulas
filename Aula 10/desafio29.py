#Escreva um programa que leia a velocidade de um carro 
#Se ele ultrapassar 80k/h, mostre uma mensagem dizendo que ele foi multado 
#A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Digite a velocidade do carro K/H: '))
multa =  (velocidade - 80) * 7.00
#10km vai ser acrescentado 7.00

if velocidade>80:
    print(' Você foi multado!')
    print('Você pagará R$: {}'.format(multa))
else:
    print('Você não foi multado, continue na linha...')
