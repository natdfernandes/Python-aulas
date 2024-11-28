#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

algoritmo=int(input('digite um numero: '))
dobro=algoritmo * 2
triplo=algoritmo *3
raizquadrada=algoritmo ** (1/2)

print('O dobro do numero {} é {}, e o triplo é {}, e a raiz quadrada é {:.2f}'.format(algoritmo, dobro, triplo, raizquadrada))


#outra possibilidade de fazer o exercicio de maneira eficiente
n=int(input('digite um numero: '))

print('O dobro do numero {} é {}, e o triplo é {}, e \na raiz quadrada é {:.2f}'.format(n, (n * 2),(n * 3),(n**(1/2))))

#outra maneira de adicionar a raiz quadrada usando a versão pow()
n=int(input('digite um numero: '))

print('O dobro do numero {} é {}, e o triplo é {}, e \na raiz quadrada é {:.2f}'.format(n, (n * 2),(n * 3),pow(n, (1/2))))


