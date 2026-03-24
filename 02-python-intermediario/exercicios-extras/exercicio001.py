# Crie uma função soma(*args) que receba vários números e retorne a soma deles.

# Jeito 1
def soma_manual(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = soma_manual(15, 20)
print(resultado)

# Jeito 2
def soma_python(*args):
    return sum(args)

resultado = soma_python(10, 10)
print(resultado)