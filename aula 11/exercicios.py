nome = input ('qual é o seu nome? ')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'roxo':'\033[35m',
         'azulmarinho':'\033[36m',
         }

print('Olá {}{}{}, seja bem-vindo(a)!'.format(cores['roxo'], nome, cores['limpa']))