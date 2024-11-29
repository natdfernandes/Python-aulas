frase = str(input('Digite uma frase: ')).upper().strip() #deixar maisculo e tirar o espaço da frente e por ultimo
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))#para mostrar a 1 posição
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))