# Peça duas notas e diga se o aluno foi aprovado (média ≥ 6).
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if(media>=6):
    print(f"Aluno aprovado média igual a: {media:.1f}")
else:
    print(f"Aluno reprovado média igual a: {media:.1f}")