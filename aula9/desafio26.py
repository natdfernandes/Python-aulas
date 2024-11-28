#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "A"
#em que posição ela aparece a primeira vez
#em que posição ela aparece da ultima vez 

frase = str(input('Digite uma frase: ')).strip()
print(frase.count('a')) #contando as letras a
print(frase.find('a')) #quando começa da primeira vez
print(frase.rfind('a')) #ultima  vez que encontra a letra a