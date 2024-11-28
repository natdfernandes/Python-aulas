#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considere us$1,00=r$3,27

dinheiro=float(input('Digite quanto dinheiro você tem R$: '))
dolar=dinheiro /5.78

print('Com R${:.2f} você pode comprar US${:.2f} dolares'.format (dinheiro, dolar))