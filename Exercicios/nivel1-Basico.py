# Peça o nome do usuário e exiba uma saudação.
nome = input("Digite seu nome: ")
print("Bem vindo ", nome)

# Peça dois números e exiba a soma.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(f"A soma do número {num1} mais {num2} é: ", num1+num2)

# Peça dois números e exiba a média.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(f"A média de {num1} com {num2} é: ", (num1+num2)/2)

# Calcule o dobro, triplo e raiz quadrada de um número.
num = int(input("Digite um número: "))
dobro = num*2
triplo = num*3
raiz = num**0.5
print(f"Número {num}: \nDobro {dobro} \nTriplo {triplo} \nRaiz {raiz}")

# Converta metros em centímetros e milímetros.
metro = float(input("Digite o valor em metro: "))
cm = metro*100
mm = metro*1000
print(f"Centimetro: {cm} \nMilimetro {mm}")

# Calcule a área de um quadrado e mostre o dobro dessa área.
lado = float(input("Digite o lado de um quadrado: "))
area = lado*lado
da = area*2
print(f"O dobro da area é igual a {da}")

# Converta temperatura de °C para °F.
c = float(input("Digite a temperatura em Cº"))
f = (c*1.8)+32
print(f"A temperatura em ºF é {f}")

# Calcule o salário mensal multiplicando horas trabalhadas por valor da hora.
ht = float(input("Digite quantas horas você trabalha: "))
vh = float(input("Digite o valor da hora trabalhada: "))
salMensal = ht*vh
print(f"Seu salario mensal é de: {salMensal:.2f}")

# Peça um número e mostre o antecessor e o sucessor.
num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1
print(f"O antecessor de {num} é: {ant} \nO sucessor de {num} é: {suc}")

#Peça o nome e idade e exiba “Fulano tem X anos”.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"{nome} tem {idade} anos")