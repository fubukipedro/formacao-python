# Crie duas funções:
# dobro(x)
# triplo(x)
# Depois use executa para testar ambas.

def executa(funcao, valor):
    return funcao(valor)

def dobro(valor):
    return valor * 2

def triplo(valor):
    return valor * 3

for funcao in ([dobro, triplo]):
    print(executa(funcao, 5))