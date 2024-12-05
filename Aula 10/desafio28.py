#escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir
#qual foi o numero escolhido pelo computador
#o peograma deverá mostrar na tela se o usuario venceu ou perdeu 

import random
usuario = int(input('Digite o número que estou pensando de 1 a 5: '))
print('Estou pensando em um número...')
numero = random.randint(0,5)

#se venceu
if numero == usuario: 
    print('Você ganhou!')
#se perdeu
else:
    print('Você perdeu!')
print('--FIM--')