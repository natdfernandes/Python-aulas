#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome tem silva? {}'.format('silva' in nome.lower()))