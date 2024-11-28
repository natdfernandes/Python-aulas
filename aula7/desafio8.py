#escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros

metros=float(input('digite um valor em metros:' ))
centimetros=(metros * 100)
milimetros=(metros * 1000)

print('O metro é {}, em centimentros é {}, e em milimetros {}'.format(metros, centimetros, milimetros))     