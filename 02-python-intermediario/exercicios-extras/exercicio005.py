# Crie uma função aplicar(funcao, lista) que aplique a função em cada elemento da lista e retorne uma nova lista.

def aplicar(funcao, lista):
    nova_lista = []

    for item in lista:
        nova_lista.append(funcao(item))
    return nova_lista

def dobra(lista):
    return lista * 2
    

resultado = aplicar(dobra, [1, 2, 3])
print(resultado)