#Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR

numero = int(input('Digite um número inteiro: '))

#se o numero for divisivel por 2 é par, número impar não é divisivel por 2
if numero %2 == 0:
    print('Esse número é par!')
else:
    print('Esse número é impar!')    