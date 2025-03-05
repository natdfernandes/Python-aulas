# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# abaixo de 18.5: ABAIXO DO PESO
# Entre 18.5 e 25: PESO IDEAL
# 25 até 30: SOBREPESO
# 30 até 40: OBESIDADE
# acima de 40: OBESIDADE MÓRBIDA

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso!")
elif imc <= 25:
    print("Peso ideal!")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")
