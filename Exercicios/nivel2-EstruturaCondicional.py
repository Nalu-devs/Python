# Verifique se um número é positivo, negativo ou zero.
num = float(input("Digite um número: "))
if(num>0):
    print(f"{num} é positivo")
elif(num<0):
    print(f"{num} é negativo")
else:
    print(f"{num} é zero")

# Verifique se um número é par ou ímpar.
num = int(input("Digite um número: "))
if(num%2==0):
    print(f"{num} é par")
else:
    print(f"{num} é impar")

# Peça duas notas e diga se o aluno foi aprovado (média ≥ 6).
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if(media>=6):
    print(f"Aluno aprovado média igual a: {media:.1f}")
else:
    print(f"Aluno reprovado média igual a: {media:.1f}")

# Verifique se um ano é bissexto.
ano = int(input("Digite o ano: "))
if((ano%4==0 and ano%100!=0) or (ano%400==0)):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")

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

# Peça três números e mostre o menor.
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))
num3 = float(input("Digite um numero: "))
if(num1<num2 and num1<num3):
    print(f"{num1} é o menor número")
elif(num2<num1 and num2<num3):
    print(f"{num2} é o menor número")
elif(num3<num1 and num3<num2):
    print(f"{num3} é o menor número")
else:
    print(f"Os números são iguais")

# Peça o sexo (M/F) e mostre uma mensagem diferente para cada caso
sexo = input("Digite F para feminino ou M para masculino: ")
if(sexo=="M" or sexo=="m"):
    print("Você se classifica como masculino")
elif(sexo=="F" or sexo=="f"):
    print("Você se classifica como feminino")
else:
    print("Você não digitou uma letra valida")

# Peça a idade e diga se é criança, adolescente, adulto ou idoso.
idade = int(input("Digite sua idade: "))
if(idade>=0 and idade<=11):
    print("Você é criança")
elif(idade>=12 and idade<=21):
    print("Você é adolescente")
elif(idade>=22 and idade<=60):
    print("Você é adulto")
else:
    print("Você é idoso")

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

# Calcule o valor do IMC e classifique (baixo peso, normal, sobrepeso, etc.).
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura*altura)
if(imc<=18.5):
    print("Baixo peso")
elif(imc>18.5 and imc<=24.9):
    print("Peso normal")
elif(imc>=25 and imc<29.9):
    print("Sobrepeso")
else:
    print("Obesidade")