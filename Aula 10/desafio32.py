#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO 

ano = int(input('Digite um ano: '))
#O ano que é BISSEXTO É DIVISIVEL POR 4
if ano %4 ==0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')