# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

quantidade_acertos = 0
for questao in perguntas:
    print('Pergunta:', questao['Pergunta'])
    opcoes = questao['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    
    escolha = input('Escolha uma opção: ')
    escolha_int = None
    quantidade_opcoes = len(opcoes)
    quantidade_questoes = len(perguntas)
    acertou = False

    if escolha.isdigit(): # .isdigit() em Python é usado para verificar se todos os caracteres em uma string são dígitos numéricos
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < quantidade_opcoes:
            if opcoes[escolha_int] == questao['Resposta']:
                acertou = True
                quantidade_acertos += 1
    
    if acertou:
            print('Acertou 👍')
    else:
            print('Errou ❌')
    print()

print(f'Você acertou {quantidade_acertos} de {quantidade_questoes} perguntas.')