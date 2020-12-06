from numpy import random as rd
import batalha as bt

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
      print('Assim você decidi ir para: \n1. direita  \n2. esquerda')
      dir = int(input('>>>')) #jogador escolhe caminho
      # virar direita
      if dir == 1: 
        sala = 104
      # virar esqueda
      elif dir == 2: 
        sala = 102
      #erro
      else:
        print ('Assim você decidi ir para: \n1. direita  \n2. esquerda') 
        dir = int(input('>>>'))
        
    elif sala == 102: 
      print ('Durante a caminhada você escuta o barulho de galhos se quebrando, mas devido a escuridão não é possível ver o responsável pelo som.')
      bt.enter()
      print ('Dessa forma você decidi: \n1. seguir em frente \n2. voltar para a encruzilhada')
      dir = int(input('>>>')) #jogador escolhe o caminho
      # seguir em frente
      if dir == 1: 
        sala =103 
      #voltar para sala anterior
      if dir == 2: 
        sala = 101
      #erro
      else: 
        print ('Dessa forma você decidi: \n1. seguir em frente \n2. voltar para a encruzilhada')
        dir = int(input('>>>'))
    
    elif sala == 103: #sala sem saida
      print ('Após horas caminhando você vê a trilha chegar ao fim, mas sem sinal da saída.') 
      bt.enter()
      print ('Frustado você decidi: \n1. voltar') 
      dir = int(input('>>>')) 
      # voltar para sala anterior
      if dir == 1: 
        sala = 102
      #erro
      else:
        print ('Frustado você decidi: \n1. voltar')
        dir = int(input('>>>'))
    
    elif sala == 104:
      print ('Continuando seu caminho pela trilha, você se depara com duas possibildades: continuar em frente, como indica a placa azul, ou virar a direita na placa laranja.')
      bt.enter()
      print ('Diante de tais possibilidades você escolhe: \n1. seguir em frente  \n2. virar a direita \n3. voltar')
      dir = int(input('>>>')) #jogador escolhe o caminho
      # seguir em frente
      if dir == 1: 
        sala = 107
      #virar a direita
      elif dir == 2: 
        sala= 105
      #voltar
      elif dir == 3: 
        sala = 101
      #erro
      else:
        print ('Diante de tais possibilidades você escolhe: \n1. seguir em frente  \n2. virar a direita \n3. voltar')
        dir = int(input('>>>'))
        
    elif sala == 105:
      #batalha com um urso
      if primeira_vez == True 
        print('Enquanto você caminhava, você se depara com um urso.')
        #inimigo
        Urso = {"nome": "Urso", 'hp': 70, 'defesa': 2, 'força': 3, 'destreza': 1, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
        #chama a função batalha do módulo batalha
        bt.batalha(Urso,jogador)
      #encrusilhada
      print ('Após o encontro com o urso você deicidi: \n1. seguir em frente \n2. voltar para encrusilhada')
      dir = int(input('>>>')) #jogador escolhe o caminho
      #seguir em frente
      if dir == 1: 
        sala = 106
        primeira_vez == False
      # voltar
      elif dir == 2: 
        sala= 104
        primeira_vez == False
      #erro
      else:
        print ('Após o encontro com o urso você deicidi: \n1. seguir em frente \n2. voltar para encrusilhada')
        dir = int(input('>>>'))
        
    elif sala == 106: #sala sem saida
      print ('Seguindo a trilha você se depara com uma caverna.')
      bt.enter()
      print('Com isso você decidi: \n1. entrar na caverna \n2. voltar')
      dir = int(input('>>>'))#jogador escolhe o caminho
      #entrar na caverna
      if dir == 1: 
        print('Ao entara na caverna, após se acostumar com o escuro, você repara nos restos de um amontoado de lenha.')
        bt.enter()
        print('Contudo, ao se aproximar, você consta que há muito tempo não ela é acesa.')
        bt.enter()
        print('Não vendo nada mais de interessante, você decidi voltar.')
        bt.enter
        sala == 105 #volta para a sala anterior
      #voltar  
      elif dir == 2:  
        sala = 105
      #erro
      else:
        print ('Com isso você decidi: \n1. entrar na caverna \n2. voltar')
        dir = int(input('>>>'))
    
    elif sala == 107:
      print ('Após um longo caminho, novamente você se depara com duas placas: uma para frente e outra para a direita.')
      bt.enter()
      print('A placa que aponta para a direita é de cor alaranjada, enquanto a para frente é arroxeada.')
      bt.enter()
      print ('E assim você segue seu caminho: \n1. pela direita \n2. em frente \n3. voltar')
      dir = int(input('>>>')) #jogador escolhe o caminho
      # ir pela direita
      if dir == 1: 
        sala = 108
      # seguir em frente  
      elif dir == 2:  
        sala= 110
      #voltar
      elif dir == 3: 
        sala = 104
      #erro
      else:
        print ('E assim você segue seu caminho: \n1. pela direita \n2. em frente \n3. voltar')
        dir = int(input('>>>'))
    
    elif sala == 108:
      print ('Enquanto caminhava pela floresta você repentinamente escuta um grunido a sua esquerda.')
      bt.enter()
      print ('Dessa forma você decid: \n1. seguir em frente \n2. voltar')
      dir = int(input('>>>')) #jogador escolhe o caminho
      #frente
      if dir == 1:  
        sala = 109
      #voltar  
      elif dir == 2: 
        sala= 107
      #erro
      else:
        print ('Dessa forma você decid: \n1. seguir em frente \n2. voltar')
        dir = int(input('>>>'))
   
    elif sala == 109: #sala sem saida
      print ('Depois de uma longa caminhada, você percebe que chegou ao fim da trilha, mas sem sinal da saida desse labirinto. ') 
      bt.enter()
      print ('Com isso você decidi: \n1. voltar') 
      dir = int(input('>>>')) #jogador escolhe o caminho
      #voltar
      if dir == 1: 
        sala = 108
      #erro
      else:
        print ('Com isso você decidi: \n1. voltar')
        dir = int(input('>>>'))
    
    elif sala == 110:
      #Chance de árvore caida no caminho
      prob = chance(1,15)
      if prob <= 6:
        print('Enquanto caminhava pela trilha, você se depara com um uma árvore caida bloquando seu caminho.')
        bt.enter()
        print('Vendo isso você decidi: \n1. empurrar a árvore caida \n2. pular por cima da árvore caida')
        escolha = int(input('>>>')) #jogador escolhe como passar pelo obstáculo
        #usar força para empurrar a árvore
        if escolha == 1:
          forca = chance(1,16) + jogador['força']
          #força suficiente para empurrar
          if forca >= 10:
            print('Você consegiui empurrar a árvore e contina seu caminho')
          #força insuficinete para empurrar
          else:
            print('Enquanto tentava empurrar a árvore caida, você acaba se machucando')
            jogador['hp'] -= 5 #jogador se machuca e perde vida
        #usar destreza para pular a árvore
        elif escolha == 2:
          des = chance(1,16) + jogador['destreza']
          #destreza suficiente para pular a árvore
          if des >= 10:
            print('Você consegiui pular a árvore e contina seu caminho')
          #destreza insuficiente para pular a árvore
          else:
            print('Após pular a árvore, ao aterrissar você acaba caindo e torcendo o tornozelo')
            jogador['hp'] -= 5
        #erro
        else:
          print('Vendo isso você decidi: \n1. empurrar a árvore caida /n2. pular por cima da árvore caida')
          escolha = int(input('>>>'))
      #encrusilhada
      print ('Andando mais um pouco você se depara com outra encruzilhada.')
      bt.enter()
      print('O caminho para direita é indicado por uma placa amarelo, enquanto o caminho para a esquerda é indicado por uma placa laranja')
      bt.enter()
      print('Assim você decidi ir pra: \n1. direita  \n2. esquerda \n3. voltar')
      dir = int(input('>>>')) #jogador escolhe o caminho
      # ir pela direita
      if dir == 1: 
        sala = 115
      #esquerda  
      elif dir == 2: 
        sala= 111
      #voltar  
      elif dir == 3: 
        sala = 107
      #erro
      else:
        print ('Assim você decidi ir pra: \n1. direita  \n2. esquerda \n3. voltar')
        dir = int(input('>>>'))
   
    elif sala == 111:
      print ('Seguindo em frente você se depara com uma nova bifurcação. Há uma placa roxa indicando o caminho a esquerda e uma placa vermelha apontando para o caminho a sua frente.')
      bt.enter()
      print ('Você decidi seguir a placa que aponta para: \n1. frente  \n2. esquerda \n3. voltar')
      dir = int(input('>>>')) #jogador escolhe o caminho a seguir
      # em frente
      if dir == 1: 
        sala = 112
      # virar esquerda
      elif dir == 2: 
        sala= 113
      #voltar  
      elif dir == 3: 
        sala = 110
      #erro
      else:
        print ('Você decidi seguir a placa que aponta para: \n1. frente  \n2. esquerda \n3. voltar')
        dir = int(input('>>>'))
    
    elif sala == 112: #sala sem saida
      print ('Continuando sua caminhada, você chega ao final da trilha, sem chegar do outro lado da floresta.')
      bt.enter()
      print ('Assim você decidi: \n1. voltar')
      dir = int(input('>>>')) #escolha do jogador
      #voltar
      if dir == 1: 
        sala = 111
      #erro
      else:
        print ('Assim você decidi: \n1. voltar')
        dir = int(input('>>>'))
    
    elif sala == 113: #sem saida
      #cabana com chance de arma
      print('Ao continuar dua caminhada você se depara com o final da trilha, mas sem sinal da saida.')
      bt.enter()
      print('Contudo você observa uma pequna cabana de madeira.')
      bt.enter()
      print('Você decidi: \n1. Entrar na cabana \n2. Voltar')
      dir = int(input('>>>')) #jogador escolhe entrar na cabana ou não
      #entrar na cabana
      if dir == 1:
        print('A medida que se aproxima da cabana, você percebe como ela está mal cuidada, provavelmente abandonada aalguns anos.')
        bt.enter()
        print('Você caminha em direção a cabana e abre a porta com cuidado, escutando o rangir da porta.')
        bt.enter()
        print('Ao entrar você percebe é capaz de enxergar uma mesa no centro do comodo, um suporte de madeira onde deveria ser a cama e um armário ao lado de uma janela.')
        voltar = 0 
        #explorando a cabana
        while escolha != 4:  
          print('Assim você decidi: \n1.Olhar a mesa \n2. Se aproximar da cama \n3. Ir até o armário \n4. Voltar')
          escolha = int(input('>>>')) #jogador escolhe para onde ir
          prob = chance(1,21) #chance de encontrar uma arma
          #mesa
          if escolha == 1: 
            if prob <=5:
              print('Ao se aproximar da mesa, você encontra uma adaga. Agora você possui uma nova arma.')
              bt.enter()
              jogador['arma'] = 'adaga'
            else:
              print('Você se aproxima da mesa vendo nada além de poeira em cima dela.')
              bt.enter()
          #cama
          elif escolha ==2: 
            if prob <=10 and prob >=6:
              print('Ao aproximar do suporte de madeira epercebe algo brilhando no chão.')
              bt.enter()
              print('Você se abaixa e pega, percebendo que se trata de uma adaga. Agora você possui uma nova arma.')
              bt.enter()
              jogador['arma'] = 'adaga'
            else:
              print('Você se aproxima do suporte de madeira e olha ao redor dele, mas não encontra nada.')
              bt.enter()
          #armário
          elif escolha== 3: 
            if prob <= 15 and prob >= 11:
              print('Você anda até o armário e o abre, e para sua surpresa você encontra uma única adaga. Agora você possui uma nova arma.')
              bt.enter()
            else:
              print('Você vai até o armário na esperança de encontrar algo, mas ao abri-lo você nã encontra nada.')
              bt.enter()
          # erro
          elif escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4: 
            print('Assim você decidi: \n1.Olhar a mesa \n2. Se aproximar da cama \n3. Ir até o armário \ni4. Voltar')
            escolha = int(input('>>>'))
        print('Depois de explorar a cabana, você decidi sair e voltar pelo caminho que veio.')
        bt.enter()
        sala = 111
      #voltar
      elif dir == 2:
        sala = 111  
      #erro
      else: 
        print('Você decidi: \n1. Entrar na cabana \n2. Voltar')
        dir = int(input('>>>'))
        
    elif sala == 114: #sem saida
      print ('Continuando pela trilha, você chega ao fim, mas sem conseguir chegar ao fim da floresta.')
      bt.enter()
      print ('Assim só lhe resta: \n1. voltar')
      dir = int(input('>>>')) #escolha do jogador
      #voltar
      if dir == 1: 
        sala = 115
      #erro
      else:
        print ('Assim só lhe resta: \n1. voltar')
        dir = int(input('>>>'))
    
    elif sala == 115:
      print('Andando pela trilha, mais uma vez você se depara com a possibilidade de escolher entre dois caminhos.')
      bt.enter()
      print('A primeira possibilidade é seguir a direita, indicada por uma placa verde. A outra possibilidade é seguir para a esquerda, indidcado por uma placa azul.')
      bt.enter()
      print ('Assim você decicdi seguir o caminho para a: \n1. direita \n2. esquerda \n3. voltar')
      dir = int(input('>>>')) #escolha do jogador
      # virar a direita
      if dir == 1: 
        sala = 114
      #virar a esquerda  
      elif dir == 2: 
        sala= 116
      #voltar
      elif dir == 3: 
        sala = 110
      #erro
      else:
        print ('Assim você decicdi seguir o caminho para a: \n1. direita \n2. esquerda \n3. voltar')
        dir = int(input('>>>'))
    
    elif sala == 116:
      print ('Enquanto caminhava pela floresta, você escuta o barulho de galhos quebrando a sua direita.')
      bt.enter()
      print('Pela altura do som  é possível prever que se tarta de um animal grande, talvez um urso.')
      bt.enter()
      print ('Com isso você decidi: \n1.seguir em frente \n2. voltar')
      dir = int(input('>>>')) #jogador escolhe 
      #frente
      if dir == 1: 
        sala = 117
      #voltar
      elif dir == 2: 
        sala= 115
      #erro
      else:
        print ('Com isso você decidi: \n1.seguir em frente \n2. voltar')
        dir = int(input('>>>'))
        
    elif sala == 117:
      #chance de evento aleatrio: frutinhas
      prob = chance(1,11) #probabilidade de ocorrer
      if prob <= 5:
        print('Cansado de andar você decidi senta em baixo da árvore pra retomar o fôlego.')
        bt.enter()
        print('Enquanto você descansava você repara em um pequeno arbusto com pequenas frutinhas avermelhadas.')
        bt.enter()
        print('Sentindo seu estomago roncar, depois de horas de camihada, você decide: \n1. comer as frutinhas \n2. não comer')
        escolha = int(input('>>>')) #jogador escolhe se come ou não as frutinhas
        #comer as frutinhas
        if escolha == 1: 
          prob2 = chance(1,21) 
          #frutinhas são venenosas
          if prob2 + jogador['sorte'] <= 10: 
            print('Você colha algumas frutinhas e as coloca na boca. Ao colocar a primeira frutinha na boca, você sente o sabor doce.')
            bt.enter()
            print('Feliz pela refeição repentina, você começa a comer as deliciosas frutinhas. Já se sentindo satisfeito você se levanta, ao fazer isso você se sente zonzo, o que lhe obriga a se apoiar em uma árvore.')
            bt.enter()
            print('Imediatamente você liga ao seu mal estar repentino as pequenas frutinhas recem ingeridas. Arrependido você continua sua viajem.')
            jogador['hp'] -=5 
          # são frutinhas normais
          else: 
            print('Você colha algumas frutinhas e as coloca na boca. Imediatamente você sente o sabor azedo lhe atingir.')
            bt.enter()
            print('Apesar disso a fome fala mais alto, então você continua se alimentando. Depois de comer um punhado, você decidi continuar a caminhada.')
        #não comer as frutinhas
        elif escolha == 2: 
          print('Apesar da fome, a desconfiança fala mais alto, então você decidi apenas ignorar a fome e descansar para continuar sua viagem.')
          bt.enter()
        else:
          print('Sentindo seu estomago roncar, depois de horas de camihada, você decide: \n1. comer as frutinhas \n2. não comer')
          escolha = int(input('>>>'))
      #encruzilhada
      print ('Andando pela trilha você se depara com uma placa roxa apontando para frente e uma placa verde apontando para a direita.')
      bt.enter()
      print ('Baseando-se nisso você decidi seguir: \n1. em frente \n2. virar a direita \n3. voltar')
      dir = int(input('>>>'))
      #frente
      if dir == 1: 
        sala = 119
      #direita
      elif dir == 2: 
        sala= 118
      #voltar  
      elif dir == 3: 
        sala = 116
      #erro
      else:
        print ('Baseando-se nisso você decidi seguir: \n1. em frente \n2. virar a direita \n3. voltar')
        dir = int(input('>>>'))
        
    elif sala == 118: #sem saida
      print ('Você continua pela trilha, até se deparar com o fim dela, mas não com o fim da floresta.')
      bt.enter()
      print ('Dessa forma você decidi: \n1. voltar')
      dir = int(input('>>>')) # escolha do jogador
      #voltar
      if dir == 1: 
        sala = 117
      #erro
      else:
        print ('Dessa forma você decidi: \n1. voltar')
        dir = int(input('>>>'))
    
    elif sala == 119:
      print ('Mais uma vez você se vê diante de uma encruzilhada, com uma placa azul para a direita e uma placa vermelha para a esquerda.')
      bt.enter()
      print ('Assim você decidi ir para: \n1. direita \n2. esquerda \n3. voltar')
      dir = int(input('>>>'))
      #direita
      if dir == 1:
        sala = saida
      #esquerda
      elif dir == 2: 
        sala= 120
      #volta
      elif dir == 3: 
        sala = 117
      #erro
      else:
        print ('Assim você decidi ir para: \n1. direita \n2. esquerda \n3. voltar')
        dir = int(input('>>>'))
    
    elif sala == 120: #sem saida
      print('Ao longe é possível ver a luz do sol novamente, ansioso, você se apressa.')
      bt.enter()
      print('Contudo, você repara que essa não era a saída e sim uma clareira com um lago de águas cristalinas.')
      bt.enter()
      print ('Você decidi:\n1. voltar')
      dir = int(input('>>>'))
      # voltar
      if dir ==1:
        sala = 119
      #erro
      else:
        print ('Você decidi:\n1. voltar')
        dir = int(input('>>>'))
  
  print('Depois de uma longa caminhada pela floresta finalmete é possível ver a luz do dia novamente.')
