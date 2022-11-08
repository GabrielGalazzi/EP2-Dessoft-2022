import random

def gera_ajuda(questao):
    i = random.randint(0,1)
    nsorteio = i
    certa = questao['correta']
    letras = list(questao['opcoes'].keys())
    opcoes = list(questao['opcoes'].values())
    dicas = []
    while i < 2:
        alternativa = random.randint(0,3)
        if letras[alternativa] != certa and opcoes[alternativa] not in dicas:
            dicas.append(opcoes[alternativa])
            i += 1
        else:
            pass
    if nsorteio == 0:
        saida = 'DICA:\nOpções certamente erradas: {0} | {1}'.format(dicas[0],dicas[1])
    elif nsorteio == 1:
        saida = 'DICA:\nOpções certamente erradas: {0}'.format(dicas[0])
    return saida


