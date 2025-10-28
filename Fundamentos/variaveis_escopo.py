global_var = 10  # variável global

def funcao_exemplo():
    local_var = 5  # variável local
    print("Local:", local_var)
    print("Global dentro da função:", global_var)

funcao_exemplo()
print("Global fora da função:", global_var)