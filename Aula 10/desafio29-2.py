
velocidade = float(input('Qual é a velocidade  atual do carro? '))

if velocidade> 80:
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')

