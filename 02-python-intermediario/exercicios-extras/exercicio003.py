# Crie uma função contar_itens(*args) que retorne quantos elementos foram passados.

def contar_itens(*args):
    return len(args)

quantLista = contar_itens('Arroz', 'Feijão', 'Carne')
print(quantLista)