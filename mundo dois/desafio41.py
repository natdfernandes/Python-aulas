# A cofederação nacional da natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre a sua categoria, de acordo com a idade:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SÊNIOR
# acima: MASTER

ano = int(input("Digite o ano de seu nascimento: "))
anoatual = 2025 - ano
idade = anoatual

if ano <= 2016:
    print("Você é da categoria MIRIM!")
elif ano <= 2011:
    print("Você é da categoriaa INFANTIL!")
elif ano <= 2006:
    print("Você é da categoria JUNIOR!")
