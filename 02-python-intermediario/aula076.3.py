# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome' : 'Pedro',
    'sobrenome' : 'Henrique'
}
pessoa.setdefault('idade', 0)

print(pessoa['idade'])
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for valor in pessoa.values():
    print(valor)

for chave, valor2 in pessoa.items():
    print(chave, valor2)