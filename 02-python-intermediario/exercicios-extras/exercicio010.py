# Crie uma função executa(funcao, *args) que execute qualquer função com qualquer quantidade de argumentos

def executa(funcao, *args):
    return funcao(*args)

def soma(*args):
    return sum(args)

resultado = executa(soma, 10, 20, 30)
print(resultado)