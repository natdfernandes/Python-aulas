#faça um programa que leia um numero de 0 a 999 e mostre na tela cada um dos digitos separados
#exemplo: digite um  numero:1834
#unidade:4
#dezena:3
#centena:8
#milhar:1

numero = int(input('Digite um numero: ')) 
unidade = numero//1 % 10    #faz a divisão do primeiro numero e o resto de 10, unidade
dezena =  numero//10 % 10   #dezena
centena = numero//100 % 10  #centena
milhar =  numero//1000 % 10 #milhar

print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
