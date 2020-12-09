import random as rd
import Batalha as bt

def chance(x,y):
    '''
    Função para gerar um número aleatório dentro de em intervalo pré-determinado
    '''
    return rd.randint(x,y)


def floresta(jogador):
  
    '''
    Essa função defini o labirnto na floresta, nele há caminhos sem saída, eventos aleatórios e uma batalha
  
    Para sair da floresta é preciso seguir as placas com as cores mais frias
    Resposta: 1,1,2,1,2,1,1,1
    Eventos extras:  - batalha: 105
                   - cabana com possibilidade de arma: sala 113
                   - possiveis eventos: 110 e 117
                   - poção para passar de nível: 120
    '''
  
    #variaveis
    sala = 101 #localização do personagem na floresta
    saida = 0
    primeira_vez = True # se o jogador já tiver passado por esse caminho ele não luta novamente com o urso na sala 105

    print('Seguindo a trilha você se depara com a floresta e suas imponentes árvores que escondem a fauna da luz do sol.')
    bt.enter()
    print('Continuando sua caminhada você sente a umidade, acompanhada de um cheiro característico e do zumbido de insetos.')
    bt.enter()
  
    while sala != saida:
    
        if sala == 101:
            print('Com poucos minutos de caminhada, já imcapacitado de ver o sol, você se depara com uma encruzilhada.')
            bt.enter()
            print('Indicando o caminho para direita há uma placa verde, equanto para a esquerda há uma placa amarela.')
            bt.enter()
            print('\u001b[37;1mAssim você decidi ir para: \n (1) direita  \n (2) esquerda')
            dir = input('>>>') #jogador escolhe caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # virar direita
            if dir == "1": 
                sala = 104
            # virar esqueda
            elif dir == "2": 
                sala = 102
            #erro
            else:
                print ('\u001b[37;1mAssim você decidi ir para: \n (1) direita  \n (2) esquerda') 
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

        
        elif sala == 102: 
            print ('Durante a caminhada você escuta o barulho de galhos se quebrando, mas devido a escuridão não é possível ver o responsável pelo som.')
            bt.enter()
            print ('\u001b[37;1mDessa forma você decidi: \n (1) seguir em frente \n (2) voltar para a encruzilhada')
            dir = input('>>>')#jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # seguir em frente
            if dir == "1": 
                sala =103 
            #voltar para sala anterior
            if dir == "2": 
                sala = 101
            #erro
            else: 
                print ('\u001b[37;1mDessa forma você decidi: \n (1) seguir em frente \n (2) voltar para a encruzilhada')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 103: #sala sem saida
            print ('Após horas caminhando você vê a trilha chegar ao fim, mas sem sinal da saída.') 
            bt.enter()
            print ('\u001b[37;1mFrustado você decidi: \n (1) voltar') 
            dir = input('>>>') 
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # voltar para sala anterior
            if dir == "1": 
                sala = 102
            #erro
            else:
                print ('\u001b[37;1mFrustado você decidi: \n (1) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 104:
            print ('Continuando seu caminho pela trilha, você se depara com duas possibildades: continuar em frente, como indica a placa azul, ou virar a direita na placa laranja.')
            bt.enter()
            print ('\u001b[37;1mDiante de tais possibilidades você escolhe: \n (1) seguir em frente  \n (2) virar a direita \n (3) voltar')
            dir = input('>>>') #jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # seguir em frente
            if dir == "1": 
                sala = 107
            #virar a direita
            elif dir == "2": 
                sala= 105
            #voltar
            elif dir == "3": 
                sala = 101
            #erro
            else:
                print ('\u001b[37;1mDiante de tais possibilidades você escolhe: \n (1) seguir em frente  \n (2) virar a direita \n (3) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

        
        elif sala == 105:
            #batalha com um urso
            if primeira_vez == True: 
                print('Enquanto você caminhava, você se depara com um urso.')
                #inimigo
                Urso = {"nome": "Urso", 'hp': 45,  'defesa': 3, 'força': 3}
                #chama a função batalha do módulo batalha
                bt.batalha(Urso,jogador)
            #encrusilhada
            print ('\u001b[37;1mApós o encontro com o urso você deicidi: \n (1) seguir em frente \n (2) voltar para encrusilhada')
            dir = input('>>>') #jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #seguir em frente
            if dir == "1": 
                sala = 106
                primeira_vez == False
            # voltar
            elif dir == "2": 
                sala= 104
                primeira_vez == False
            #erro
            else:
                print ('\u001b[37;1mApós o encontro com o urso você deicidi: \n (1) seguir em frente \n (2) voltar para encrusilhada')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

        
        elif sala == 106: #sala sem saida
            print ('Seguindo a trilha você se depara com uma caverna.')
            bt.enter()
            print('\u001b[37;1mCom isso você decidi: \n (1) entrar na caverna \n (2) voltar')
            dir = input('>>>')#jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #entrar na caverna
            if dir == "1": 
                print('Ao entara na caverna, após se acostumar com o escuro, você repara nos restos de um amontoado de lenha.')
                bt.enter()
                print('Contudo, ao se aproximar, você consta que há muito tempo não ela é acesa.')
                bt.enter()
                print('Não vendo nada mais de interessante, você decidi voltar.')
                bt.enter
                sala == 105 #volta para a sala anterior
            #voltar  
            elif dir == "2":  
                sala = 105
            #erro
            else:
                print ('\u001b[37;1mCom isso você decidi: \n (1) entrar na caverna \n (2) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 107:
            print ('Após um longo caminho, novamente você se depara com duas placas: uma para frente e outra para a direita.')
            bt.enter()
            print('A placa que aponta para a direita é de cor alaranjada, enquanto a para frente é arroxeada.')
            bt.enter()
            print ('\u001b[37;1mE assim você segue seu caminho: \n (1) pela direita \n (2) em frente \n (3) voltar')
            dir = input('>>>') #jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # ir pela direita
            if dir == "1": 
                sala = 108
            # seguir em frente  
            elif dir == "2":  
                sala= 110
            #voltar
            elif dir == "3": 
                sala = 104
            #erro
            else:
                print ('\u001b[37;1mE assim você segue seu caminho: \n (1) pela direita \n (2) em frente \n (3) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 108:
            print ('Enquanto caminhava pela floresta você repentinamente escuta um grunido a sua esquerda.')
            bt.enter()
            print ('\u001b[37;1mDessa forma você decid: \n (1) seguir em frente \n (2) voltar')
            dir = input('>>>') #jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #frente
            if dir == "1":  
                sala = 109
            #voltar  
            elif dir == "2": 
                sala= 107
            #erro
            else:
                print ('\u001b[37;1mDessa forma você decid: \n (1) seguir em frente \n (2) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

   
        elif sala == 109: #sala sem saida
            print ('Depois de uma longa caminhada, você percebe que chegou ao fim da trilha, mas sem sinal da saida desse labirinto. ') 
            bt.enter()
            print ('\u001b[37;1mCom isso você decidi: \n (1) voltar') 
            dir = input('>>>') #jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #voltar
            if dir == "1": 
                sala = 108
            #erro
            else:
                print ('\u001b[37;1mCom isso você decidi: \n (1) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 110:
            #Chance de árvore caida no caminho
            prob = chance(1,15)
            if prob <= 6:
                print('Enquanto caminhava pela trilha, você se depara com um uma árvore caida bloquando seu caminho.')
                bt.enter()
                print('\u001b[37;1mVendo isso você decidi: \n (1) empurrar a árvore caida \n (2) pular por cima da árvore caida')
                escolha = input('>>>') #jogador escolhe como passar pelo obstáculo
                bt.delete_last_lines(1)
                print(f">>>{escolha}\u001b[0m\n")

                #usar força para empurrar a árvore
                if escolha == "1":
                    forca = chance(1,16) + jogador['força']
                    #força suficiente para empurrar
                    if forca >= 10:
                        print('Você consegiui empurrar a árvore e contina seu caminho')
                        #força insuficinete para empurrar
                    else:
                        print('Enquanto tentava empurrar a árvore caida, você acaba se machucando')
                        jogador['hp'] -= 5 #jogador se machuca e perde vida
                        bt.game_over(jogador) #confirmar que o hp do jogador é maior que zero
                #usar destreza para pular a árvore
                elif escolha == "2":
                    des = chance(1,16) + jogador['destreza']
                    #destreza suficiente para pular a árvore
                    if des >= 10:
                        print('Você consegiui pular a árvore e contina seu caminho')
                    #destreza insuficiente para pular a árvore
                    else:
                        print('Após pular a árvore, ao aterrissar você acaba caindo e torcendo o tornozelo')
                        jogador['hp'] -= 5 #jogador se machuca e perde vida
                        bt.game_over(jogador) #confirmar que o hp do jogador é maior que zero
                #erro
                else:
                    print('\u001b[37;1mVendo isso você decidi: \n (1) empurrar a árvore caida \n (2) pular por cima da árvore caida')
                    escolha = input('>>>')
                    bt.delete_last_lines(1)
                    print(f">>>{escolha}\u001b[0m\n")

            #encrusilhada
            print ('Andando mais um pouco você se depara com outra encruzilhada.')
            bt.enter()
            print('O caminho para direita é indicado por uma placa amarelo, enquanto o caminho para a esquerda é indicado por uma placa laranja')
            bt.enter()
            print('\u001b[37;1mAssim você decidi ir pra: \n (1) direita  \n (2) esquerda \n (3) voltar')
            dir = input('>>>') #jogador escolhe o caminho
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # ir pela direita
            if dir == "1": 
                sala = 115
            #esquerda  
            elif dir == "2": 
                sala= 111
            #voltar  
            elif dir == "3": 
                sala = 107
            #erro
            else:
                print ('\u001b[37;1mAssim você decidi ir pra: \n (1) direita  \n (2) esquerda \n (3) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

   
        elif sala == 111:
            print ('Seguindo em frente você se depara com uma nova bifurcação. Há uma placa roxa indicando o caminho a esquerda e uma placa vermelha apontando para o caminho a sua frente.')
            bt.enter()
            print ('\u001b[37;1mVocê decidi seguir a placa que aponta para: \n (1) frente  \n (2) esquerda \n (3) voltar')
            dir = input('>>>') #jogador escolhe o caminho a seguir
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # em frente
            if dir == "1": 
                sala = 112
            # virar esquerda
            elif dir == "2": 
                sala= 113
            #voltar  
            elif dir == "3": 
                sala = 110
            #erro
            else:
                print ('\u001b[37;1mVocê decidi seguir a placa que aponta para: \n (1) frente  \n (2) esquerda \n (3) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 112: #sala sem saida
            print ('Continuando sua caminhada, você chega ao final da trilha, sem chegar do outro lado da floresta.')
            bt.enter()
            print ('\u001b[37;1mAssim você decidi: \n (1) voltar')
            dir = input('>>>') #escolha do jogador
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #voltar
            if dir == "1": 
                sala = 111
            #erro
            else:
                print ('\u001b[37;1mAssim você decidi: \n (1) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 113: #sem saida
            #cabana com chance de arma
            print('Ao continuar dua caminhada você se depara com o final da trilha, mas sem sinal da saida.')
            bt.enter()
            print('Contudo você observa uma pequna cabana de madeira.')
            bt.enter()
            print('\u001b[37;1mVocê decidi: \n (1) Entrar na cabana \n (2) Voltar')
            dir = input('>>>') #jogador escolhe entrar na cabana ou não
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #entrar na cabana
            if dir == "1":
                print('A medida que se aproxima da cabana, você percebe como ela está mal cuidada, provavelmente abandonada aalguns anos.')
                bt.enter()
                print('Você caminha em direção a cabana e abre a porta com cuidado, escutando o rangir da porta.')
                bt.enter()
                #explorando a cabana
                escolha = 0
                while escolha != "4": 
                    print('Ao entrar você percebe é capaz de enxergar uma mesa no centro do comodo, um suporte de madeira onde deveria ser a cama e um armário ao lado de uma janela.')
                    print('\u001b[37;1mAssim você decidi: \n (1) Olhar a mesa \n (2) Se aproximar da cama \n (3) Ir até o armário \n (4) Voltar')
                    escolha = input('>>>') #jogador escolhe para onde ir
                    bt.delete_last_lines(1)
                    print(f">>>{escolha}\u001b[0m\n")

                    prob = chance(1,21) #chance de encontrar uma arma
                    #mesa
                    if escolha == "1": 
                        if prob <=5:
                            print('\u001b[37;1mAo se aproximar da mesa, você encontra uma adaga. Você quer pegas a arma?.\n (1) sim\n (2) não')
                            pegar = input('>>>') #jogador escolhe se quer equipar a arma ou não
                            bt.delete_last_lines(1)
                            print(f">>>{pegar}\u001b[0m\n")

                            #jogador pega a arma
                            if pegar == "1": 
                                print('Sem saber o que lhe aguarda pela fente, você decidi pegar a adaga. Isso faz com que você se sinta mais seguro.')
                                jogador['arma'] = 'adaga'
                                bt.enter()
                            #jogador não pega a arma
                            elif pegar == "2": 
                                print('Você olha a arma e decidi que é melhor não pega-la')
                                bt.enter()
                            #erro
                            else: 
                                print('Ao se aproximar da mesa, você encontra uma adaga. Você quer pegas a arma?.\n1.sim\n2.não') 
                        else:
                            print('Você se aproxima da mesa vendo nada além de poeira em cima dela.')
                            bt.enter()
                    #cama
                    elif escolha == "2": 
                        if prob <=10 and prob >=6:
                            print('Ao aproximar do suporte de madeira epercebe algo brilhando no chão.')
                            bt.enter()
                            print('\u001b[37;1mVocê se abaixa e pega, percebendo que se trata de uma adaga. Você quer pegar a arma:\n (1) sim\n (2) não')
                            pegar = input('>>>') #jogador escolhe se pega ou não a arma
                            bt.delete_last_lines(1)
                            print(f">>>{pegar}\u001b[0m\n")

                            #jogador pega a arma
                            if pegar == "1":
                                print('Incerto sobre o que lhe aguarde, você decidi pegar a adaga.')
                                jogador['arma'] = 'adaga'
                                bt.enter()
                            #jogador não pega a arma
                            elif pegar == "2": 
                                print('Você acaba achando que não seria uma boa ideia pegar a arma e deixa-a no lugar em que encontrou.')
                            #erro
                            else:
                                print('\u001b[37;1mVocê se abaixa e pega, percebendo que se trata de uma adaga. Você quer pegar a arma:\n (1) sim\n (2) não')
                                pegar = input('>>>')
                                bt.delete_last_lines(1)
                                print(f">>>{pegar}\u001b[0m\n")

                        else:
                            print('Você se aproxima do suporte de madeira e olha ao redor dele, mas não encontra nada.')
                            bt.enter()
                    #armário
                    elif escolha == "3": 
                        if prob <= 15 and prob >= 11:
                            print('\u001b[37;1mVocê anda até o armário e o abre, e para sua surpresa você encontra uma única adaga. Você quer pegar a arma:\n (1) sim\n (2) não')
                            pegar=input('>>>')
                            bt.delete_last_lines(1)
                            print(f">>>{pegar}\u001b[0m\n")

                            #jogador pega a arma
                            if pegar == "1":
                                print('Não sabendo o que vem pela frente, você decidi pegar a adaga para poder se proteger melhor.')
                                jogador['arma'] = 'adaga'
                                bt.enter()
                            #jogador não pega a arma
                            elif pegar == "2":
                                print('Você observa a adaga, mas decidi não pegar.')
                                bt.enter()
                            #erro
                            else:
                                print('\u001b[37;1mVocê anda até o armário e o abre, e para sua surpresa você encontra uma única adaga. Você quer pegar a arma:\n (1) sim\n (2) não')
                                pegar = input('>>>')
                                bt.delete_last_lines(1)
                                print(f">>>{pegar}\u001b[0m\n")

                        else:
                            print('Você vai até o armário na esperança de encontrar algo, mas ao abri-lo você nã encontra nada.')
                            bt.enter()
                    # erro
                    elif escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4": 
                        print('\u001b[37;1mAssim você decidi: \n (1) Olhar a mesa \n (2) Se aproximar da cama \n (3) Ir até o armário \n (4) Voltar')
                        escolha = input('>>>')
                        bt.delete_last_lines(1)
                        print(f">>>{escolha}\u001b[0m\n")

                    print('Depois de explorar a cabana, você decidi sair e voltar pelo caminho que veio.')
                    bt.enter()
                    sala = 111
                #voltar
            elif dir == '2':
                sala = 111  
            #erro
            else: 
                print('\u001b[37;1mVocê decidi: \n (1) Entrar na cabana \n (2) Voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

        
        elif sala == 114: #sem saida
            print ('Continuando pela trilha, você chega ao fim, mas sem conseguir chegar ao fim da floresta.')
            bt.enter()
            print ('\u001b[37;1mAssim só lhe resta: \n (1) voltar')
            dir = input('>>>') #escolha do jogador
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #voltar
            if dir == '1': 
                sala = 115
            #erro
            else:
                print ('\u001b[37;1mAssim só lhe resta: \n (1) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 115:
            print('Andando pela trilha, mais uma vez você se depara com a possibilidade de escolher entre dois caminhos.')
            bt.enter()
            print('A primeira possibilidade é seguir a direita, indicada por uma placa verde. A outra possibilidade é seguir para a esquerda, indidcado por uma placa azul.')
            bt.enter()
            print ('\u001b[37;1mAssim você decicdi seguir o caminho para a: \n (1) direita \n (2) esquerda \n (3) voltar')
            dir = input('>>>') #escolha do jogador
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            # virar a direita
            if dir == '1': 
                sala = 114
            #virar a esquerda  
            elif dir == '2': 
                sala= 116
            #voltar
            elif dir == '3': 
                sala = 110
            #erro
            else:
                print ('\u001b[37;1mAssim você decicdi seguir o caminho para a: \n (1) direita \n (2) esquerda \n (3) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 116:
            print ('Enquanto caminhava pela floresta, você escuta o barulho de galhos quebrando a sua direita.')
            bt.enter()
            print('Pela altura do som  é possível prever que se tarta de um animal grande, talvez um urso.')
            bt.enter()
            print ('\u001b[37;1mCom isso você decidi: \n (1) seguir em frente \n (2) voltar')
            dir = input('>>>') #jogador escolhe 
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #frente
            if dir == '1': 
                sala = 117
            #voltar
            elif dir == '2': 
                sala = 115
            #erro
            else:
                print ('\u001b[37;1mCom isso você decidi: \n (1) seguir em frente \n (2) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

        
        elif sala == 117:
            #chance de evento aleatrio: frutinhas
            prob = chance(1,11) #probabilidade de ocorrer
            if prob <= 5:
                print('Cansado de andar você decidi senta em baixo da árvore pra retomar o fôlego.')
                bt.enter()
                print('Enquanto você descansava você repara em um pequeno arbusto com pequenas frutinhas avermelhadas.')
                bt.enter()
                print('\u001b[37;1mSentindo seu estomago roncar, depois de horas de camihada, você decide: \n (1) comer as frutinhas \n (2) não comer')
                escolha = input('>>>') #jogador escolhe se come ou não as frutinhas
                bt.delete_last_lines(1)
                print(f">>>{escolha}\u001b[0m\n")

                #comer as frutinhas
                if escolha == '1': 
                    prob2 = chance(1,21) 
                    #frutinhas são venenosas
                    if prob2 + jogador['sorte'] <= 10: 
                        print('Você colha algumas frutinhas e as coloca na boca. Ao colocar a primeira frutinha na boca, você sente o sabor doce.')
                        bt.enter()
                        print('Feliz pela refeição repentina, você começa a comer as deliciosas frutinhas. Já se sentindo satisfeito você se levanta, ao fazer isso você se sente zonzo, o que lhe obriga a se apoiar em uma árvore.')
                        bt.enter()
                        print('Imediatamente você liga ao seu mal estar repentino as pequenas frutinhas recem ingeridas. Arrependido você continua sua viajem.')
                        jogador['hp'] -=5 #jogador perde vida
                        bt.game_over(jogador) #confirmar que o jogador ainda possui hp
                    # são frutinhas normais
                    else: 
                        print('Você colha algumas frutinhas e as coloca na boca. Imediatamente você sente o sabor azedo lhe atingir.')
                        bt.enter()
                        print('Apesar disso a fome fala mais alto, então você continua se alimentando. Depois de comer um punhado, você decidi continuar a caminhada.')
                    #não comer as frutinhas
                elif escolha == '2': 
                    print('Apesar da fome, a desconfiança fala mais alto, então você decidi apenas ignorar a fome e descansar para continuar sua viagem.')
                    bt.enter()
                else:
                    print('\u001b[37;1mSentindo seu estomago roncar, depois de horas de camihada, você decide: \n (1) comer as frutinhas \n (2) não comer')
                    escolha = input('>>>')
                    bt.delete_last_lines(1)
                    print(f">>>{escolha}\u001b[0m\n")

            #encruzilhada
            print ('Andando pela trilha você se depara com uma placa roxa apontando para frente e uma placa verde apontando para a direita.')
            bt.enter()
            print ('\u001b[37;1mBaseando-se nisso você decidi seguir: \n (1) em frente \n (2) virar a direita \n (3) voltar')
            dir = input('>>>')
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #frente
            if dir == '1': 
                sala = 119
            #direita
            elif dir == '2': 
                sala= 118
            #voltar  
            elif dir == '3': 
                sala = 116
            #erro
            else:
                print ('\u001b[37;1mBaseando-se nisso você decidi seguir: \n (1) em frente \n (2) virar a direita \n (3) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

        
        elif sala == 118: #sem saida
            print ('Você continua pela trilha, até se deparar com o fim dela, mas não com o fim da floresta.')
            bt.enter()
            print ('\u001b[37;1mDessa forma você decidi: \n (1) voltar')
            dir = input('>>>') # escolha do jogador
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #voltar
            if dir == '1': 
                sala = 117
            #erro
            else:
                print ('\u001b[37;1mDessa forma você decidi: \n (1) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 119:
            print ('Mais uma vez você se vê diante de uma encruzilhada, com uma placa azul para a direita e uma placa vermelha para a esquerda.')
            bt.enter()
            print ('\u001b[37;1mAssim você decidi ir para: \n (1) direita \n (2) esquerda \n (3) voltar')
            dir = input('>>>')
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #direita
            if dir == '1':
                sala = saida
            #esquerda
            elif dir == '2': 
                sala= 120
            #volta
            elif dir == '3': 
                sala = 117
            #erro
            else:
                print ('\u001b[37;1mAssim você decidi ir para: \n (1) direita \n (2) esquerda \n (3) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

    
        elif sala == 120: #sem saida
            print('Ao longe é possível ver a luz do sol novamente, ansioso, você se apressa. Contudo, você repara que essa não era a saída e sim uma clareira com um lago de águas cristalinas.')
            bt.enter()
            print('\u001b[37;1mAo olhar ao redor você repara em algo que parece um acampamento improvisado. Você decidi:\n (1) olhar o acampamento\n (2) voltar')
            dir = input('>>>')
            bt.delete_last_lines(1)
            print(f">>>{dir}\u001b[0m\n")

            #olhar o acampamento
            if dir == '1':
                print('Ao se aproximar você vê os requicíos de um fogueira e uma cabana mal feita. Olhando dentro você repara que há alguns frascos vazios, exceto por um preeenchido por um líquido brilhante.\n\u001b[37;1m Assim você decidi:\n (1) beber o frasco\n (2) não beber')
                beber = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{beber}\u001b[0m\n")

                #jogador bebe a poção
                if beber == '1': 
                    print('Curioso para saber o que aconteceria você bebe a poção e imediatamente se sente bem.')
                    bt.passar_nivel(jogador)
                    print('Vendo que nã há mais nada de interessante, você decidi retornar pelo caminho que veio.')
                    sala = 119
                # jogador não bebe a poção
                if beber == '2':
                    print('O bom censo fala mais alto e você decidi que seria melho não arriscar. Então você decidi voltar pelo caminho que você veio.')
                    sala = 119
                # erro
                else:
                    print('Ao se aproximar você vê os requicíos de um fogueira e uma cabana mal feita. Olhando dentro você repara que há alguns frascos vazios, exceto por um preeenchido por um líquido brilhante.\n\u001b[37;1mAssim você decidi:\n (1) beber o frasco\n (2) não beber')
                    beber = input('>>>')   
                    bt.delete_last_lines(1)
                    print(f">>>{beber}\u001b[0m\n")
      
            # voltar
            if dir == '2':
                sala = 119
            #erro
            else:
                print ('\u001b[37;1mVocê decidi:\n (1) voltar')
                dir = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{dir}\u001b[0m\n")

  
    print('Depois de uma longa caminhada pela floresta finalmete é possível ver a luz do dia novamente e ao longe você avista o castelo.')
    bt.enter()
