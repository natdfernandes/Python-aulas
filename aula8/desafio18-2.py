#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno, e tangente desse angulo
#importando apenas a função que sera utilizada

from math import radians, sin, cos, tan 

angulo=float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo,seno))


cosseno=cos(radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f} '.format(angulo,cosseno))

tangente=tan(radians(angulo))
print('O angulo de {}, tem a tangente de {:.2f}'.format(angulo, tangente))