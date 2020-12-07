'''
Módulo com as funções que descrevem os acontecimentos da última parte do jogo
As funções salas definem o que o jogador pode encontrar em cada sala'''

import batalha as bt 
import sys
import os

def teste_atributo(atributo, min_atr = 5, max_atr = 10):
    '''Realiza um teste de atributo da seguinte forma:
       É gerado um valor entre min_atr e max_atr como valor a ser atingido.
       Outro valor aleatório entre 0 e 5 é somado ao valor do atributo do jogador
       Caso a soma seja maior ou igual ao valor a ser atingido, o jogador passa no teste e a função retorna True
       Caso seja menor, o jogador não passa e a função retorna False
       
       Argumentos obrigatórios: atributo (int)
       Argumentos opcionais: min_atr (int) e max_atr (int)
       Saída: True ou False'''
       
    valor = bt.dado(min_atr, max_atr)
    if atributo == 5: #Joga com vantagem
        dado = bt.dado(4, 5)
    else:
        dado = bt.dado(1, 5)
    if atributo + dado >= valor: #Passa no teste
        return True
    elif atributo + dado < valor: #Não passa no teste
        return False
    
def armadilha_armario(jogador):
    '''
    Descreve os acontecimentos da armadilha para a sala 4 - enigma de poções e gaveta
    Argumento: dicionário dos atributos do jogador
    '''
    
    n = 0 #Contador para que o jogador tenha apenas duas tentativas
    dano = 25
    print('No instante em que encosta na maçaneta, você sente algo espetar a palma de sua mão. A porta se abre e você observa o interior. '
          'Diversas prateleiras contendo frascos de poções. Cada poção possui a figura de um animal no rótulo e cada prateleira é composta de poções do mesmo animal. '
          'Além disso, há também uma grande gaveta trancada. Seu olhar recai sobre um bilhete caído aos seus pés e você se abaixa para lê-lo.')
    bt.enter()
    print('\nTEXTO DO BILHETE:\n"Ao maldito curioso, uma punição merecida\nUma dose de veneno e um mistério a resolver\n8 bebidas, 5 efeitos, 2 chances\n'
          'Em uma, a morte certa, em outra a cura garantida\nAo ladrão esperto, uma recompensa esperada"')
    bt.enter()
    print('\nVERSO DO BILHETE:\n"Aquele que o mata pode o salvar da vida como tal\nAquele que salta na floresta faz a queda se aparar\n'
          'Aquele que pelo chão segue o afunda na terra final\nAquele que pela água segue o leva a recuar\n'
          'Aquele que cisca o fará se sentir como um igual\nAqueles que sobram não vão além do natural"')
    bt.enter()
    print('Você percebe nesse momento uma mancha verde crescendo na palma de sua mão, partindo de onde sentiu espetar ao abrir o armário. '
          'Também presta atenção nos animais nos frascos e vê a seguinte ordem, de cima para baixo: SERPENTE, GALINHA, PEIXE, GATO, URSO, ÁGUIA, MACACO e CORVO')
    bt.enter()
    flag_enigma = False #Flag para resposta de qual poção beber
    flag_veneno = False #Flag para checar se escolheu a poção certa
    while flag_enigma == False or flag_veneno == False: #Garante que o input se repita caso o jogador digite uma opção inválida e tente mais uma vez
        print('Qual poção você irá beber?\n1 - SERPENTE\n2 - GALINHA\n3 - PEIXE\n4 - GATO\n5 - URSO\n6 - ÁGUIA\n7 - MACACO\n8 - CORVO')
        pocao = input('>>>')
        if pocao == '1': #Bebe a poção da Serpente - morte instantanea
            flag_enigma = True 
            print('Você bebe a poção e sente um gosto amargo dominar sua boca. Nos primeiros segundos nada acontece e a mancha para de crescer em sua mão. '
                  'Mas repentinamente suas pernas falham e você cai no chão. Sua energia se esvai e a última coisa que você escuta é uma risada aguda.')
            jogador['hp'] = 0
            bt.game_over(jogador)
        elif pocao == '2': #Bebe a poção da Galinha - vira uma galinha
            flag_enigma = True
            print('Em um único gole você bebe todo o conteúdo do frasco. Uma sensação parecida com cócegas percorre seu corpo e você tem a sensação de que seu interior está queimando e a sala está crescendo. '
                  'Ao tentar falar, apenas cacareja. Você vê seu reflexo em um pequeno espelho na parte interna da porta do armário. Você virou uma galinha!')
            bt.enter()
            print('\nDesesperado, sai pulando pela sala, pensando em como enfrentaria o VILÃO nessa forma. Alguns minutos se passam e a sensação de que seu corpo está queimando retorna. '
                  'Você fecha os olhos quando todos seus ossos doem e, quando abre novamente, voltou ao normal e a mancha verde agora tem o dobro do tamanho')
            bt.enter()
            dano += 5 #Aumenta o dano em 5 pontos
            n += 1 
        elif pocao == '3' or pocao == '7': #Bebe a poção do Peixe ou do Macaco - diminui metade do dano
            flag_enigma = True
            dano //= 2
            n += 1
            print('A poção que você bebe possui um estranho gosto salgado. Aparentemente nada acontece, mas ao observar mais atentamente nota que o tom de verde da crescente mancha na sua mão está mais claro.')
            bt.enter()
        elif pocao == '4' or pocao == '6' or pocao == '8': #Bebe a poção do Gato, da Águia ou do Corvo - nada acontece
            flag_enigma = True
            print('Você cheira a poção antes de beber, mas ela é inodora. Tampouco tem algum sabor. Você logo percebe que é apenas água!')
            bt.enter()
            n += 1
        elif pocao == '5': #Bebe a poção do Urso - antídoto do veneno
            flag_enigma = True
            flag_veneno = True
            print('Você não consegue evitar fazer uma careta ao sentir um péssimo gosto azedo ao beber do frasco. O enjôo é forte e você quase vomita. Olha para sua mão com expectativa e vê a mancha começar a diminuir até sumir.')
            bt.enter()
            print('Uma olhada mais atenta ao frasco revela uma pequena chave no seu interior. Você o joga no chão e ele se quebra em vários cacos, liberando a chave, que se encaixa perfeitamente na fechadura da gaveta.\n')
            flag_gaveta = False #Flag para a resposta de abrir ou não a gaveta
            while flag_gaveta == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('Deseja abrir a gaveta:\n1 - sim\n2 - não')
                gaveta = input('>>>')
                if gaveta == '1': #Abre a gaveta
                    flag_gaveta = True
                    print('Você gira a chave e a gaveta se abre. 2 itens no interior chamam a sua atenção:\n'
                          '1 - Um frasco com uma poção verde\n3 - Um frasco com uma poção vermelha')
                    #Teste de inteligência para saber se o jogador reconhece as poções
                    pocoes = teste_atributo(jogador['inteligência'])
                    if pocoes == True: #Passa no teste
                        print('Ao analisar os frascos, você chega a conclusão de que a poção vermelha é diferente da poção de cura que conhece e a verde é uma poção de fortalecimento.')
                    bt.enter()
                    flag_pocao = False #Flag para a resposta de beber ou não a poção
                    while flag_pocao == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                        print('Deseja tomar as poções?\n1 - Sim, as duas\n2 - Apenas a vermelha\n3 - Apenas a verde\n4 - Não')
                        pocao = input('>>>')
                        if pocao == '1': #Bebe as duas poções
                            flag_pocao = True
                            print('\nVocê bebe primeiro a poção verde. Ela não possui sabor algum, mas você se sente mais forte de alguma forma.')
                            jogador['força'] += 1
                            print(f'\nSua força: {jogador["força"]}')
                            bt.enter()
                            print('Confiante, você bebe a poção vermelha em seguida. Ela possui um suave sabor doce e você logo esvazia o frasco. Contudo sua cabeça começa a latejar e você precisa se apoiar na parede para não cair.')
                            bt.enter()
                            jogador['hp'] -= 9
                            print(f'Você levou 9 pontos de dano. Seu hp: {jogador["hp"]}')
                            bt.game_over(jogador) #Checa se deu game over
                        elif pocao == '2': #Bebe apenas a poção vermelha
                            flag_pocao = True
                            print('Confiante, você bebe a poção vermelha. Ela possui um suave sabor doce e você logo esvazia o frasco. Contudo sua cabeça começa a latejar e você precisa se apoiar na parede para não cair.')
                            bt.enter()
                            jogador['hp'] -= 9
                            print(f'Você levou 9 pontos de dano. Seu hp: {jogador["hp"]}')
                            bt.game_over(jogador) #Checa se deu game over
                            bt.enter()
                        elif pocao == '3': #Bebe apenas a poção verde
                            flag_pocao = True
                            print('\nVocê bebe a poção verde. Ela não possui sabor algum, mas você se sente mais forte de alguma forma.')
                            jogador['força'] += 1
                            print(f'\nSua força: {jogador["força"]}')
                            bt.enter()
                        elif pocao == '4': #Não bebe nenhuma poção
                            flag_pocao = True
                            print('Você não pode assumir riscos desnecessário, então simplesmente fecha a gaveta.')
                        if flag_pocao == False: #Checa se o jogador digitou um comando inválido
                            print('Comando não reconhecido, tente novamente.')
                elif gaveta == '2': #Não abre a gaveta
                    flag_gaveta = True
                    print('É melhor não perder tempo ou se arriscar, pode ser apenas mais uma armadilha.')
        if flag_enigma == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
        if n == 2: #Checa se o jogador já fez duas tentativas
            flag_enigma = True
            flag_veneno = True
            print('Você se lembra da frase do bilhete que diz que você tem apenas duas chances. A mancha já cobre toda sua mão. Subtamente, você sente como se algo tivesse atingido seu coração com força e a mancha desaparece.')
            bt.enter()
            jogador['hp'] -= dano
            print(f'Você levou {dano} pontos de dano. Seu hp: {jogador["hp"]}')
            bt.game_over(jogador) #Checa se deu game over


def sala1(jogador):
    '''
    Descreve os acontecimentos da sala 1 - 2 batalhas e uma escolha de qual caminho seguir
    Argumento: dicionário dos atributos do jogador
    Saída: sala_atual
    '''
    
    global sala_atual
    print('Ao entrar, você chega em uma grande sala. Apenas dois sofás velhos ao redor de uma mesa de centro, juntamente com uma lareira apagada na parede da direita e a falta de decoração fazem o ambiente parecer frio e vazio. '
          'O lugar estava vazio até um pequeno Goblin entrar. Ele não perde tempo e logo te ataca!')
    bt.enter()
    #Dicionário do Goblin
    Goblin1 = {"nome" : "Goblin",    'hp': 55,  'defesa': 3, 'força': 1, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.batalha(Goblin1, jogador, True)
    bt.enter()
    print('Os sons da batalha atraem um Segurança para a sala!')
    bt.enter()
    #Dicionário do Segurança 
    Segurança = {"nome" : "Segurança",    'hp': 60,  'defesa': 3, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.batalha(Segurança, jogador, True)
    bt.enter()
    #Nesse momento, o jogador tem dois caminhos a seguir, um mais longo e um mais curto
    print('Há duas portas de madeira lisa na sala: uma na parede em frente a você e outra à esquerda.')
    flag_porta = False #Flag para resposta de qual caminho seguir
    while flag_porta == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('Qual você escolhe?\n1 - frente\n2 - esquerda')
        prox = input('>>>')
        if prox == '1': #Segue pela porta da frente
            sala_atual = 7 #Manda o jogador para a sala 7
            flag_porta = True
        elif prox == '2': #Segue pela porta da esquerda
            sala_atual = 5 #Manda o jogador para a sala 5
            flag_porta = True
        if flag_porta == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
    return sala_atual

def sala2(jogador):
    '''
    Descreve os acontecimentos da sala 2 - busca nas caixas (comida, poções, batalha e encontrar espada), 
    batalha no corredor e escolha de caminho
    Argumento: dicionário dos atributos do jogador
    Saída: sala_atual
    '''
    global sala_atual
    print('A porta abre direto para um pequeno depósito. No instante que você entra, a porta se fecha e tranca sozinha.')
    print('Todas as paredes são cobertas por estantes de metal simples, todas cheias de caixas de diferentes tamanhos e formatos.')
    bt.enter()
    flag_caixa = False #Flag para resposta de olhar ou não as caixas
    while flag_caixa == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('Deseja olhar dentro das caixas?\n1 - sim\n2 - não')
        caixa = input('>>>')
        if caixa == '1': #Olha as caixas
            flag_caixa = True
            print('\nConforme você mexe nas caixas, percebe que a maioria contém apenas roupas e comidas de aparência suspeita.')
            bt.enter()
            flag_comida = False #Flag para resposta de comer ou não
            while flag_comida == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('Deseja comer algo?\n1 - sim\n2 - não')
                comida = input('>>>')
                if comida == '1': #Come
                    flag_comida = True
                    #Teste de sorte para ver se a comida está estragada ou não
                    estraga = teste_atributo(jogador['sorte'], 6, 8)
                    if estraga == True: #Passa no teste - não está estragada
                        print('\nA fome fala mais alto e você pega um pão escuro. Estava um pouco salgado e com gosto de queimado, mas até que estava bom. '
                              'A fome passa e você sente suas energias renovadas!')
                        bt.enter()
                        jogador['hp'] += 5
                    elif estraga == False: #Não passa no teste - está estragada
                        print('\nA fome fala mais alto e você pega um pão com um cheiro doce. Nas primeiras mordidas não sente nada, mas depois de comer metade um enjôo o faz vomitar.')
                        bt.enter()
                        jogador['hp'] -= 5
                    print(f'Seu hp: {jogador["hp"]}')
                    bt.game_over(jogador) #Checa se deu game over
                elif comida == '2': #Não come
                    flag_comida = True
                    print('\nApesar da fome, melhor não arriscar comer algo estragado.')
                    bt.enter()
                if flag_comida == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.')
                    
            print('\nVocê ouve um barulho estranho vindo de uma caixa, mas continua mexendo e um escorpião do tamanho de um filhote de cachorro pula da caixa.')
            bt.enter()
            #Dicionário dos atributos do escorpião (ajustar atributos)
            escorpiao = {"nome" : 'Escorpião Anormalmente Grande',    'hp': 50,  'defesa': 1, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
            bt.batalha(escorpiao, jogador, True)
            bt.enter()
            print('Após derrotar o escorpião, você olha a caixa em que ele estava e encontra uma espada em seu interior!')
            flag_espada = False #Flag para resposta de pegar ou não a espada
            while flag_espada == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('Deseja pegar a espada?\n1 - sim\n2 - não')
                pegar = input('>>>')
                if pegar == '1': #Pega a espada
                    flag_espada = True
                    print('Você pegou a arma!')
                    #Dicionário com os atributos da espada
                    espada = {"nome": "espada", "atributo": "DES", "dano": "1-3", "min": 2, "max": 4}
                    jogador['arma'] = espada #definir atributos da espada
                elif pegar == '2': #Não pega a espada
                    flag_espada = True
                    print('Você deixa a espada onde ela está.')
                if flag_espada == False: #Checa se o jogador digitou um comando inválido
                    print('Comando não reconhecido, tente novamente.')
            bt.enter()
            print('Em outra caixa, você encontra diferentes garrafas. Enquanto abre uma por uma, vê que a maioria é água ou café velho, exceto por três delas. '
                  'Uma possui um líquido roxo, outra um líquido azul e a última um líquido laranja.')
            teste_pa = teste_atributo(jogador['inteligência'], 8, 9) #Teste se o jogador reconhece a poção azul
            if teste_pa == True: #Passa no teste
                print('\nVocê conhece o líquido azul, é uma poção de força.')
            teste_pl = teste_atributo(jogador['inteligência']) #Teste se o jogador reconhece a poção laranja
            if teste_pl == True:
                print('\nO cheiro do líquido laranja lhe é familiar e você percebe se tratar de uma simples poção de cura.')
            teste_pr = teste_atributo(jogador['inteligência'], 6, 7) #Teste se o jogador reconhece a poção roxa 
            if teste_pr == True:
                print('\nVocê se lembra já ter visto esse veneno roxo antes e sabe que não deve bebê-lo.')
            flag_pa = False #Flag para resposta de beber ou não a poção azul
            while flag_pa == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('Deseja beber a poção azul?\n1 - sim\n2 - não')
                pocao_azul = input('>>>')
                if pocao_azul == '1': #Bebe a poção
                    flag_pa = True
                    print('Você bebe a poção, que não possui sabor algum, mas sente que, de alguma forma, está mais forte.\n')
                    jogador['força'] += 1
                    print(f'Sua força: {jogador["força"]}')
                elif pocao_azul == '2': #Não bebe a poção
                    flag_pa = True
                    print('Não é hora de correr riscos, deixa essa garrafa onde está.')
                if flag_pa == False: #Checa se o jogador digitou um comando inválido
                    print('Comando não reconhecido, tente novamente.')
            flag_pl = False #Flag para resposta de beber ou não a poção laranja
            while flag_pl == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('Deseja beber a poção laranja?\n1 - sim\n2 - não')
                pocao_laranja = input('>>>')
                if pocao_laranja == '1': #Bebe a poção
                    flag_pl = True
                    print('A doce poção com sabor de suco de laranja te passa a sensação de estar revigorado.')
                    jogador['hp'] += 25
                elif pocao_laranja == '2': #Não bebe a poção
                    flag_pl = True
                    print('Apesar do cheiro doce e saboroso, as aparências podem enganar e não tem motivo para arriscar. Você fecha a garrafa e a devolve no local que pegou.')
                if flag_pl == False: #Checa se o jogador digitou um comando inválido
                    print('Comando não reconhecido, tente novamente.')
            flag_pr = False #Flag para resposta de beber ou não a poção roxa
            while flag_pr == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('Deseja beber a poção roxa?\n1 - sim\n2 - não')
                pocao_roxa = input('>>>')
                if pocao_roxa == '1': #Bebe a poção
                    flag_pr = True
                    print('A bebida tem uma consistência estranha e você se arrepende de beber. Uma fumaça roxa sai de sua boca e você se sente repentinamente mais cansado.')
                    jogador['hp'] -= 15
                    print(f'Seu hp: {jogador["hp"]}')
                elif pocao_roxa == '2': #Não bebe a poção
                    print('A poção não é confiável e você tem coisa melhor para fazer do que ficar bebendo de garrafas estranhas.')
                    flag_pr = True
                if flag_pr == False: #Checa se o jogador digitou um comando inválido
                    print('Comando não reconhecido, tente novamente.')
        elif caixa == '2': #Não olha as caixas
            flag_caixa = True
            print('\nVocê não tem tempo para ficar mexendo em nada, está com pressa para encontrar TAL COISA.')
        if flag_caixa == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
    bt.enter()
    print('Uma saída sem porta leva a um caminho que vira à esquerda em um longo corredor com apenas uma tocha no meio do caminho para iluminar tudo. '
            'Você segue em frente e a única opção ao final é virar à esquerda outra vez.')
    bt.enter()
    print('Um estranho morto vivo estava parado e te ataca!')
    bt.enter()
    #Dicionário com os atributos do Morto Vivo:
    Morto_vivo = {"nome" : "Morto Vivo",    'hp': 45,  'defesa': 2, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.batalha(Morto_vivo, jogador, True)
    bt.enter()
    print('Ao seguir pelo corredor, você vê que na parede esquerda existem duas ramificações.')
    flag_ramif = False #Flag para resposta de qual ramificação seguir
    while flag == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('Deseja seguir pela primeira ou pela segunda?\n1 - primeira\n2 - segunda')
        prox = input('>>>')
        if prox == '1': #Segue pela primeira ramificação
            print('\nVocê vira na primeira ramificação e a péssima iluminação mostra apenas a porta aberta de uma sala escura ao final do corredor.')
            sala_atual = 3 #Manda o jogador para a sala 3
            flag = True
        elif prox == '2': #Segue pela segunda ramificação
            print('\nVocê vira na segunda ramificação e segue por outro corredor escuro até encontrar uma porta fechada. Você tenta abrir e, para sua sorte, estava destrancada.')
            sala_atual = 6 #Manda o jogador para a sala 6
            flag = True
        if flag == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.')
    return sala_atual

def sala3(jogador):
    '''
    Descreve os acontecimentos da sala 3 - batalha, baú com poções, cochilo
    Argumento: dicionário com os atributos do jogador
    Saída: sala_atual
    '''
    global sala_atual
    print('Quando você entra na sala, a luz se acende e a porta se fecha atrás de você. Apenas para ter certeza, você tenta abrí-la, mas já está trancada.')
    print('Três beliches e um armário vazio são, aparentemente, a única mobilia do local. Um Goblin dorme em uma das camas, mas quando a luz acende ele levanta e não perde tempo antes de te atacar.')
    #dicionário com os atributos do Goblin
    Goblin = {"nome" : "Goblin",    'hp': 55,  'defesa': 3, 'força': 1, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.enter()
    bt.batalha(Goblin, jogador, True)
    bt.enter()
    print('Você vê, no canto esquerdo da sala, um pequeno baú dourado com a tampa aberta.')
    flag_bau = False #Flag para resposta de ver ou não o baú
    while flag_bau == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('Deseja ver seu conteúdo?\n1 - sim\n2 - não')
        bau = input('>>>') 
        if bau == '1': #Vê o baú
            flag_bau = True
            print('\nNo interior do baú há dois frascos: um deles possui um líquido viscoso e esbranquiçado e o outro um líquido vermelho.')
            #Testes de inteligencia do jogador para saber se ele reconhece ou não as poções
            teste_pb = teste_atributo(jogador['inteligência'], 7, 10) #Teste para a poção branca
            teste_pv = teste_atributo(jogador['inteligência'], 5, 7) #Teste para a poção vermelha
            if teste_pb == True and teste_pv == True: #Reconhece as duas
                print('Você reconhece as poções de um livro, sendo a vermelha uma de cura e a esbranquiçada de experiência')
            elif teste_pb == False and teste_pv == True: #Reconhece apenas a vermelha
                print('Você não sabe o que é a poção branca, mas sabe que a vermelha aumentará sua vida.')
            elif teste_pv == False: #Não reconhece nenhuma
                print('Você não sabe o efeito de nenhuma das poções.')
            flag_pb = False #Flag para respota de beber ou não a poção branca
            while flag_pb == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('Deseja tomar a poção esbranquiçada?\n1 - sim\n2 - não')
                poção_branca = input('>>>')
                if poção_branca == '1': #Bebe
                    flag_pb = True
                    bt.passar_nivel(jogador)
                elif poção_branca == '2': #Não bebe
                    flag_pb = True
                    print('Desconfiado, você decide ignorar o frasco com o líquido branco.')
                if flag_pb == False: #Checa se o jogador digitou um comando inválido
                    print('Comando não reconhecido, tente novamente.')
            flag_pv = False #Flag para resposta de beber ou não a poção vermelha
            while flag_pv == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                bt.enter()
                poção_vermelha = input('Deseja tomar a poção vermelha?\n1 - sim\n2 - não')
                if poção_vermelha == '1': #Bebe a poção
                    flag_pv = True
                    jogador['hp'] += 25 #Aumenta a vida do jogador
                    print('Você ganhou 25 pontos de vida!')
                    print(f'Seu hp: {jogador["hp"]}')
                    bt.enter()
                elif poção_vermelha == '2': #Não bebe a poção
                    flag_pv = True
                    print('Você prefere não arriscar e não bebe a poção vermelha.')
                if flag_pv == False: #Checa se o jogador digitou um comando inválido
                    print('Comando não reconhecido, tente novamente.')
        elif bau == '2': #Não abre o baú
            flag_bau = True
            print('Você ignora o baú e nada acontece.')
        if flag_bau == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
    print('Você olha para as camas e se pergunta se um rápido cochilo pode ser bom para recuperar as energias ou se é melhor não perder tempo.')
    flag_cochilo = False  #Flag para resposta de cochilar ou não
    while flag_cochilo == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('O que você escolhe?\n1 - Cochilar\n2 - Não perder tempo')
        cochilo = input('>>>')
        if cochilo == '1': #Dorme
            flag_cochilo = True
            print('Você deita em uma das camas e aproveita para descansar, em estado semi-alerta. Alguns minutos se passam e você se sente descansado e recuperado.')
            jogador['hp'] += 20
            print(f'Você recuperou 20 ponts de hp. Sua vida: {jogador["hp"]}')
        elif cochilo == '2': #Não dorme
            flag_cochilo = True
            print('É arriscado demais baixar a guarda desse jeito, melhor não.')
        if flag_cochilo == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
    bt.enter()
    print('Além da porta pela qual você entrou, existem outras duas, mas apenas uma na parede oeste está destrancada e você segue por ela.')
    sala_atual = 6 #Manda o jogador para a sala 6
    return sala_atual

def sala4(jogador):
    '''
    Descreve os acontecimentos da sala 4 - armadilha do armário
    Entrada: dicionário com os atributos do jogador
    Saída: sala_atual
    '''
    global sala_atual
    print('Uma vela em cima de uma mesa no centro do cômodo fornece uma fraca iluminação. Estantes com pedaços de armadura e armamentos quebrados ou não terminados indicam que o local devia ser utilizado como arsenal anteriormente.')
    print('Há também um armário de aço com uma única porta cuja maçaneta parece ser de ouro maciço com um pequeno diamante no centro.')
    #Teste de inteligencia para saber se o jogador identifica algo estranho
    armadilha = teste_atributo(jogador['inteligência'])
    if armadilha == True: #Identifica algo estranho
        print('Você percebe que a maçaneta possui uma mancha incomum para uma peça de ouro e que o diamante é falso, além de ter algo pequeno e fino na superfície apontando para fora.')
    flag_armario = False #Flag para a resposta de abrir o armário
    while flag_armario == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('Você tenta abrí-lo?\n1 - sim\n2 - não')
        armario = input('>>>')
        if armario == '1': #Abre o armário
            flag_armario = True
            armadilha_armario(jogador)
        elif armario == '2': #Não abre o armário
            flag_armario = True
            print('O que pode ser mais importante que recuperar TAL COISA? Seja lá o que tem nesse armário, a recompensa do rei deve ser melhor.')
        if flag_armario == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
    bt.enter()
    print('No meio da parede à esquerda, uma porta com um enorme X vermelho pintado fecha a única saída existente já que, como tem acontecido, a porta pela qual você entrou se trancou sozinha. '
          'Você sai por ela e, após alguns passos, se depara com uma porta aberta de uma sala escura.')
    bt.enter()
    sala_atual = 3 #Manda o jogador pra sala 3
    return sala_atual

def sala5(jogador):
    '''
    Descreve os acontecimentos da sala 5 - batalha
    Argumento: dicionário com os atributos do jogador
    Saída: sala_atual
    '''
    global sala_atual
    print('Você decide seguir pela porta da esquerda, pensando que poderia tentar o outro caminho caso necessário, porém a porta se tranca sozinha assim que você passa por ela. Sem outra opção, você olha a sala em que entrou. '
          'Não há nenhum móvel no local, apenas o que parece ser uma grande escultura. Mas quando você se aproxima ela se levanta e se vira para você, que percebe que na verdade a estátua era um Troll adormecido!')
    #Dicionário com os atributos do troll
    troll = {"nome" : 'Troll',    'hp': 60,  'defesa': 1, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.enter()
    bt.batalha(troll, jogador, True)
    bt.enter()
    print('Assim que o INIMIGO morre, um leve tremor percorre a sala. O contorno de uma porta que não existia antes surge na parede a sua frente. Ela se abre e você continua sua busca por TAL COISA. '
          'O corredor mal iluminado vira à esquerda e depois à direita antes de chegar a uma porta feita de grossas barras de ferro cruzadas formando uma grade, como a prisão de algo ou alguém.')
    bt.enter()
    sala_atual = 8 #Manda o jogador para a sala 8
    return sala_atual

def sala6(jogador):
    global sala_atual
    print('DESCRIÇÃO SALA6')
    print('Então, você finalmente o vê. Sentado em uma cadeira, te encarando como se te esperasse.')
    #Discurso do boss1
    bt.enter()
    #Primeira parte do boss
    boss1 = {"nome" : 'Boss1',    'hp': 85,  'defesa': 3, 'força': 1, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.batalha(boss1, jogador, True)
    sala_atual = 0 #Encerra a parte das salas para seguir para o final
    print('Após derrotar BOSS1, você faz uma busca pela sala, mas não encontra nada. Todas as portas estão trancadas e, aparentemente, não há uma saída. '
          'Começando a acreditar que está no lugar errado, você se senta na cadeira em que BOSS1 estava e vê um discreto botão camuflado na lateral do tampo da mesa. '
          'Você o aperta, o teto começa a se mexer e uma nuvem de poeira cai por todo o local. Quando finalmente a poeira abaixa, você vê uma escada circular no canto da sala e resolve subir.')
    return sala_atual

def sala7(jogador):
    global sala_atual
    print('\nApós dar dois passos para a frente e virar à direita, você segue por um corredor não muito longo e pouco iluminado até chegar em outra porta. Você entra e escuta um barulho de tranca. '
          'Surpreso, tenta abrir a porta, mas ela está trancada.')
    bt.enter()
    print('Uma análise rápida e você percebe se tratar de uma cozinha. Um fogão simples e sem lenha num canto, uma pia sem torneira e uma geladeira sem porta fazem o local parecer abandonado há anos. '
          'Uma pilha de ossos no canto começa a se mexer, formando um esqueleto vivo que te ataca!')
    bt.enter()
    #Dicionário com os atributos do Esqueleto parte 1
    Esqueleto = {"nome" : "Esqueleto", 'hp': 55,  'defesa': 3, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.batalha(Esqueleto, jogador, True)
    bt.enter()
    #Dicionário com os atributos do Esqueleto remontado
    Esqueleto2 = {"nome" : "Esqueleto", 'hp': 45,  'defesa': 2, 'força': 3, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    print('Você pensa ter derrotado o esqueleto, mas assim que se vira, escuta barulhos de ossos batendo e gira outra vez a tempo de ver o esqueleto se montando e ficando em pé outra vez.')
    bt.enter()
    bt.batalha(Esqueleto2, jogador, True)
    bt.enter()
    print('Dessa vez, ao derrortá-lo você separa os ossos, prendendo um pouco dentro do forno, um tanto na geladeira e um tanto na pia, utilizando alguns pedaços de corda que encontrou para amarrá-lo.')
    bt.enter()
    print('Nesse momento, há apenas um caminho para seguir, uma porta branca à direita.')
    sala_atual = 2
    return sala_atual

def sala8(jogador):
    global sala_atual
    print('A única tocha no alto da parede é suficiente para você ver entender que entrou na jaula de um grande Javali. O animal tem certa de 2 metros de comprimento, o pelo cinza está sujo e ele parece faminto, já que a única coisa além dele é um balde com água. '
          'Como esperado, ele olha para você, pronto para devorar o novo jantar.')
    bt.enter()
    #Dicionário do Javali
    Javali = {"nome" : "Javali", 'hp': 65,  'defesa': 5, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.batalha(Javali, jogador, True)
    bt.enter()
    print('O Javali desaparece quase por inteiro na frente dos seus olhos, restando apenas sua pele. Você a observa e vê que está limpa por dentro e é mais leve do que parece.')
    flag = False
    while flag == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('Deseja vestir a pele do javali?\n1 - sim\n2 - não')
        pele = input('>>>')
        if pele == '1':
            flag = True
            print('Você veste a pele e ela adere à sua roupa magicamente, como uma armadura, e sua defesa aumenta!')
            jogador['defesa'] += 1
            print(f'Sua defesa atual: {jogador["defesa"]}')
        elif pele == '2':
            flag = True
            print('Uma pele como essa só iria atrapalhar, melhor deixar onde está.')
        if flag == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
   
    bt.enter()
    print('Aparentemente a grade é a única saída, porém está trancada. Lembrando da porta que apareceu sozinha na sala anterior, você decide explorar as paredes em busca de algo semelhante. '
          'Ao encostar na parede da direita, subtamente ela desaparece por completo. Antes que ela volte, você entra no espaço escuro atrás dela. Um barulho indica que a parede voltou ao seu lugar. '
          'No segundo seguinte, uma série de tochas se acende, iluminando um corredor que segue em frente por alguns passos antes de virar à direita.')
    bt.enter()
    print('As paredes do corredor estão repletas de pinturas e inscrições que não possuem nenhum significado para você. Distraído com elas, não percebe que as paredes estão se fechando até estarem quase encostando em você. '
          'Vendo a velocidade com que elas se aproximam e a distância para sair do corredor, você percebe que não terá tempo de correr e precisará de um jeito de desarmar.')
    bt.enter()
    
    flag = False
    flag_armadilha = False
    n = 0 #Contador para que o jogador tenha apenas duas tentativas
    while flag == False or flag_armadilha == False: #Garante que o input se repita caso o jogador digite uma opção inválida e permite que o jogador tente mais uma vez
        print('\nVocê tenta parar a armadilha usando força, inteligência ou sorte?\n1 - força\n2 - inteligência\n3 - sorte')
        armadilha = input('>>>')
        if armadilha == '1': #Tenta desarmar usando força
            flag = True
            print('\nVocê apoia as costas e as mãos em uma parede e coloca os dois pés na outra. As paredes estão próximas o bastante para que seus joelhos se dobrem.'
                  'Você aplica toda sua força nas pernas, empurrando a parede.')
            #Teste de força. Se a força do jogador for maior que a da armadilha ele consegue parar as paredes.
            forca = teste_atributo(jogador['força'], 8, 9) 
            if forca == True: #Passa no teste
                flag_armadilha = True
                print('Elas param de se aproximar e você intensifica a força. Um estalo se faz ouvir em todo o corredor e as paredes voltam para suas posições iniciais.')
                print('\nParabéns! Você conseguiu quebrar o sistema da armadilha e pode seguir seu caminho!')
            if forca == False: #Não passa no teste
                print('Por um instante, as paredes param de se aproximar, mas dura apenas alguns segundos antes de voltarem a se aproximar. Você cai no chão e sente uma onda de dor subir por seu corpo.')
                jogador['hp'] -= 5
                bt.game_over(jogador)
        elif armadilha == '2': #Tenta desativar usando inteligência
            flag = True
            print('Você olha os itens que tem consigo e tenta elaborar um plano para desativar o sistema da armadilha.')
            #Teste de inteligência. Se passar, ele consegue desativar o sistema.
            inteligencia = teste_atributo(jogador['inteligência'], 8, 9) 
            if inteligencia == True: #Passa no teste
                flag_armadilha = True
                print('Você observa atentamente as paredes e consegue ver através de um buraco na parede o mecanismo da armadilha. Pega então uma pedra no chão e joga nesse buraco. '
                      'Escuta-se um barulho de algo quebrando e as paredes param de se aproximar.\n\nParabéns! Você conseguiu travar o sistema da armadilha!')
            if inteligencia == False: #Não passa no teste
                print('Você tenta parar as paredes prendendo sua ARMA em uma fresta entre a parede e o chão. Até funciona por um tempo e você começa a correr para sair do corredor, '
                      'mas então a ARMA se solta e acerta seu braço esquerdo. As paredes voltam a se fechar e agora você tem menos tempo para encontrar uma solução.')
                jogador['hp'] -= 5
                bt.game_over(jogador)
        elif armadilha == '3': #Tenta desarmar usando a sorte
            flag = True
            print('Você resolve confiar na sorte e tenta encontrar algo que pare a armadilha, aliás os moradores precisam passar de alguma forma.')
            #Teste de sorte. Se a sorte do jogador for maior que a da armadilha, ele encontra o botão para desligar o sistema.
            sorte = teste_atributo(jogador['sorte'], 8, 9)
            if sorte == True: #Passa no teste
                flag_armadilha = True
                print('Você analisa atentamente as paredes e encontra um pequeno botão vermelho. Ao pressioná-lo, escuta um click e as paredes param de se aproximar.')
                print('\nParabéns! Você conseguiu desligar o sistema da armadilha e pode seguir seu caminho!')
            elif sorte == False: #Não passa no teste
                print('Você procura nas paredes atentamente e vê um botão verde. Pensando ser a solução, o aperta, contudo uma saraivada de espinhos sai da parede, um deles te acertando no ombro.')
        if flag_armadilha == False and flag == True: #Checa se o jogador conseguiu desativar a armadilha
            print('As paredes continuam se fechando ao seu redor.')
            bt.enter()
            n += 1
            if n == 2:
                print('Seu tempo acabou. As paredes se fecham sobre você, colocando um fim a sua jornada.')
                jogador['hp'] = 0
                bt.game_over(jogador)
                
        if flag == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
            
    bt.enter()
    print('Finalmente você consegue se livrar da armadilha e segue seu caminho, que faz uma curva à esquerda antes de outra porta aparecer.')
    bt.enter()
    sala_atual = 4 #Manda o jogador para a sala 4
    return sala_atual

def salao_final(jogador):
    print('Após subir toda a escada, você chega em uma sala no alto da torre. O artefato estava lá, em cima de uma mesa e você corre pegá-lo.')
    #Acrescentar o que acontece ao pegar o artefato e breve descrição da sala
    bt.enter()
    print('Uma risada faz você olhar para o sofá. Um homem se levanta e te olha. Surpreso, você percebe ser o mesmo mago que enfrentou ateriormente.')
    #Adicionar pequeno diálogo
    bt.enter()
    #Dicionário do Boss2 (ajustar atributos)
    boss2 = {"nome" : 'Boss2',    'hp': 85,  'defesa': 3, 'força': 1, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}
    bt.batalha(boss2, jogador, True)
    bt.enter()
    print('Após finalmente derrotá-lo, você percebe que o artefato realmente te deixa mais forte. Você poderia ser o mais forte do reino com ele. '
          'Voltar a ser um homem livre, obter todas as recompensas do rei deve ser bom, mas será que vale a pena? As opções passam por sua mente e você precisa decidir logo.')
    bt.enter()
    flag = False
    while flag == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('Você irá devolver o artefato ou fugir com ele?\n1 - Entregar\n2 - Fugir')
        final = input('>>>')
        if final == '1': #Final 1 - o jogador devolve o artefato para o rei
            flag = True
            print('Você tinha uma vida antes de ser preso e gostaria muito de recuperá-la. Sem perder tempo, você sai da casa, percebendo que agora todas as portas estão abertas. '
                  'Agora que conhece o caminho, não tem problemas para voltar para o castelo. O mesmo soldado que te guiou para fora te espera nos portões. Você é guiado até a presença do rei.')
        elif final == '2': #Final 2 - o jogador foge com o artefato
            flag = True
            print('Sua vida anterior não era assim tão boa e nada que o rei possa oferecer é tão bom quanto à grande quantidade de poder que o artefato lhe fornece. Além de tudo, não importa o resultado da guerra se você já estiver longe.')
        if flag == False: #Checa se o jogador digitou um comando inválido
            print('Comando não reconhecido, tente novamente.')
    

def final(jogador, lugar):
    '''
    Define os acontecimentos e sua ordem dentro da mansão
    Entrada: dicionário com os atributos do jogador e string com o local que ele foi 
    '''
    print(f'Após finalmente atravessar o {lugar}, seu destino surge frente aos seus olhos.')
    print('Uma casa comum, de pedra cinza, sem muitos detalhes a vista. O que chama a atenção, porém, é uma grande torre do lado direito, sem portas ou janelas. '
          'A porta preta da frente não é exatamente convidativa, mas mesmo assim você adentra o local.')
    bt.enter()
    sala1(jogador)
    while 2 <= sala_atual <= 8:
        if sala_atual == 2:
            sala2(jogador)
        elif sala_atual == 3:
            sala3(jogador)
        elif sala_atual == 4:
            sala4(jogador)
        elif sala_atual == 5:
            sala5(jogador)
        elif sala_atual == 6:
            sala6(jogador)
        elif sala_atual == 7:
            sala7(jogador)
        elif sala_atual == 8:
            sala8(jogador)
    salao_final(jogador)
    print('Você terminou o jogo!\n\nDeseja jogar outra vez:\n1 - sim\n2 - não')
    jogar_nov = input('>>>')
    if jogar_nov == '1':
        restart_program()
    elif jogar_nov == '2':
        sys.exit()
