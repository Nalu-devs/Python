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