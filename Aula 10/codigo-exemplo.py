nome = str(input('Qual é o seu nome? '))
if nome == 'Natalia':
    print('Que nome lindo você tem!') #é unma estrutura condicional simples quando tem apenas o if sem o else
else:
    print('Seu nome é tão normal') #condicional composta quando tem o else
print('Bom dia, {}'.format(nome))  