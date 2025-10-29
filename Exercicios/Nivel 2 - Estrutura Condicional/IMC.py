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