n1= int(input('Um valor: '))
n2= int(input('outro valor: '))

soma= n1 + n2
multiplicacao= n1 * n2
divisao= n1 / n2
divisaoInteira= n1 // n2
espocientacao= n1 ** n2

#o \n serve como quebra de linha
#o end='  ' serviu de espaçamento
#o end='>>>' mostra o segmento

print('A soma é {}, \n o produto é {}, e a \n divisão é {:.3f}'.format(soma,multiplicacao, divisao, end ='>>> '))
print('Divisão inteira {}, e potencia{}'.format(divisaoInteira, espocientacao))