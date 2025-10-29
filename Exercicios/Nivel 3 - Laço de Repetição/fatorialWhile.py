# Calcule o fatorial de um número usando while (não for).
num = int(input("Digite um numero e daremos o fatorial"))
fatorial = 1
while True:
    fatorial*=num
    num-=1
    if(num<1):
        break
print(fatorial)