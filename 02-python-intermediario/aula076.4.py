# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2]
}

d2 = d1.copy()
d3 = copy.deepcopy(d1)
d2['c1'] = 100
d2['l1'][1] = 999
d3['l1'][1] = 777

print(d1)
print(d2)
print(d3)