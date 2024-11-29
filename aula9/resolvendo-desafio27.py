n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() 
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) #o len ve a posição e o -1 é para mostrar a ultima posição