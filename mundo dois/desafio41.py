# A cofederação nacional da natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre a sua categoria, de acordo com a idade:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SÊNIOR
# acima: MASTER

ano = int(input("Digite o ano de seu nascimento: "))
idade = 2025 - ano

if idade <= 9:
    print("Você é da categoria MIRIM!")
elif idade <= 14:
    print("Você é da categoriaa INFANTIL!")
elif idade <= 19:
    print("Você é da categoria JUNIOR!")
elif idade == 20:
    print("Você é da categoria SêNIOR!")
else:
    print("Você é da categoria MASTER!")
