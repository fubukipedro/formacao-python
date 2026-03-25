# Crie uma função criar_saudacao(msg) que retorne uma função que recebe um nome e retorna uma saudação.

def criar_saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}'
    return saudar
    
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_tarde = criar_saudacao('Boa tarde')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Pedro'))