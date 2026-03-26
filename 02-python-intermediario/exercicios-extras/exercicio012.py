# Crie uma função criar_formatador(prefixo, sufixo) que retorne uma função que formata textos assim:
# *prefixo + texto + sufixo*

def criar_formatador(prefixo, sufixo):
    def formatador(texto):
        return f'{prefixo}{texto}{sufixo}'
    return formatador

texto_formatado = criar_formatador('>>>', '<<<')
print(texto_formatado('Pedro'))

'''
1. criar_formatador é chamada com prefixo e sufixo
2. Ela cria a função formatador
3. formatador "lembra" prefixo e sufixo (closure)
4. criar_formatador retorna a função formatador
5. texto_formatado agora é essa função
6. quando chamamos texto_formatado('Pedro'), executamos formatador
7. ela usa prefixo + texto + sufixo e retorna o resultado
'''