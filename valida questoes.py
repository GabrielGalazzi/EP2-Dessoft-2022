def valida_questao(questao):
    analise = {}
    keys = ['titulo','nivel','opcoes','correta']
    niveis = ['facil','medio','dificil']
    letras = ['A','B','C','D']
    qkeys = questao.keys()
    for i in keys:
        if i not in qkeys:
            analise[str(i)] = 'nao_encontrado'
    if len(questao.keys()) != 4:
       analise['outro'] = 'numero_chaves_invalido'
    if 'titulo' in qkeys:
        caracteres = list(set(questao['titulo']))
        if questao['titulo'] == '' or ((' ' in caracteres or '\t' in caracteres)  and len(caracteres) < 3): 
            analise['titulo'] = 'vazio'
    if 'nivel' in qkeys:
        if questao['nivel'] not in niveis:
            analise['nivel'] ='valor_errado'
    if 'opcoes' in qkeys:
        alternativas = questao['opcoes'].keys()
        if len(alternativas) != 4:
            analise['opcoes'] = 'tamanho_invalido'
        elif len(alternativas) == 4:
            elementos = set(alternativas)
            certa = True
            for i in alternativas:
                if i not in letras or len(elementos) < 4:
                    analise['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    certa = False
            if certa == True and 'opcoes' in qkeys:
                analise["opcoes"] = {}
                nao_usou = True
                values = list(questao['opcoes'].values())
                print(values)
                for i in range(len(values)):
                    caracteres2 = list(set(values[i]))
                    if values[i] == '' or ((' ' in caracteres2 or '\t' in caracteres2)  and len(caracteres2) < 3):
                        analise['opcoes'][str(letras[i])] = 'vazia'
                        nao_usou = False
                if nao_usou:
                    analise.pop("opcoes")
    if 'correta' in qkeys:
        if questao['correta'] not in letras:
            analise['correta'] =  'valor_errado'
    return analise

def valida_questoes(l_questoes):
    l_resultados = []
    for i in l_questoes:
        resultado = valida_questao(i)
        l_resultados.append(resultado)

    return l_resultados

