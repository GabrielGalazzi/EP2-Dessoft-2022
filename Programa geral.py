import random

from termcolor import colored

def transforma_base(dicraw):
    dic = {}
    for i in dicraw:
        keys = dic.keys()
        dificuldade = i['nivel']
        if str(dificuldade) not in keys:
            dic[str(dificuldade)] = []
        dic[str(dificuldade)].append(i) 
    return dic

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

def valida_questoes(banco):
    l_resultados = []
    for i in banco:
        resultado = valida_questao(i)
        l_resultados.append(resultado)

    return l_resultados

def sorteia_questao_inedita(banco,nivel,questoes_sorteadas):
    i = True
    while i == True:
        if len(banco[nivel]) == 0:
            print('fudeu.')
        numero = random.randint(0,(len(banco[nivel])-1))

        questao = banco[nivel][numero]
        if questao in questoes_sorteadas:
            pass
        else:
            questoes_sorteadas.append(questao)
            return questao
  
        

    return questao

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
        saida = colored('DICA:\nOp????es certamente erradas: {0} | {1}'.format(dicas[0],dicas[1]),'green')
    elif nsorteio == 1:
        saida = colored('DICA:\nOp????es certamente erradas: {0}'.format(dicas[0]))
    return saida

def questao_para_texto(questao,id):
    saida = '----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}\n'.format(id,questao['titulo'],questao['opcoes']['A'],questao['opcoes']['B'],questao['opcoes']['C'],questao['opcoes']['D'])
    return saida

def gera_nivel():
    niveis = ['facil','medio','dificil']
    if questoes < 4:
        return str(niveis[0])
    elif questoes >= 4 and questoes > 7:
        if questoes == 4:
            print(colored('HEY! Voc?? passou para o n??vel MEDIO!','green' ))
        return str(niveis[1])
    elif questoes >= 7:
        if questoes == 7 :  
            print(colored('HEY! Voc?? passou para o n??vel DIFICIL!','green' ))
        return str(niveis[2])

dicraw = [{'titulo': 'Qual o resultado da opera????o 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Bras??lia', 'B': 'Rio de janeiro', 'C': 'S??o Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando ?? o feriado da Independ??ncia do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ ?? um conjunto de particularidades que caracterizam um grupo de pessoas, uma fam??lia ou uma sociedade. ?? formada por princ??pios morais, h??bitos, costumes, hist??rias, manifesta????es religiosas, entre outros. Qual palavra melhor completa o in??cio da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miss??o', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culin??ria'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem rela????o com o fen??meno da globaliza????o?',
          'nivel': 'facil',
          'opcoes': {'A': 'Acultura????o', 'B': 'Neoliberalismo', 'C': 'Uni??o Europeia', 'D': 'Caldeir??o do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do anivers??rio da cidade de S??o Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Mar??o', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas n??o ?? uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Ma??a', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilh??o de usu??rios?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes n??o ?? um app com foco em streaming de v??deo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques n??o se localiza em S??o Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas n??o ?? uma linguagem de programa????o?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes ?? menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Nata????o', 'B': 'V??lei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da opera????o 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas ?? uma pseudoci??ncia que estuda os corpos celestes e as prov??veis rela????es que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'F??sica qu??ntica', 'C': 'Astrologia', 'D': 'Computa????o'},
          'correta': 'C'},

         {'titulo': 'Qual destas n??o foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois pr??mios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erd??s', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem ?? considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes n??meros ?? primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um n??mero natural inicial n, onde n > 0, os seguintes crit??rios ser??o obedecidos: Se n for par o seu sucessor ser?? a metade e se n for ??mpar o seu sucessor ser?? o triplo mais um, gerando ent??o um novo n??mero. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincar??', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como fa??o para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodu????o dos seres vivos ?? um processo biol??gico atrav??s do qual os organismos geram descend??ncia. Qual desta n??o ?? uma forma de reprodu????o assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporula????o', 'C': 'Partenog??nese', 'D': 'Divis??o bin??ria'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da opera????o 5 + 2 * 3 ^ 2, onde ^ representa potencia????o?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem ?? Ox??ssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Diss??labo', 'C': 'Divindade das religi??es africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de f??sica em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o n??mero at??mico do nitrog??nio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fus??o do nitrog??nio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120?? C', 'B': '15?? C', 'C': '-210?? C', 'D': '-180?? C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pel?? fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que ?? Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido org??nico'},
          'correta': 'D'},
        {'titulo': 'No jogo League of legends qual estrutura deve ser destruida para se ganhar o jogo?',
          'nivel': 'facil',
          'opcoes': {'A': 'dux', 'B': 'nexus', 'C': 'cristal', 'D': 'arcanum'},
          'correta': 'B'},
          {'titulo': 'Qual a diferen??a entre um camelo e um dromed??rio?',
          'nivel': 'medio',
          'opcoes': {'A': 'cor', 'B': 'cheiro', 'C': 'numero de corcovas', 'D': 'quem esta em cima dele'},
          'correta': 'C'},
          {'titulo': 'Qual jogo do genero FPS foi feito pela Riot Games?',
          'nivel': 'facil',
          'opcoes': {'A': 'Valorant', 'B': 'CS:GO', 'C': 'Call of duty', 'D': 'Halo'},
          'correta': 'A'},
          {'titulo': 'Oque define um diamante??',
          'nivel': 'facil',
          'opcoes': {'A': 'estrutura molecular', 'B': 'transparencia', 'C': 'sua dureza na escala mohs', 'D': 'a cor do seu brilho'},
          'correta': 'A'},
          {'titulo': 'Qual e a massa relativa a agua na massa do cerebro?',
          'nivel': 'dificil',
          'opcoes': {'A': '30%', 'B': '50%', 'C': '90%', 'D': '75%'},
          'correta': 'D'},
          {'titulo': 'Quantos japoneses(em milhares) habitam sao paulo(capital)?',
          'nivel': 'dificil',
          'opcoes': {'A': '500', 'B': '600', 'C': '450', 'D': '900'},
          'correta': 'B'},
          {'titulo': 'Quantas faixas a maior avenida do mundo possui?',
          'nivel': 'medio',
          'opcoes': {'A': '12', 'B': '16', 'C': '14', 'D': '20'},
          'correta': 'C'},
          {'titulo': 'Qual a populacao do vaticano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1200', 'B': '3000', 'C': '2400', 'D': '800'},
          'correta': 'D'},
          {'titulo': 'Qualndo inventaram a nutella?',
          'nivel': 'dificil',
          'opcoes': {'A': '1964', 'B': '1953', 'C': '1975', 'D': '1981'},
          'correta': 'A'},
          {'titulo': 'Em qual pais se encontra a famosa pintura mona lisa?',
          'nivel': 'facil',
          'opcoes': {'A': 'Alemanha', 'B': 'Sui??a', 'C': 'Fran??a', 'D': 'Italia'},
          'correta': 'C'},
          {'titulo': 'Onde inventaram o cachorro quente??',
          'nivel': 'facil',
          'opcoes': {'A': 'EUA', 'B': 'Alemanha', 'C': 'Inglaterra', 'D': 'Finlandia'},
          'correta': 'B'},
          {'titulo': 'Quantos ossos um esqueleto adulto possui?',
          'nivel': 'medio',
          'opcoes': {'A': '267', 'B': '270', 'C': '183', 'D': '206'},
          'correta': 'D'},
          {'titulo': 'Quanto tempo (minutos) a luz do sol leva para chegar a terra?',
          'nivel': 'dificil',
          'opcoes': {'A': '2', 'B': '6', 'C': '9', 'D': '8'},
          'correta': 'D'},
          {'titulo': 'Qual animal nao possui cordas vocais?',
          'nivel': 'medio',
          'opcoes': {'A': 'hipopotamo', 'B': 'girafa', 'C': 'foca', 'D': 'penguin'},
          'correta': 'B'},
          {'titulo': 'Qual a velociadade da luz(km/s)?',
          'nivel': 'facil',
          'opcoes': {'A': '500000', 'B': '300000', 'C': '100000', 'D': '250000'},
          'correta': 'B'},
          {'titulo': 'Qual a idade (em anos) do inventor da bandeira dos EUA',
          'nivel': 'dificil',
          'opcoes': {'A': '17', 'B': '61', 'C': '43', 'D': '26'},
          'correta': 'A'},
          {'titulo': 'Qual o musculo que nunca se cansa?',
          'nivel': 'facil',
          'opcoes': {'A': 'Biceps', 'B': 'Mandibula', 'C': 'Cora??ao', 'D': 'Quadriceps'},
          'correta': 'C'},
          {'titulo': 'Quanto de oxigenio (em %) disponivel nosso cerebro consume?',
          'nivel': 'medio',
          'opcoes': {'A': '30', 'B': '15', 'C': '25', 'D': '20'},
          'correta': 'D'},
          {'titulo': 'Qual o a linguagem de program????o do codigo fonte desse jogo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Julia', 'B': 'Brainfuck', 'C': 'Python', 'D': 'Ruby'},
          'correta': 'C'},
          {'titulo': 'Qual o elemento mais abundante do universo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Helio', 'B': 'Ouro', 'C': 'Hidrogenio', 'D': 'Argonio'},
          'correta': 'C'}
        ]

banco = transforma_base(dicraw)

premios = [0,1000.00,5000.00,10000.00,30000.00,50000.00,100000.00,300000.00,500000.00,1000000.00]
respostasvalidas= ["A", "B", "C", "D", "ajuda", "pula" , "parar"]
letras = ["A", "B", "C", "D"]
game = True

while game != False:
    questoes_sorteadas = []
    pular = 3
    ajuda = 2
    questoes = 1
    erros = 0
    desistiu = 'n'
    print(colored('Ol??! Voc?? esta na Fortuna DesSoft e ter?? a oportunidade de enriquecer!', 'magenta'))
    nome = str.upper(input('Qual seu nome? '))

    print('Ok {}, voc?? tem direito a pular 3 vezes e 2 ajudas! '.format(nome))
    print(colored('As op????es de resposta s??o "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n', 'cyan'))

    input('Aperte ENTER para continuar...\n')

    print('O jogo j?? vai come??ar! L?? vem a primeira quest??o!\n')
    
    print('Vamos come??ar com quest??es do n??vel FACIL!')
    input('Aperte ENTER para continuar...')
    while questoes < 10 and erros <= 0 and desistiu == 'n':
        natureza = 'invalida'
        antirepeteco = 'n'
        questaosorteada = sorteia_questao_inedita(banco,gera_nivel(),questoes_sorteadas)

        print(questao_para_texto(questaosorteada,questoes))

       
        print('\n')
        while natureza != 'valida':
            resposta = str(input('Qual sua resposta?! '))

            if resposta not in respostasvalidas:
                print(colored('Op????o Inv??lida!', 'red'))
                print(colored('As op????es de resposta s??o "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n', 'cyan'))
            elif resposta in letras:
                if resposta == questaosorteada['correta']:
                    questoes += 1
                    questoes_sorteadas.append(questaosorteada)
                    print(colored('Voc?? acertou! Seu pr??mio atual ?? de R$ {}'.format(premios[questoes]), 'cyan'))                                
                    input('Aperte ENTER para continuar...\n\n')
                else:
                    erros +=1
                natureza = 'valida'
            elif resposta == 'ajuda':
                if ajuda > 0:
                    ajuda -=1
                    antirepeteco = 's'
                    print('Ok, l?? vem ajuda! Voc?? ainda tem {} ajudas!\n'.format(ajuda))
                    input('Aperte ENTER para continuar...')
                    print(gera_ajuda(questaosorteada))
                    input('Aperte ENTER para continuar...\n\n')
                    print('\n')
                    while natureza != 'valida':
                        resposta = str(input('Qual sua resposta?! '))

                        if resposta not in respostasvalidas:
                            print(colored('Op????o Inv??lida!', 'red'))
                            print(colored('As op????es de resposta s??o "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n', 'cyan'))
                        elif resposta in letras:
                            if resposta == questaosorteada['correta']:
                                questoes += 1
                                questoes_sorteadas.append(questaosorteada)
                                print(colored('Voc?? acertou! Seu pr??mio atual ?? de R$ {}'.format(premios[questoes]), 'cyan'))                                
                                input('Aperte ENTER para continuar...\n\n')
                            else:
                                erros +=1
                            natureza = 'valida'
                        elif resposta == 'ajuda':
                            print(colored('N??o deu! Voc?? j?? pediu ajuda nesta quest??o!','red'))
                                    
                        elif resposta == 'pula':
                            if pular > 0:
                                pular -= 1
                                if pular >= 1:
                                    natureza = 'valida'
                                    print('Ok, pulando! Voc?? ainda tem {} pulos!'.format(pular))
                                else: 
                                    print('Ok, pulando! ATEN????O: Voc?? n??o tem mais direito a pulos!')
                                questoes_sorteadas.append(questaosorteada)
                            else:
                                    print('N??o deu! Voc?? n??o tem mais direito a pulos!')
                        elif resposta == 'parar':
                            escolha =  str(input('Deseja mesmo parar [S/N]?? Caso responda "S", sair?? com R$ {}!'.format(premios[questoes])))
                            if escolha == 'S':
                                print('Ok! Voc?? parou e seu pr??mio ?? de R$ {}'.format(premios[questoes-1]))
                                natureza = 'valida'
                                desistiu = 's'
                            else:
                                pass        
                else:
                    print(colored('N??o deu! Voc?? n??o tem mais direito a ajuda!','red'))              
            elif resposta == 'pula':
                if pular > 0:
                    pular -= 1
                    if pular >= 1:
                        natureza = 'valida'
                        print('Ok, pulando! Voc?? ainda tem {} pulos!'.format(pular))
                    else: 
                        natureza = 'valida'
                        print('Ok, pulando! ATEN????O: Voc?? n??o tem mais direito a pulos!')
                    questoes_sorteadas.append(questaosorteada)
                else:
                        print('N??o deu! Voc?? n??o tem mais direito a pulos!')
            elif resposta == 'parar':
                escolha =  str(input('Deseja mesmo parar [S/N]?? Caso responda "S", sair?? com R$ {}!'.format(premios[questoes])))
                if escolha == 'S':
                    print('Ok! Voc?? parou e seu pr??mio ?? de R$ {}'.format(premios[questoes-1]))
                    natureza = 'valida'
                    desistiu = 's'
                else:
                    pass
    if questoes == 10:
        
        print(colored('PARAB??NS, voc?? zerou o jogo e ganhou um milh??o de reais!','green'))
        vontade = str(input('Deseja jogar novamente?[S/N] '))
        if vontade in ['s','S']:
            pass
        elif vontade in ['n','N']:
            game = False
    elif erros > 0:
        print(colored('Que pena! Voc?? errou e vai sair sem nada :(','yellow'))
        vontade = str(input('Deseja jogar novamente?[S/N] '))
        if vontade in ['s','S']:
            pass
        elif vontade in ['n','N']:
            game = False
    elif desistiu == 's':
        vontade = str(input('Deseja jogar novamente?[S/N] '))
        if vontade in ['s','S']:
            pass
        elif vontade in ['n','N']:
            game = False
        