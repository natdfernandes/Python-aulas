# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input("Escolha um número: "))
conversao = int(
    input(
        "Qual será a base de conversão escolhida: 1 Binário, 2 Octal, 3 Hexadecimal? "
    )
)


if conversao == 1:
    binario = bin(numero)
    print("O número esolhido é {} , em Binário é : {}".format(numero, binario))
elif conversao == 2:
    octal = oct(numero)
    print("O número escolhido é {}, em Octal é {}".format(numero, octal))
elif conversao == 3:
    hexadecimal = hex(numero)
    print("O número escolhido é {}, em hexadecimal é {}".format(numero, hexadecimal))
else:
    print("Nenhuma categoria foi escolhida, tente novamente!")
