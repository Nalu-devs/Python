# Peça números até digitar 0 e mostre a soma.
soma=0
while True:
    num = float(input("Digite um número ou 0 para sair"))
    soma+=num
    if num==0:
        break
print(soma)