frequencia = None # serve para determinar se o aluno está começando, terminando ou recomeçando o ciclo.
atual = 0 # serve para fazer a contagem dos dias e adicionar a frequencia que não é interger.
mCompletou = "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ" #mensagem após completar os 21 dias
mVoltou = "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO." # mensagem quando o aluno retorna após perder a contagem
mContando = "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO." # mensagem desde quando inicia até antes de terminar
ontem = 0 # serve para guardar o valor do dia anterior e comparar com o dia atual.

while True: # loop infinito para simular a passagem dos dias
    hoje = int(input('Dia de hoje na contagem: ')) # placeholder, em um cenário real, esse valor seria alimentado pelo dia atual no sistema da catraca. Para o funcionamento deste código sempre adicionar o valor do dia atual em comparação com o dia de inicio da contagem.
    
    match (frequencia):
        case "21": # quando o aluno completa os 21 dias
            print(mCompletou)
            frequencia = None
            atual = 0
            ontem = 0
            break
        case None: # quando o aluno inicia a contagem
            hoje += 1
            ontem = hoje - 1
            atual += 1
            frequencia = f"{atual}"
            print('DEBUG:', frequencia)
            print(mContando)
        case _ if hoje-ontem == 1: # A contagem sem faltas sempre resultará em hoje-ontem = 1
            ontem = hoje
            atual += 1
            frequencia = f"{atual}"
            print('DEBUG:', atual)
            print('DEBUG:', frequencia)
            print(mContando)
        case _ if hoje-ontem != 1: # quando o aluno falta sempre resultará em hoje-ontem diferente de 1, reiniciando a contagem.
            atual = 1
            frequencia = f"{atual}"
            print('DEBUG:', frequencia)
            ontem = hoje
            print(mVoltou)
        case _: # Nem tudo é perfeito, se existir um cenário que eu não previ, esse bloco captura o erro.
            print("Erro inesperado.")
            break


'''
Este desafio foi o mais difícil até agora, refiz com várias ideias diferentes. Inclusive usando um input para perguntar se o aluno veio ou não. Mas pensei melhor, no case afirmava ter uma catraca, o programa só será acionado caso o aluno passe a catraca.

Então, quando o aluno faltar, o sistema não computará falta.

A forma a qual optei, usei while true para simular a passagem dos dias, esse loop não faz parte do código, é apenas para entender como seria o funcionamento caso fosse usado continuamente.

Usei match case para as condições pois acho mais legível que if/elif/else. Mas a lógica é a mesma.
'''