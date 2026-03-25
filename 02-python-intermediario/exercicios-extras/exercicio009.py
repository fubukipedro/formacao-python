# Crie uma função criar_desconto(porcentagem) que retorne uma função que aplica desconto em um valor.

def criar_desconto(porcentagem):
    def valor(numero):
        valorDescontado = numero * (porcentagem / 100)
        valorFinal = numero - valorDescontado
        return valorFinal
    return valor

porcentagemDesconto = input('Qual a porcentagem de desconto?: ')
valorDesconto = input('Qual o valor?: ')

desconto = criar_desconto(float(porcentagemDesconto))
resultado = desconto(float(valorDesconto))
print(f'O valor final é: R${resultado:.2f}')

'''def criar_desconto(porcentagem):
    def valor(numero):
        valorDescontado = numero * (porcentagem / 100)
        valorFinal = numero - valorDescontado
        return print(f'R${numero:.2f} com {porcentagem}% de desconto fica R${valorFinal:.2f} e teve R${valorDescontado:.2f} de desconto.')
    return valor

porcentagemDesconto = input('Qual a porcentagem de desconto?: ')
valorDesconto = input('Qual o valor?: ')

desconto = criar_desconto(int(porcentagemDesconto))
desconto(int(valorDesconto))'''