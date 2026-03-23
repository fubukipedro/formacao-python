# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

calculo = multiplicar(10, 5)
print(calculo)

#-#-#

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def ImparPar(n):
    multiplo_de_dois = n % 2 == 0
    
    if multiplo_de_dois:
        return f'O número {n} é par'
    return f'O número {n} é impar'

numero = input('Digite um número: ')
print(ImparPar(int(numero)))