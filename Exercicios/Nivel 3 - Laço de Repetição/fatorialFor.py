# Calcule o fatorial de um número.
num = int(input("Digite um numero e daremos o fatorial"))
fatorial = 1
for i in range(num, num+1):
    fatorial*=i
print(fatorial)