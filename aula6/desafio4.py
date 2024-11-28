#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ela
letra=input('digite uma letra: ')
numeroflutuante=float(input('digite um numero: '))
numeroInteiro=int(input('digite um numero: '))
valorBool=bool(input('digite qualquer valor: '))

print(type(letra))
print(type(numeroflutuante))
print(type(numeroInteiro))
print(type(valorBool))

print(letra.isalpha())
 #o .is serve para ver se a variavel é do tipo numerico, letra, minusculo, verdadeiro e falso