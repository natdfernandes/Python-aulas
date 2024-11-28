#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta 
#necessaria para pinta la, sabendo que cada litro de tinta pinta uma area de 2m² (2 em cima pequeno)

largura=float(input('Digite a altura: '))
altura=float(input('Digite a largura: '))
area=largura * altura

print('Sua parede tem a dimensão de {} x {} e a sua area é de {} m²'.format(largura, altura, area))

tinta=area / 2

print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))