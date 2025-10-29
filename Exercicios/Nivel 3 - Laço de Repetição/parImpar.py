# Peça 10 números e, ao final, mostre a soma dos pares e a soma dos ímpares separadamente.
somaPar = 0
somaImpar = 0
for i in range (1, 11):
    num = int(input(f"Digite o {i}º número: "))
    if(num%2==0):
        somaPar+=num
    else:
        somaImpar+=num
print(f"A soma dos números impares é {somaImpar} e dos pares é {somaPar}")