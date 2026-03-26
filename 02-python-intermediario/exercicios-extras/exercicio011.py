# Crie uma função criar_operacao(operacao) que retorne:
# soma (se "soma")
# multiplicação (se "multiplica")

def criar_operacao(operacao):
    if operacao == 'soma':
        return soma
    elif operacao == 'multiplica':
        return multiplicacao

def soma(*args):
    return sum(args)
def multiplicacao(*args):
    calculo = 1
    for numeros in args:
        calculo *= numeros
    return calculo

somar = criar_operacao('soma')
multiplicar = criar_operacao('multiplica')
print(somar(10, 20))
print(multiplicar(5, 2))