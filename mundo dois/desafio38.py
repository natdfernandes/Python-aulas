# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# não existe valor maior os dois são iguais

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior")
elif numero2 > numero1:
    print("O segundo número é maior")
else:
    print("Os números são iguais")
