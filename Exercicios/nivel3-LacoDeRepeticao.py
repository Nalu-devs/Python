# Mostre todos os números de 1 a 100.
for numero in range(1, 101): 
    print(numero)

# Mostre todos os números pares de 1 a 100.
for num in range(2, 101, 2):
    print(num)

# Mostre a tabuada de um número.
n = int(input("Digite o numero da tabuada"))
for num in range(1, 11):
    resultado = n * num
    print(f"{n} x {num} = {resultado}")

# Some todos os números de 1 a 100.
soma = sum(range(1, 101))
print(soma)

# Conte quantos números pares existem entre 1 e 50.
cont=0 
for num in range(2, 51, 2):
    cont+=1
print(cont)

# Peça 10 números e mostre a média.
soma = 0
for num in range(1, 11):
    numero = float(input("Digite um numero: "))
    soma+=numero
media = soma/10
print(media)

# Peça números até digitar 0 e mostre a soma.
soma=0
while True:
    num = float(input("Digite um número ou 0 para sair"))
    soma+=num
    if num==0:
        break
print(soma)

# Peça uma senha até que o usuário acerte.
senha="Olá mundo!"
while True:
    tentativa = input("Digite uma senha e tente acertar: ")
    if tentativa==senha:
        break
print("Senha correta")

# Mostre os múltiplos de 3 entre 1 e 100.
for num in range(3, 101, 3):
    print(num)

# Calcule o fatorial de um número.
num = int(input("Digite um numero e daremos o fatorial"))
fatorial = 1
for i in range(num, num+1):
    fatorial*=i
print(fatorial;)