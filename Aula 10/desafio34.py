#Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
#Para sálarios superiores a R$1.250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o seu sálario R$: '))
menor = (salario * 10/100) + salario
maior = (salario * 15/100) + salario

if salario:
    print('O seu novo sálario com aumento de 10% será de R$: {}'.format(menor))
else:
    print('O seu novo sálario com aumento de 15% será de R$: {}'.format(maior))


