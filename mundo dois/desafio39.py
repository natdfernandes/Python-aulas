# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# se ele ainda vai se alistar no serviço militar
# se é a hora de se alistar
# se já passou do tempo de alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anos = int(input("Digite o ano do seu nascimento: "))
idade = 2025 - anos

if idade == 18:
    print("Você precisa se alistar no exército!")
elif idade > 18:
    atraso = idade - 18
    print("Você passou do prazo de alistamento! {} anos".format(atraso))
else:
    falta = 18 - idade
    print("Ainda falta tempo para se alistar!{} anos".format(falta))
