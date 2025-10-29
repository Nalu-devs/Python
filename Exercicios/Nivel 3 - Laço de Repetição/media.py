# Peça 10 números e mostre a média.
soma = 0
for num in range(1, 11):
    numero = float(input("Digite um numero: "))
    soma+=numero
media = soma/10
print(media)