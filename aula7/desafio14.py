#escreva um programa que converta uma temperatura difitada em ªc e a converta para ºf

c = float(input('Digita a temperatura em ºc: '))
f = ((9 * c) / 5 ) + 32 #mesmo sem usar os parenteses () o resultado seria o mesmo pela ordem de expressao

print('A temperatura de {}ºc corresponde a {}ºf!'.format(c, f))
