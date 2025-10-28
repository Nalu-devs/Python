# Tipos básicos
inteiro = 10
real = 3.14
texto = "Python"
booleano = True

# Conversões de tipo
num_str = "25"
num_int = int(num_str)  # converte string para inteiro
num_float = float(num_int)

print(type(num_int), num_int)
print(type(num_float), num_float)

# Operações com diferentes tipos
soma = inteiro + num_float
print("Resultado da soma:", soma)