#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

salario=float(input('Salario R$: '))
aumento=salario + (salario + 15/100) #é 15% 

print('O salario atual com o aumento é {}'.format(aumento))