# Peça uma senha até que o usuário acerte.
senha="Olá mundo!"
while True:
    tentativa = input("Digite uma senha e tente acertar: ")
    if tentativa==senha:
        break
print("Senha correta")