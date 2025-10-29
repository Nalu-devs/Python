# Peça três números e mostre o maior.
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))
num3 = float(input("Digite um numero: "))
if(num1>num2 and num1>num3):
    print(f"{num1} é o maior número")
elif(num2>num1 and num2>num3):
    print(f"{num2} é o maior número")
elif(num3>num1 and num3>num2):
    print(f"{num3} é o maior número")
else:
    print(f"Os números são iguais")