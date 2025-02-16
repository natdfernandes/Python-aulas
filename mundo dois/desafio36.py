# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálario ou então o emprestimo será negado.


casa = float(input("Qual o valor da casa R$: "))
salario = float(input("Qual é o seu sálario? "))
anos = int(input("Em quantos anos você pagará a casa? "))
# logica para conseguir converter anos em meses
meses = 12 * anos
valorparcela = casa / meses
# calculo dos 30% do sálario
mensal = (salario * 30) / 100

if valorparcela > mensal:
    print("Você não poderá comprar a casa! Excedeu o valor dos 30%")
else:
    print("O emprestimo foi aprovado, PARÁBENS! Você tem uma casa.")
