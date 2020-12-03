from numpy import random as rd

def chance(x,y):
  return rd.randint(x,y)

sala = 101
saida = 0

'''
Para sair da floresta é preciso seguir as placas com as cores mais frias
Resposta: 1,1,2,1,2,1,1,1,
Inserir:  -batalha na sala 105
          - item na cabana, sala 113
          - tirar vida nas salas 110 e 117
'''
print('Seguindo a trilha você se depara com a floresta e suas imponentes árvores que escondem a fauna da luz do sol.')
print('Continuando sua caminhada você sente a umidade, acompanhada de um cheiro característico e do zumbido de insetos.')
while sala != saida:
  if sala == 101:
    print('Com poucos minutos de caminhada, já imcapacitado de ver o sol, você se depara com uma encruzilhada.')
    print('Indicando o caminho para direita há uma placa verde, equanto para a esquerda há uma placa amarela.')
    print('Assim você decidi ir para: \n1. direita  \n2. esquerda')
    dir = int(input('>>>'))
    if dir == 1: # virar direita
      sala = 104
    elif dir == 2: # virar esqueda
      sala = 102
    else:
      print ('Assim você decidi ir para: \n1. direita  \n2. esquerda') 
      dir = int(input('>>>'))
  elif sala == 102: 
    print ('Durante a caminhada você escuta o barulho de galhos se quebrando, mas devido a escuridão não é possível ver o responsável pelo som.')
    print ('Dessa forma você decidi: \n1. seguir em frente \n2. voltar para a encruzilhada')
    dir = int(input('>>>'))
    if dir == 1: # seguir em frente
      sala =103 
    if dir == 2: #voltar para sala anterior
      sala = 101
    else:
      print ('Dessa forma você decidi: \n1. seguir em frente \n2. voltar para a encruzilhada')
      dir = int(input('>>>'))
  elif sala == 103: #sala sem saida
    print ('Após horas caminhando você vê a trilha chegar ao fim, mas sem sinal da saída.') 
    print ('Frustado você decidi: \n1. voltar') 
    dir = int(input('>>>'))
    if dir == 1:
      sala = 102
    else:
      print ('Frustado você decidi: \n1. voltar')
      dir = int(input('>>>'))
  elif sala == 104:
    print ('Continuando seu caminho pela trilha, você se depara com duas possibildades: continuar em frente, como indica a placa azul, ou virar a direita na placa laranja.')
    print ('Diante de tais possibilidades você escolhe: \n1. seguir em frente  \n2. virar a direita \n3. voltar')
    dir = int(input('>>>'))
    if dir == 1: # seguir em frente
      sala = 107
    elif dir == 2: #virar a direita
      sala= 105
    elif dir == 3: #voltar
      sala = 101
    else:
      print ('Diante de tais possibilidades você escolhe: \n1. seguir em frente  \n2. virar a direita \n3. voltar')
      dir = int(input('>>>'))
  elif sala == 105:
   
    #inserir batalha contra um urso
    
    print ('Após o encontro com o urso você deicidi: \n1. seguir em frente \n2. voltar para encrusilhada')
    dir = int(input('>>>'))
    if dir == 1: #sseguir em frente
      sala = 106
    elif dir == 2: # voltar
      sala= 104
    else:
      print ('Após o encontro com o urso você deicidi: \n1. seguir em frente \n2. voltar para encrusilhada')
      dir = int(input('>>>'))
  elif sala == 106: #sala sem saida
    print ('Seguindo a trilha você se depara com uma caverna.')
    print('Com isso você decidi: \n1. entrar na caverna \n2. voltar')
    dir = int(input('>>>'))
    if dir == 1: #entrar na caverna
      print('Ao entara na caverna, após se acostumar com o escuro, você repara nos restos de um amontoado de lenha.')
      print('Contudo, ao se aproximar, você consta que há muito tempo não ela é acesa.')
      print('Não vendo nada mais de interessante, você decidi voltar.')
      sala == 105
    elif dir == 2: #voltar 
      sala = 105
    else:
      print ('Com isso você decidi: \n1. entrar na caverna \n2. voltar')
      dir = int(input('>>>'))
  elif sala == 107:
    print ('Após um longo caminho, novamente você se depara com duas placas: uma para frente e outra para a direita.')
    print('A placa que aponta para a direita é de cor alaranjada, enquanto a para frente é arroxeada.')
    print ('E assim você segue seu caminho: \n1. pela direita \n2. em frente \n3. voltar')
    dir = int(input('>>>'))
    if dir == 1: # direita
      sala = 108
    elif dir == 2: # seguir em frente 
      sala= 110
    elif dir == 3: #voltar
      sala = 104
    else:
      print ('E assim você segue seu caminho: \n1. pela direita \n2. em frente \n3. voltar')
      dir = int(input('>>>'))
  elif sala == 108:
    print ('Enquanto caminhava pela floresta você repentinamente escuta um grunido a sua esquerda.')
    print ('Dessa forma você decid: \n1. seguir em frente \n2. voltar')
    dir = int(input('>>>'))
    if dir == 1: #frente 
      sala = 109
    elif dir == 2: #voltar
      sala= 107
    else:
      print ('Dessa forma você decid: \n1. seguir em frente \n2. voltar')
      dir = int(input('>>>'))
  elif sala == 109: #sala sem saida
    print ('Depois de uma longa caminhada, você percebe que chegou ao fim da trilha, mas sem sinal da saida desse labirinto. ') 
    print ('Com isso você decidi: \n1. voltar') 
    dir = int(input('>>>'))
    if dir == 1: #voltar
        sala = 108
    else:
      print ('Com isso você decidi: \n1. voltar')
      dir = int(input('>>>'))
  elif sala == 110:
    #Chance de árvore caida no caminho
    prob = chance(1,15)
    if prob <= 6:
      print('Enquanto caminhava pela trilha, você se depara com um uma árvore caida bloquando seu caminho.')
      print('Vendo isso você decidi: \n1. empurrar a árvore caida \n2. pular por cima da árvore caida')
      escolha = int(input('>>>'))
      if escolha == 1:
        forca = chance(1,11) #+ forca
        if forca >= 6:
          print('Você consegiui empurrar a árvore e contina seu caminho')
        else:
          print('Enquanto tentava empurrar a árvore caida, você acaba se machucando')
          #tirar vida -1
      elif escolha == 2:
        des = chance(1,11) #+ destreza
        if des >= 6:
          print('Você consegiui pular a árvore e contina seu caminho')
        else:
          print('Após pular a árvore, ao aterrissar você acaba caindo e torcendo o tornozelo')
          #tirar vida -1
      else:
        print('Vendo isso você decidi: \n1. empurrar a árvore caida /n2. pular por cima da árvore caida')
        escolha = int(input('>>>'))
    
    print ('Andando mais um pouco você se depara com outra encruzilhada.')
    print('O caminho para direita é indicado por uma placa amarelo, enquanto o caminho para a esquerda é indicado por uma placa laranja')
    print('Assim você decidi ir pra: \n1. direita  \n2. esquerda \n3. voltar')
    dir = int(input('>>>'))
    if dir == 1: # direita
      sala = 115
    elif dir == 2: #esquerda
      sala= 111
    elif dir == 3: #voltar
      sala = 107
    else:
      print ('Assim você decidi ir pra: \n1. direita  \n2. esquerda \n3. voltar')
      dir = int(input('>>>'))
  elif sala == 111:
    print ('Seguindo em frente você se depara com uma nova bifurcação. Há uma placa roxa indicando o caminho a esquerda e uma placa vermelha apontando para o caminho a sua frente.')
    print ('Você decidi seguir a placa que aponta para: \n1. frente  \n2. esquerda \n3. voltar')
    dir = int(input('>>>'))
    if dir == 1: # em frente
      sala = 112
    elif dir == 2: # virar esquerda
      sala= 113
    elif dir == 3: #voltar
      sala = 110
    else:
      print ('Você decidi seguir a placa que aponta para: \n1. frente  \n2. esquerda \n3. voltar')
      dir = int(input('>>>'))
  elif sala == 112: #sala sem saida
    print ('Continuando sua caminhada, você chega ao final da trilha, sem chegar do outro lado da floresta.')
    print ('Assim você decidi: \n1. voltar')
    dir = int(input('>>>'))
    if dir == 1: #voltar
      sala = 111
    else:
      print ('Assim você decidi: \n1. voltar')
      dir = int(input('>>>'))
  elif sala == 113: #sem saida
    print('Ao continuar dua caminhada você se depara com o final da trilha, mas sem sinal da saida.')
    print('Contudo você observa uma pequna cabana de madeira.')
    print('Você decidi: \n1. Entrar na cabana \n2. Voltar')
    dir = int(input('>>>'))
    if dir == 1:
      print('A medida que se aproxima da cabana, você percebe como ela está mal cuidada, provavelmente abandonada aalguns anos.')
      print('Você caminha em direção a cabana e abre a porta com cuidado, escutando o rangir da porta.')
      print('Ao entrar você percebe é capaz de enxergar uma mesa no centro do comodo, um suporte de madeira onde deveria ser a cama e um armário ao lado de uma janela.')
      voltar = 0 
      while escolha != 4:  
        print('Assim você decidi: \n1.Olhar a mesa \n2. Se aproximar da cama \n3. Ir até o armário \n4. Voltar')
        escolha = int(input('>>>'))
        prob = chance(1,20)
        if escolha == 1: #mesa
          if prob <=5:
            print('recompensa')
          else:
            print('não encontrou nada')
        elif escolha ==2: #cama
          if prob <=10 and prob >=6:
            print('recompensa')
          else:
            print('não encontrou nada')
        elif escolha== 3: #armário
          if prob <= 15 and prob >= 11:
            print('recompensa')
          else:
            print('não encontrou nada')
        elif escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4: 
          print('Assim você decidi: \n1.Olhar a mesa \n2. Se aproximar da cama \n3. Ir até o armário \ni4. Voltar')
          escolha = int(input('>>>'))
      print('Você sai da cabana')
      print('Você decidi: \n1. Entrar na cabana \n2. Voltar')
      dir = int(input('>>>'))
      
    elif dir == 2:
      sala = 111  
    else: 
      print('Você decidi: \n1. Entrar na cabana \n2. Voltar')
      dir = int(input('>>>'))
  elif sala == 114: #sem saida
    print ('Continuando pela trilha, você chega ao fim, mas sem conseguir chegar ao fim da floresta.')
    print ('Assim só lhe resta: \n1. voltar')
    dir = int(input('>>>'))
    if dir == 1: #voltar
      sala = 115
    else:
      print ('Assim só lhe resta: \n1. voltar')
      dir = int(input('>>>'))
  elif sala == 115:
    print('Andando pela trilha, mais uma vez você se depara com a possibilidade de escolher entre dois caminhos.')
    print('A primeira possibilidade é seguir a direita, indicada por uma placa verde. A outra possibilidade é seguir para a esquerda, indidcado por uma placa azul.')
    print ('Assim você decicdi seguir o caminho para a: \n1. direita \n2. esquerda \n3. voltar')
    dir = int(input('>>>'))
    if dir == 1: # virar a direita
      sala = 114
    elif dir == 2: #virar a esquerda
      sala= 116
    elif dir == 3: #voltar
      sala = 110
    else:
      print ('Assim você decicdi seguir o caminho para a: \n1. direita \n2. esquerda \n3. voltar')
      dir = int(input('>>>'))
  elif sala == 116:
    print ('Enquanto caminhava pela floresta, você escuta o barulho de galhos quebrando a sua direita.')
    print('Pela altura do som  é possível prever que se tarta de um animal grande, talvez um urso.')
    print ('Com isso você decidi: \n1.seguir em frente \n2. voltar')
    dir = int(input('>>>'))
    if dir == 1: #frente
      sala = 117
    elif dir == 2: #voltar
      sala= 115
    else:
      print ('Com isso você decidi: \n1.seguir em frente \n2. voltar')
      dir = int(input('>>>'))
  elif sala == 117:
    #chance de evento aleatrio: frutinhas
    prob = chance(1,11)
    if prob <= 5:
      print('Cansado de andar você decidi senta em baixo da árvore pra retomar o fôlego.')
      print('Enquanto você descansava você repara em um pequeno arbusto com pequenas frutinhas avermelhadas.')
      print('Sentindo seu estomago roncar, depois de horas de camihada, você decide: \n1. comer as frutinhas \n2. não comer')
      escolha = int(input('>>>'))
      if escolha == 1: #comer as frutinhas
        prob2 = chance(1,11)
        if prob2 <=5: #frutinhas são venenosas
          print('Você colha algumas frutinhas e as coloca na boca. Ao colocar a primeira frutinha na boca, você sente o sabor doce.')
          print('Feliz pela refeição repentina, você começa a comer as deliciosas frutinhas. Já se sentindo satisfeito você se levanta, ao fazer isso você se sente zonzo, o que lhe obriga a se apoiar em uma árvore.')
          print('Imediatamente você liga ao seu mal estar repentino as pequenas frutinhas recem ingeridas. Arrependido você continua sua viajem.')
          #tirar vida 
        else: # são frutinhas normais
          print('Você colha algumas frutinhas e as coloca na boca. Imediatamente você sente o sabor azedo lhe atingir.')
          print('Apesar disso a fome fala mais alto, então você continua se alimentando. Depois de comer um punhado, você decidi continuar a caminhada.')
      elif escolha == 2: #não comer as frutinhas
        print('Apesar da fome, a desconfiança fala mais alto, então você decidi apenas ignorar a fome e descansar para continuar sua viagem.')
      else:
        print('Sentindo seu estomago roncar, depois de horas de camihada, você decide: \n1. comer as frutinhas \n2. não comer')
        escolha = int(input('>>>'))
    
    print ('Andando pela trilha você se depara com uma placa roxa apontando para frente e uma placa verde apontando para a direita.')
    print ('Baseando-se nisso você decidi seguir: \n1. em frente \n2. virar a direita \n3. voltar')
    dir = int(input('>>>'))
    if dir == 1: #frente
      sala = 119
    elif dir == 2: #direita
      sala= 118
    elif dir == 3: #voltar
      sala = 116
    else:
      print ('Baseando-se nisso você decidi seguir: \n1. em frente \n2. virar a direita \n3. voltar')
      dir = int(input('>>>'))
  elif sala == 118: #sem saida
    print ('Você continua pela trilha, até se deparar com o fim dela, mas não com o fim da floresta.')
    print ('Dessa forma você decidi: \n1. voltar')
    dir = int(input('>>>'))
    if dir == 1: #voltar
      sala = 117
    else:
      print ('Dessa forma você decidi: \n1. voltar')
      dir = int(input('>>>'))
  elif sala == 119:
    print ('Mais uma vez você se vê diante de uma encruzilhada, com uma placa azul para a direita e uma placa vermelha para a esquerda.')
    print ('Assim você decidi ir para: \n1. direita \n2. esquerda \n3. voltar')
    dir = int(input('>>>'))
    if dir == 1: #direita
      sala = saida
    elif dir == 2: #esquerda
      sala= 120
    elif dir == 3: #volta
      sala = 117
    else:
      print ('Assim você decidi ir para: \n1. direita \n2. esquerda \n3. voltar')
      dir = int(input('>>>'))
  elif sala == 120: #sem saida
    print('Ao longe é possível ver a luz do sol novamente, ansioso, você se apressa.')
    print('Contudo, você repara que essa não era a saída e sim uma clareira com um lago de águas cristalinas.')
    print ('Você decidi:\n1. voltar')
    dir = int(input('>>>'))
    if dir ==1:
      sala = 119
    else:
      print ('Você decidi:\n1. voltar')
      dir = int(input('>>>'))
print('Depois de uma longa caminhada pela floresta finalmete é possível ver a luz do dia novamente.')


