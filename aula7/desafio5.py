#faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
numero=int(input('Digite um numero inteiro: '))
sucessor=numero+1
antecessor=numero-1
print('O numero inteiro é {}, o sucessor é {}, e o antecessor é {}'.format(numero, sucessor, antecessor))


#fazendo o mesmo codigo mas com menos variaveis e sendo  mais direto
numero=int(input('Digite um numero inteiro: '))

print('O numero inteiro é {}, o sucessor é {}, e o antecessor é {}'.format(numero, (numero+1), (numero-1)))