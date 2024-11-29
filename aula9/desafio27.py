#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente
#exemplo: Ana Maria de souza
#primeiro:ana
#ultimo= souza

nome = str(input('Digite seu nome completo: ')).split()
print(nome)
#mostre o primeiro nome
#nome = nome.split()
print('O primeiro nome é {}'.format(nome[0]))
#mostre o ultimo nome
print('O ultimo nome é {}'.format(nome[2]))
