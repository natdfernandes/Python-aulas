#testes
frase = 'Curso em Video Python'
print(frase)
print(frase[3]) #fatiando
print(frase[3:13])
print(frase[:13]) #do começo até o 13
print(frase[13:]) #o começo é 13 e o final é até o fim da string
print(frase[1:15]) #da posição 1 ate 15
print(frase[1:15:2]) #o ultimo valor mostrara quanto sera pulado, em 2 em 2
print(frase[::2]) #pulando em 2 em 2
print('oi')
print("""welcome, you´re a programming computer and that´s amazing!good luck and sucess in your journady!""") #3 aspas para colocar texto
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase)) #contar quantos caracteres tem a frase     
print(len(frase.strip)) #tira os espaços que tiver na string
print(frase.replace('Python', 'Andorid'))
print(frase[0])
#para receber a alteração deve se usar
frase = 'Curso em Video Python'
frase = frase.replace('Python','Andorid')
print(frase)
print('curso ' in frase)