distancia = float(input(' Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {} km'.format(distancia))

preço = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('E o preço da sua passagem será de {:.2f}'.format(preço))



#if distancia <=20:
#    preço = distancia * 0.50 
#else:
#    preço = distancia * 0.45