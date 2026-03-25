# Crie uma função executa(funcao, valor) que execute a função recebida passando o valor.

def executa(funcao, valor):
    return funcao(valor)

def dobra(valor):
    return valor * 2

print(executa(dobra, 5))