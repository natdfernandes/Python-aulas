#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto

preco=float(input('Preço do produto R$: '))
valorAtual=preco - (preco * 5/100) #O novo preço será o valor com o -5% 

print('O valor atual com desconto é {:.2f}'.format(valorAtual))