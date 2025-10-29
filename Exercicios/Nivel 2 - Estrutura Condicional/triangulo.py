# Verifique se um triângulo é equilátero, isósceles ou escaleno.
lado1 = float(input("Digite um lado do triangulo: "))
lado2 = float(input("Digite outro lado do triangulo: "))
lado3 = float(input("Digite mais um lado do triangulo: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if(lado1==lado2==lado3):
        print("O trinagulo é equilatero")
    elif(lado1==lado2!=lado3 or lado1!=lado2==lado3 or lado1==lado3!=lado2):
        print("O triangulo é isosceles")
    else:
        print("O triangulo é escaleno")
else:
    print("Os valores não formam um triangulo")