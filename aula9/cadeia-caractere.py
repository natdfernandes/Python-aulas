#manipulando cadeia de texto
#sempre é usado aspas '' simples ou "" aspas duplas para strings
#maisculo e minusculo é visto de forma diferente em python
#exemplo de fatiamento: frase[9] vai pegar a letra da frase no espaço 9 contando a partir do zero 0
#frase Curso em Video Python
#     01234 56 78 910111213 14 151617181920  
#exemplo frase [9:13] seria a letra v, e o 13 é o e seria excluido
#no incio sempre começa com zero, mas no final sempre é excluindo 1
# frase[9:21] vai do 9 até o 20
#frase [9:21:2] o 2 vai ser para pular em dois em dois os numeros, vai saltando
#frase[:5] os : pontos é onde vai começar e o 5 seria onde vai parar, vai do 0 até o 4 e cortar o 5
#frase[15:] quando o numero vem primeiro e os : depois significa onde vai começar e até onde vai é o final da frase
#frase[9::3] começa no 9 e vai até o final, e quando chegar no 3 vai pular a cada 3

#analise
#len(frase) o len de frase seria 21 porque começa do 0 até acabar e chega em 21
#frase.count('o') conta quantas vezes tem o (o) minusculo, maisculo não
#frase.cocunt('o',0,13) o ultimo 13 seria ignorado, teria apenas 1 letra (o)
#frase.find('deo'), vai ver quantas vezes vai encontrar a letra d e o, vai indicar o 11 que é onde começou
#frase.find('Android'), iria retornar o valor -1 porque não existe essa frase, não foi encontrado
#'curso' in frase, vai mostrar true na tela porque tem a frase. é um operador

#transformação
#frase.replace('pyhton', 'android'), substitui a palavra python por android
#frase.upper(),é obrigatorio em função abrir e fechar os (), upper significa para cima, essa função faz tudo ficar maisculo
#frase.lower(), deixa tudo minusculo, substituindo os que estavam em maisculo
#frase.capitalize(), faz o primeiro caractere ficar maisculo e o resto todo em minusculo
#frase.title(), vai transformar toda primeira letra da palavra em maisculo conforme os espaços

#| | | |A|p|r|e|n|d|a| |P|y|t|h|o|n| | |  
#|0|1|2| |1|2|3|4|5|6|7|8|9| |10| |11|12|13|14|15|16| 17|18|
#frase.strip(), vai remover todos os espaços inuteis no começo,e os ultimos espaços, e a partir da letra A começaria a contagem 0
#frase.rstrip(), right direita, vai remover somente os ultimos espaços da direita, e vai manter os da esquerda
#frase.lstrip(), left esquerda, vai tirar os espaços da esquerda, e vai manter os espaços da direita

#divisão
#frase
#Curso em Video Pyhton
#frase.split(), é feito nos espaços e vai criar uma divisão, a cada começo de palavra começa pelo 01, é colocada dentro de uma nova lista

#junção
#'-'.join(frase), vai juntar todos os elementos de frase e vai usar o separador
#curso-em-video-python
#' '.join(frase), vai juntar todos os elementos de frase e vai usar o separador colocando espaço entre eles
#curso em video python


