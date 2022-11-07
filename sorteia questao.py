import random

def sorteia_questao(l_questoes, nivel):

    numero = random.randint(0, (len(l_questoes[str(nivel)])-1))

    questao = l_questoes[str(nivel)][numero]

    return questao
