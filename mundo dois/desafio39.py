# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# se ele ainda vai se alistar no serviço militar
# se é a hora de se alistar
# se já passou do tempo de alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anos = int(input("Digite o ano do seu nascimento: "))
meses = 12 * anos

if anos == 18:
    print("Você precisa se alistar no exércit! {}".format(meses))
