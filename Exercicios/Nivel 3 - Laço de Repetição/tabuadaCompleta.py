# Mostre a tabuada de todos os números de 1 a 10.
for i in range(1, 11):
    for j in range(1, 11):
        resultado = i*j
        print(f"{i} x {j} = {resultado}")
    print()