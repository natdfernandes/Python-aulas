#crie um programa que leia o nome completo de uma pessoa e mostre: 
#o nome com todas as letras maiusculas
#o nome com todas minusculas
#quantas letras ao todo(sem considerar espaços)
#quantas letras tem o primeiro nome


nome = str(input('Digite seu nome completo: ')).strip() #strip vai eliminar os espaços antes e depois

#deixando o nome todo em maisculo
print('Seu nome em maisculo é {}'. format (nome.upper()))
#deixando tudo em minusculo
print('Seu nome em minusculo é {}' .format (nome.lower()))
#quantas letras tem ao todo no nome sem contar o espaço
print('Seu nome ao todo tem {} letras'.format(len(nome) -nome.count(' '))) # - contador de espaços
#quantas letras tem o primeiro nome
print('Seu primeiro nome tem {} letras' .format (nome.find(' '))) #vai parar de contar depois que encontrar o espaço


#outra maneira de resolver o exercicio usando split()
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))