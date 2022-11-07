def transforma_base(dicraw):
    dic = {}
    for i in dicraw:
        keys = dic.keys()
        dificuldade = i['nivel']
        if str(dificuldade) not in keys:
            dic[str(dificuldade)] = []
        dic[str(dificuldade)].append(i) 
    return dic