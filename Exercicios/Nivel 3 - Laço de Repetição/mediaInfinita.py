# Peça notas até o usuário digitar um valor negativo. Mostre a média das notas válidas.
soma = 0
cont = 0
while True:
    notas=float(input("Digite as notas ou um valor negativo para gerar a media: "))
    if notas<0:
        break
    soma+=notas
    cont+=1
media=soma/cont
print(media)