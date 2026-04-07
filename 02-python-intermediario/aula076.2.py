# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'
pessoa[chave] = 'Pedro Henrique'
pessoa['sobrenome'] = 'Panda'

print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Maria Julia'
print(pessoa[chave])

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('A chave não existe.')
else: 
    print('A chave existe:', pessoa['sobrenome'])