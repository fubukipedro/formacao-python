# Crie uma função **criar_multiplicador(n)** que retorne uma função que multiplica qualquer número por n.

def criar_multiplicador(n):

    def numero(x):
        return x * n
    return numero

x2 = criar_multiplicador(2)
x3 = criar_multiplicador(3)

print(x2(5))
print(x3(2))