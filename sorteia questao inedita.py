import random

def sorteia_questao_inedita(l_questoes, nivel,l_repetidas):
    i = True
    while i == True:
        numero = random.randint(0, (len(l_questoes[str(nivel)])-1))

        questao = l_questoes[str(nivel)][numero]
        if questao in l_repetidas:
            pass
        else:
            l_repetidas.append(questao)
            i = False
        

    return questao
