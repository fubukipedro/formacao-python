# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {1, 2, 3, 3, 3, 3, 1}
print(s1) # {1, 2, 3}

l1 = [1, 2, 3, 3, 3, 3, 1]
sets = set(l1)
l1 = list(sets)
print(l1)

s2 = {1, 2, 50}
print(50 in s2)

for numero in s2:
    print(numero)