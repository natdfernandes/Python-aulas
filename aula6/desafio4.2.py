a=input('digite algo: ')

print('O tipo primitivo desse valor é ', type(a))
print('So tem espaço?', a.isspace()) #se tem espaço
print('É um numero?',a.isnumeric()) #se é numerico
print('É alfabetico',a.isalpha()) # se é alfabetico, sempre abrir e fechar () quando colocar uma função
print('É alfanumerico?',a.isalnum()) #se é alfanumerico, letras e numeros
print('Está em maisculo?', a.isupper()) #se está em maisculo
print('Está em minusculo?', a.islower()) #se está em minusculo
print('Está capitalizada?', a.istitle()) #se está minuscula e maiscula

#o a na frente é um objeto que tem caracteristicas, metodos
