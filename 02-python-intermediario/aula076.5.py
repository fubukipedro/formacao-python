# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del) (porém você pode armazenar o valor antes de deletar)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome' : 'Pedro',
    'sobrenome' : 'Henrique'
}

print(p1['nome'])
print(p1.get('nome', 'Nome não existe'))

# nome = p1.pop('nome')
# print(nome)
print(p1)


# ultima_chave = p1.popitem()
# print(ultima_chave)

p1.update({
    'nome' : 'Maria',
    'idade' : 18
})
print(p1)

p1.update(nome='Pandinha', idade=10)
print(p1)

tupla = (('nome', 'novo valor'), ('sobrenome', 'outro valor'), ('idade', None))
lista = [['nome', 'novo valor'], ['sobrenome', 'outro valor'], ['idade', None]]
p1.update(tupla)
print(p1)
p1.update(lista)
print(p1)