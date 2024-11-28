import math

num = int (input ('digite um numero: '))
raiz= math.sqrt (num)

print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

#print('A raiz de {} é igual a {:.2f}'.format(num,math.ceil(raiz))) para aredondar o numero para cima
#print('A raiz de {} é igual a {:.2f}'.format(num,math.floor(raiz))) para aredondar o numero para baixo