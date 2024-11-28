#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa

import math 

catetoOposto= float(input('Digite o temanho do cateto oposto: '))
catetoAdjacente= float(input('Digite o tamanho do cateto adjacente: '))
hipotenusa= (catetoOposto * 2 + catetoAdjacente * 2) ** (1/2) #cateto² + catetoA² resto

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))