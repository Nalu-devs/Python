# Peça um número e mostre a contagem regressiva até 0.
num = int(input("Digite um número para iniciar a contagem: "))
for i in range(num, -1, -1):
    print(i)