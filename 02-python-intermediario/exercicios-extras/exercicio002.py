# Crie uma função media(*args) que calcule a média dos números recebidos.

# Jeito 1
def media(*args):
    if not args:
        raise ValueError('Você não digitou nenhum valor')
    total = 0
    contagem = 0
    for numero in args:
        total += numero
        contagem += 1
    return total / contagem

mediaFinal = media(100, 3, 56, 31)
print(mediaFinal)

# Jeito 2

def media(*args):
    if not args:
        raise ValueError('Você não digitou nenhum valor') 
    return sum(args) / len(args)

mediaFinal= media(100, 3, 56, 31)
print(mediaFinal)