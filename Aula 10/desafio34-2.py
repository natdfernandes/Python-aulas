#Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
#Para sálarios superiores a R$1.250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o sálario do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100) #15% de aumento
else:
    novo = salario + (salario * 10 / 100) #10% de aumento 
print('Quem ganhava R$ {:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))
