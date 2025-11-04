# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input())
num2 = int(input())
num3 = int(input())

if(num1>num2 and num1>num3):
    print(f"{num1} é o maior numero")
elif(num2>num1 and num2>num3):
    print(f"{num2} é o maior numero")
elif(num3>num1 and num3>num2):
    print(f"{num3} é o maior numero")
else:
    print("Os numeros são iguais")