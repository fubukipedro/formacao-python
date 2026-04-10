# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

s1 = set() # set vazio
s1 = set('Pedro') 
s1 = {'Henrique', 1, 2, 3} # set com dados
print(s1, type(s1))

# Um set em Python é um tipo de dado que representa um conjunto — parecido com os conjuntos da matemática.

# Não permite valores repetidos
# Não tem ordem definida (os itens podem aparecer em qualquer ordem)
# É mutável (você pode adicionar ou remover elementos)