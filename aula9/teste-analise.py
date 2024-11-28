#analise
frase = 'Curso em Video Python'
print(len(frase)) #para saber quantos caracteres tem no total do começo até o fim
print(frase.count('o')) #mostra quantas vezes é usado a letra o
print(frase.count('o',0,13)) #contagem com fatiamento do 0 até o 12 tem apenas 1 letra o
print(frase.find('deo')) #quantas vezes encontrou o deo
print(frase.find('Android')) #não existe por isso retorna o valor -1
print('Curso' in frase) #O operador in verifica se existe a palavra e mostra True ou False