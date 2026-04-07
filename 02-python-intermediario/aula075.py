# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_duplicar(numero):
    return numero * 2

def criar_triplicar(numero):
    return numero * 3

def criar_quadruplicar(numero):
    return numero * 4

duplicar = criar_duplicar(5) # 10
triplicar = criar_triplicar(10) # 30
quadruplicar = criar_quadruplicar(50) # 200

print(duplicar)
print(triplicar)
print(quadruplicar)

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5)) # 10
print(triplicar(10)) # 30
print(quadruplicar(50)) # 200