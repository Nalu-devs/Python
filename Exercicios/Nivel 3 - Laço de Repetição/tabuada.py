# Mostre a tabuada de um número.
n = int(input("Digite o numero da tabuada"))
for num in range(1, 11):
    resultado = n * num
    print(f"{n} x {num} = {resultado}")