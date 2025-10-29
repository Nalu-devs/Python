# Peça o sexo (M/F) e mostre uma mensagem diferente para cada caso
sexo = input("Digite F para feminino ou M para masculino: ")
if(sexo=="M" or sexo=="m"):
    print("Você se classifica como masculino")
elif(sexo=="F" or sexo=="f"):
    print("Você se classifica como feminino")
else:
    print("Você não digitou uma letra valida")