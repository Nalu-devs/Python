# Peça 5 números e mostre qual foi o maior e o menor digitado.
menor = 0
maior = 0
for i in range(1, 6):
    num = int(input(f"Digite o {i}º número"))
    if(i==1):
        maior=num
        menor=num
    if(num>maior):
        maior=num
    if(num<menor):
        menor=num

print(f"O menor numero digitado foi {menor} e o maior numero digitado foi {maior}")