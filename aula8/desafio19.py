#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles, e escrevendo o nome escolhido

import random 

nomes=['Natalia', 'Leonardo', 'Thais', 'Enzo']

nome= random.choices((nomes))

print('O nome sorteado é {}'.format(nome))