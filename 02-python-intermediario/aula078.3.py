# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Pedro')
s1.add(1)
print(s1)

s1.update(('Olá mundo', 1, 2, 3, 4)) # Com o update da para enviar vários valores
print(s1)

# s1.clear()
# print(s1)

s1.discard('Olá mundo')
s1.discard(2)
print(s1)