#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidde de dias pelos quais
#ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

km = float(input('Quantos km rodados: '))
dias = int(input('Quantidade de dias: '))
pago= (dias * 60) + (km * 0.15)

print('O total a pagar será R${:.2f}'. format(pago))
