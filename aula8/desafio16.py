#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
#ex: digite um numero inteiro 6.127, o numero 6.127 tem a parte inteira 6

import math

numero = float(input('Digite um numero real: '))

print('O numero real é {} e o numero inteiro é {}'.format(numero, math.trunc(numero)))


#outra maneira de fazer o mesmo programa sem importar a biblioteca
#num= float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))