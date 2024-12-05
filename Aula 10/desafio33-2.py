#Faça um programa que leia três números e mostre qual é o maior e qual é o menor número 

numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
numero3 = int(input('Terceiro valor: '))

#verificando número menor
menor = numero1 #menor recebe o primeiro número
if numero2<numero1 and numero2<numero3:     #vai substituindo o valor do  número menor
    menor = numero2
if numero3<numero1 and numero3<numero2:
    menor = numero3
#verificando quem é maior
maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
if  numero3>numero1 and numero3>numero2:
    maior = numero3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
