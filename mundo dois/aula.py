#estrutura condicional

nome = str(input('Qual é seu nome? '))
if nome == 'Natalia':     #condição simples
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'João' or nome =='Paulo':  #estrutura condicional aninhada
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Aurora Ariel Suzi':
    print('Belo nome feminino!')
else:                     #estrutura condicional composta
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))  