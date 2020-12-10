'''
Módulo com as funções que descrevem os acontecimentos da última parte do jogo
As funções salas definem o que o jogador pode encontrar em cada sala'''

import Batalha as bt
import sys

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
    print('No instante em que encosta na maçaneta, você sente algo espetar a palma de sua mão. A porta se abre e você observa o \ninterior. \n'
          'Diversas prateleiras contendo frascos de poções. Cada poção possui a figura de um animal no rótulo e cada prateleira é \ncomposta de poções do mesmo animal.\n '
          'Além disso, há também uma grande gaveta trancada. Seu olhar recai sobre um bilhete caído aos seus pés e você se abaixa \npara lê-lo.\n')
    bt.enter()
    print('\nTEXTO DO BILHETE:\n"Ao maldito curioso, uma punição merecida\nUma dose de veneno e um mistério a resolver\n8 bebidas, 5 efeitos, 2 chances\n'
          'Em uma, a morte certa, em outra a cura garantida\nAo ladrão esperto, uma recompensa esperada"')
    bt.enter()
    print('\nVERSO DO BILHETE:\n"Aquele que o mata pode o salvar da vida como tal\nAquele que salta na floresta faz a queda se aparar\n'
          'Aquele que pelo chão segue o afunda na terra final\nAquele que pela água segue o leva a recuar\n'
          'Aquele que cisca o fará se sentir como um igual\nAqueles que sobram não vão além do natural"\n')
    bt.enter()
    print('Você percebe nesse momento uma mancha verde crescendo na palma de sua mão, partindo de onde sentiu espetar ao abrir o \narmário.\n '
          'Também presta atenção nos animais nos frascos e vê a seguinte ordem, de cima para baixo: SERPENTE, GALINHA, PEIXE, GATO,\n URSO, ÁGUIA, MACACO e CORVO\n')
    bt.enter()
    flag_enigma = False #Flag para resposta de qual poção beber
    flag_veneno = False #Flag para checar se escolheu a poção certa
    while flag_enigma == False or flag_veneno == False: #Garante que o input se repita caso o jogador digite uma opção inválida e tente mais uma vez
        print('\u001b[37;1mQual poção você irá beber?\n (1) SERPENTE\n (2) GALINHA\n (3) PEIXE\n (4) GATO\n (5) URSO\n (6) ÁGUIA\n (7) MACACO\n (8) CORVO\n')
        pocao = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{pocao}\u001b[0m\n")

        if pocao == '1': #Bebe a poção da Serpente - morte instantanea
            flag_enigma = True
            print('Você bebe a poção e sente um gosto amargo dominar sua boca. Nos primeiros segundos nada acontece e a mancha para de \ncrescer em sua mão.\n '
                  'Mas repentinamente suas pernas falham e você cai no chão. Sua energia se esvai e a última coisa que você escuta é uma \nrisada aguda.\n')
            jogador['hp'] = 0
            bt.game_over(jogador)
        elif pocao == '2': #Bebe a poção da Galinha - vira uma galinha
            flag_enigma = True
            print('Em um único gole você bebe todo o conteúdo do frasco. Uma sensação parecida com cócegas percorre seu corpo e você tem a \nsensação de que seu interior está queimando e a sala está crescendo.\n '
                  'Ao tentar falar, apenas cacareja. Você vê seu reflexo em um pequeno espelho na parte interna da porta do armário. Você \nvirou uma galinha!\n')
            bt.enter()
            print('\nDesesperado, sai pulando pela sala, pensando em como enfrentaria o guardião da relíquia nessa forma. Alguns minutos se \npassam e a sensação de que seu corpo está queimando retorna.\n '
                  'Você fecha os olhos quando todos seus ossos doem e, quando abre novamente, voltou ao normal e a mancha verde agora tem \no dobro do tamanho.\n')
            bt.enter()
            dano += 5 #Aumenta o dano em 5 pontos
            n += 1
        elif pocao == '3' or pocao == '7': #Bebe a poção do Peixe ou do Macaco - diminui metade do dano
            flag_enigma = True
            dano //= 2
            n += 1
            print('A poção que você bebe possui um estranho gosto salgado. Aparentemente nada acontece, mas ao observar mais atentamente \nnota que o tom de verde da crescente mancha na sua mão está mais claro.\n')
            bt.enter()
        elif pocao == '4' or pocao == '6' or pocao == '8': #Bebe a poção do Gato, da Águia ou do Corvo - nada acontece
            flag_enigma = True
            print('Você cheira a poção antes de beber, mas ela é inodora. Tampouco tem algum sabor. Você logo percebe que é apenas água!\n')
            bt.enter()
            n += 1
        elif pocao == '5': #Bebe a poção do Urso - antídoto do veneno
            flag_enigma = True
            flag_veneno = True
            print('Você não consegue evitar fazer uma careta ao sentir um péssimo gosto azedo ao beber do frasco. O enjôo é forte e você \nquase vomita. Olha para sua mão com expectativa e vê a mancha começar a diminuir até sumir.\n')
            bt.enter()
            print('Uma olhada mais atenta ao frasco revela uma pequena chave no seu interior. Você o joga no chão e ele se quebra em vários\ncacos, liberando a chave, que se encaixa perfeitamente na fechadura da gaveta.\n')
            flag_gaveta = False #Flag para a resposta de abrir ou não a gaveta
            while flag_gaveta == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('\u001b[37;1mDeseja abrir a gaveta:\n (1) sim\n (2) não\n')
                gaveta = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{gaveta}\u001b[0m\n")

                if gaveta == '1': #Abre a gaveta
                    flag_gaveta = True
                    print('Você gira a chave e a gaveta se abre. 3 itens no interior chamam a sua atenção:\n'
                          '1 - Um frasco com uma poção verde\n2 - Um frasco com uma poção vermelha\n3 - Uma espada longa\n')
                    #Teste de inteligência para saber se o jogador reconhece as poções
                    pocoes = teste_atributo(jogador['inteligência'])
                    if pocoes == True: #Passa no teste
                        print('Ao analisar os frascos, você chega a conclusão de que a poção vermelha é diferente da poção de cura que conhece e a \nverde é uma poção de fortalecimento.\n')
                    bt.enter()
                    flag_pocao = False #Flag para a resposta de beber ou não a poção
                    while flag_pocao == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                        print('\u001b[37;1mDeseja tomar as poções?\n (1) Sim, as duas\n (2) Apenas a vermelha\n (3) Apenas a verde\n (4) Não\n')
                        pocao = input('>>>')
                        bt.delete_last_lines(1)
                        print(f">>>{pocao}\u001b[0m\n")

                        if pocao == '1': #Bebe as duas poções
                            flag_pocao = True
                            print('\nVocê bebe primeiro a poção verde. Ela não possui sabor algum, mas você se sente mais forte de alguma forma.\n')
                            jogador['força'] += 1
                            print(f'\nSua força: {jogador["força"]}\n')
                            bt.enter()
                            print('Confiante, você bebe a poção vermelha em seguida. Ela possui um suave sabor doce e você logo esvazia o frasco. Contudo \nsua cabeça começa a latejar e você precisa se apoiar na parede para não cair.\n')
                            jogador['hp'] -= 9
                            print(f'\nVocê levou 9 pontos de dano. Seu hp: {jogador["hp"]}')
                            bt.enter()
                            bt.game_over(jogador) #Checa se deu game over
                        elif pocao == '2': #Bebe apenas a poção vermelha
                            flag_pocao = True
                            print('Confiante, você bebe a poção vermelha. Ela possui um suave sabor doce e você logo esvazia o frasco. Contudo sua cabeça \ncomeça a latejar e você precisa se apoiar na parede para não cair.\n')
                            bt.enter()
                            jogador['hp'] -= 9
                            print(f'\nVocê levou 9 pontos de dano. Seu hp: {jogador["hp"]}')
                            bt.game_over(jogador) #Checa se deu game over
                            bt.enter()
                        elif pocao == '3': #Bebe apenas a poção verde
                            flag_pocao = True
                            print('\nVocê bebe a poção verde. Ela não possui sabor algum, mas você se sente mais forte de alguma forma.\n')
                            jogador['força'] += 1
                            print(f'\nSua força: {jogador["força"]}')
                            bt.enter()
                        elif pocao == '4': #Não bebe nenhuma poção
                            flag_pocao = True
                            print('Você não pode assumir riscos desnecessário, então simplesmente fecha a gaveta.\n')
                        if flag_pocao == False: #Checa se o jogador digitou um comando inválido
                            print('\nComando não reconhecido, tente novamente.\n')
                    flag_espada = False #Flag para resposta de pegar a espada
                    while flag_espada == False: #Garante que o imput se repita caso o jogador digite uma opção inválida
                        print('\u001b[37;1mDeseja substituir sua arma atual pela espada?\n (1) sim\n (2) não\n')
                        pegar = input('>>>')
                        bt.delete_last_lines(1)
                        print(f">>>{pegar}\u001b[0m\n")

                        if pegar == '1': #Pega a espada
                            flag_espada = True
                            print(f'Você deixou {jogador["arma"]} e pegou a espada!\n')
                            #Dicionário com os atributos da espada
                            espada_longa = {'nome': 'espada longa', 'atributo': 'FOR', 'dano': '3-5', 'min': 3, 'max': 5}
                            jogador['arma'] = espada_longa #definir atributos da espada
                        elif pegar == '2': #Não pega a espada
                            flag_espada = True
                            print('Você deixa a espada onde ela está.\n')
                        if flag_espada == False: #Checa se o jogador digitou um comando inválido
                            print('\nComando não reconhecido, tente novamente.\n')
                elif gaveta == '2': #Não abre a gaveta
                    flag_gaveta = True
                    print('É melhor não perder tempo ou se arriscar, pode ser apenas mais uma armadilha.\n')
                if flag_gaveta == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')
        if flag_enigma == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')
        if n == 2: #Checa se o jogador já fez duas tentativas
            flag_enigma = True
            flag_veneno = True
            print('Você se lembra da frase do bilhete que diz que você tem apenas duas chances. A mancha já cobre toda sua mão. Subtamente,\nvocê sente como se algo tivesse atingido seu coração com força e a mancha desaparece.\n')
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
    print('Ao entrar, você chega em uma grande sala. Os dois sofás velhos ao redor de uma mesa de centro, juntamente com uma \nlareira apagada na parede da direita e a falta de decoração fazem o ambiente parecer frio e abandonado.\n '
          'O lugar estava vazio até um pequeno Goblin entrar. Ele não perde tempo e logo te ataca!\n')
    bt.enter()
    #Dicionário do Goblin
    Goblin = {'nome': 'Goblin', 'hp': 55,  'defesa': 4, 'força': 3}
    bt.batalha(Goblin, jogador, True)
    Goblin["hp"] = 55
    bt.enter()
    print('Os sons da batalha atraem um Segurança para a sala!\n')
    bt.enter()
    #Dicionário do Segurança
    Seguranca = {'nome': 'Segurança', 'hp': 60,  'defesa': 5, 'força': 3}
    bt.batalha(Seguranca, jogador, True)
    bt.enter()
    #Nesse momento, o jogador tem dois caminhos a seguir, um mais longo e um mais curto
    print('Há duas portas de madeira lisa na sala: uma na parede em frente a você e outra à esquerda.\n')
    flag_porta = False #Flag para resposta de qual caminho seguir
    while flag_porta == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mQual você escolhe?\n (1) frente\n (2) esquerda\n')
        prox = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{prox}\u001b[0m\n")

        if prox == '1': #Segue pela porta da frente
            sala_atual = 7 #Manda o jogador para a sala 7
            flag_porta = True
        elif prox == '2': #Segue pela porta da esquerda
            sala_atual = 5 #Manda o jogador para a sala 5
            flag_porta = True
        if flag_porta == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')
    return sala_atual

def sala2(jogador):
    '''
    Descreve os acontecimentos da sala 2 - busca nas caixas (comida, poções, batalha e encontrar espada),
    batalha no corredor e escolha de caminho
    Argumento: dicionário dos atributos do jogador
    Saída: sala_atual
    '''
    global sala_atual
    print('A porta abre direto para um pequeno depósito. No instante que você entra, a porta se fecha e tranca sozinha.\n')
    print('Todas as paredes são cobertas por estantes de metal simples, todas cheias de caixas de diferentes tamanhos e formatos.\n')
    bt.enter()
    flag_caixa = False #Flag para resposta de olhar ou não as caixas
    while flag_caixa == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mDeseja olhar dentro das caixas?\n (1) sim\n (2) não\n')
        caixa = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{caixa}\u001b[0m\n")

        if caixa == '1': #Olha as caixas
            flag_caixa = True
            print('\nConforme você mexe nas caixas, percebe que a maioria contém apenas roupas e comidas de aparência suspeita.\n')
            bt.enter()
            flag_comida = False #Flag para resposta de comer ou não
            while flag_comida == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('\u001b[37;1mDeseja comer algo?\n (1) sim\n (2) não\n')
                comida = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{comida}\u001b[0m\n")

                if comida == '1': #Come
                    flag_comida = True
                    #Teste de sorte para ver se a comida está estragada ou não
                    estraga = teste_atributo(jogador['sorte'], 6, 8)
                    if estraga == True: #Passa no teste - não está estragada
                        print('\nA fome fala mais alto e você pega um pão escuro. Estava um pouco salgado e com gosto de queimado, mas até que estava bom.\n '
                              'A fome passa e você sente suas energias renovadas!\n')
                        jogador['hp'] += 5
                    elif estraga == False: #Não passa no teste - está estragada
                        print('\nA fome fala mais alto e você pega um pão com um cheiro doce. Nas primeiras mordidas não sente nada, mas depois de comer metade um enjôo o faz vomitar.\n')
                        jogador['hp'] -= 5
                    print(f'Seu hp: {jogador["hp"]}')
                    bt.enter()
                    bt.game_over(jogador) #Checa se deu game over
                elif comida == '2': #Não come
                    flag_comida = True
                    print('\nApesar da fome, melhor não arriscar comer algo estragado.\n')
                    bt.enter()
                if flag_comida == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')

            print('\nVocê ouve um barulho estranho vindo de uma caixa, mas continua mexendo e um escorpião do tamanho de um filhote de \ncachorro pula da caixa.\n')
            bt.enter()
            #Dicionário dos atributos do escorpião (ajustar atributos)
            Escorpiao_enorme = {'nome': 'Escorpião enorme', 'hp': 60,  'defesa': 4, 'força': 3}
            bt.batalha(Escorpiao_enorme, jogador, True)
            bt.enter()
            print('Após derrotar o escorpião, você olha a caixa em que ele estava e encontra uma espada em seu interior!\n')
            flag_espada = False #Flag para resposta de pegar ou não a espada
            while flag_espada == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('\u001b[37;1mDeseja pegar a espada?\n (1) sim\n (2) não\n')
                pegar = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{[pegar]}\u001b[0m\n")

                if pegar == '1': #Pega a espada
                    flag_espada = True
                    print(f'Você deixa sua arma no local e pega a espada!\n')
                    #Dicionário com os atributos da espada
                    espada_longa = {'nome': 'espada longa', 'atributo': 'FOR', 'dano': '3-5', 'min': 3, 'max': 5}
                    jogador['arma'] = espada_longa #definir atributos da espada
                elif pegar == '2': #Não pega a espada
                    flag_espada = True
                    print('Você deixa a espada onde ela está.\n')
                if flag_espada == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')
            bt.enter()
            print('Em outra caixa, você encontra diferentes garrafas. Enquanto abre uma por uma, vê que a maioria é água ou café velho, \nexceto por três delas.\n '
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
                print('\u001b[37;1mDeseja beber a poção azul?\n (1) sim\n (2) não')
                pocao_azul = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{pocao_azul}\u001b[0m\n")

                if pocao_azul == '1': #Bebe a poção
                    flag_pa = True
                    print('Você bebe a poção, que não possui sabor algum, mas sente que, de alguma forma, está mais forte.\n')
                    jogador['força'] += 1
                    print(f'Sua força: {jogador["força"]}\n')
                elif pocao_azul == '2': #Não bebe a poção
                    flag_pa = True
                    print('Não é hora de correr riscos, deixa essa garrafa onde está.\n')
                if flag_pa == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')
            bt.enter()
            flag_pl = False #Flag para resposta de beber ou não a poção laranja
            while flag_pl == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('\u001b[37;1mDeseja beber a poção laranja?\n (1) sim\n (2) não\n')
                pocao_laranja = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{pocao_laranja}\u001b[0m\n")

                if pocao_laranja == '1': #Bebe a poção
                    flag_pl = True
                    print('A doce poção com sabor de suco de laranja te passa a sensação de estar revigorado.\n')
                    jogador['hp'] += 25
                    print(f'Sua vida: {jogador["hp"]}')
                elif pocao_laranja == '2': #Não bebe a poção
                    flag_pl = True
                    print('Apesar do cheiro doce e saboroso, as aparências podem enganar e não tem motivo para arriscar. Você fecha a garrafa e a \ndevolve no local que pegou.\n')
                if flag_pl == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')
            bt.enter()
            flag_pr = False #Flag para resposta de beber ou não a poção roxa
            while flag_pr == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('\u001b[37;1mDeseja beber a poção roxa?\n (1) sim\n (2) não\n')
                pocao_roxa = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{pocao_roxa}\u001b[0m\n")

                if pocao_roxa == '1': #Bebe a poção
                    flag_pr = True
                    print('A bebida tem uma consistência estranha e você se arrepende de beber. Uma fumaça roxa sai de sua boca e você se sente \nrepentinamente mais cansado.\n')
                    jogador['hp'] -= 15
                    print(f'Seu hp: {jogador["hp"]}')
                elif pocao_roxa == '2': #Não bebe a poção
                    print('A poção não é confiável e você tem coisa melhor para fazer do que ficar bebendo de garrafas estranhas.\n')
                    flag_pr = True
                if flag_pr == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')
        elif caixa == '2': #Não olha as caixas
            flag_caixa = True
            print('\nVocê não tem tempo para ficar mexendo em nada, está com pressa para encontrar a relíquia.\n')
        if flag_caixa == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')
    bt.enter()
    print('Uma saída sem porta leva a um caminho que vira à esquerda em um longo corredor com apenas uma tocha no meio do caminho \npara iluminar tudo.\n '
            'Você segue em frente e a única opção ao final é virar à esquerda outra vez.\n')
    bt.enter()
    print('Um estranho morto vivo estava parado e te ataca!\n')
    bt.enter()
    #Dicionário com os atributos do Morto Vivo:
    Morto_vivo = {'nome': 'Morto vivo', 'hp': 45,  'defesa': 2, 'força': 5}
    bt.batalha(Morto_vivo, jogador, True)
    bt.enter()
    print('Ao seguir pelo corredor, você vê que na parede esquerda existem duas ramificações.\n')
    flag_ramif = False #Flag para resposta de qual ramificação seguir
    while flag_ramif == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mDeseja seguir pela primeira ou pela segunda?\n (1) primeira\n (2) segunda\n')
        prox = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{prox}\u001b[0m\n")

        if prox == '1': #Segue pela primeira ramificação
            print('\nVocê vira na primeira ramificação e a péssima iluminação mostra apenas a porta aberta de uma sala escura ao final do corredor.\n')
            sala_atual = 3 #Manda o jogador para a sala 3
            flag_ramif = True
        elif prox == '2': #Segue pela segunda ramificação
            print('\nVocê vira na segunda ramificação e segue por outro corredor escuro até encontrar uma porta fechada. Você tenta abrir e, \npara sua sorte, estava destrancada.\n')
            sala_atual = 6 #Manda o jogador para a sala 6
            flag_ramif = True
        if flag_ramif == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')
    return sala_atual

def sala3(jogador):
    '''
    Descreve os acontecimentos da sala 3 - batalha, baú com poções, cochilo
    Argumento: dicionário com os atributos do jogador
    Saída: sala_atual
    '''
    global sala_atual
    print('Quando você entra na sala, a luz se acende e a porta se fecha atrás de você. Apenas para ter certeza, você tenta \nabrí-la, mas já está trancada.\n')
    print('Três beliches e um armário vazio são, aparentemente, a única mobilia do local. Um Goblin dorme em uma das camas, mas \nquando a luz acende ele levanta e não perde tempo antes de te atacar.\n')
    #dicionário com os atributos do Goblin
    Goblin = Goblin = {'nome': 'Goblin', 'hp': 55,  'defesa': 4, 'força': 3}
    bt.enter()
    bt.batalha(Goblin, jogador, True)
    bt.enter()
    print('Você vê, no canto esquerdo da sala, um pequeno baú dourado com a tampa aberta.\n')
    flag_bau = False #Flag para resposta de ver ou não o baú
    while flag_bau == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mDeseja ver seu conteúdo?\n (1) sim\n (2) não\n')
        bau = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{bau}\u001b[0m\n")

        if bau == '1': #Vê o baú
            flag_bau = True
            print('\nNo interior do baú há dois frascos: um deles possui um líquido viscoso e esbranquiçado e o outro um líquido vermelho.\n')
            #Testes de inteligencia do jogador para saber se ele reconhece ou não as poções
            teste_pb = teste_atributo(jogador['inteligência'], 7, 10) #Teste para a poção branca
            teste_pv = teste_atributo(jogador['inteligência'], 5, 7) #Teste para a poção vermelha
            if teste_pb == True and teste_pv == True: #Reconhece as duas
                print('Você reconhece as poções de um livro, sendo a vermelha uma de cura e a esbranquiçada de experiência\n')
            elif teste_pb == False and teste_pv == True: #Reconhece apenas a vermelha
                print('Você não sabe o que é a poção branca, mas sabe que a vermelha aumentará sua vida.\n')
            elif teste_pv == False: #Não reconhece nenhuma
                print('Você não sabe o efeito de nenhuma das poções.\n')
            flag_pb = False #Flag para respota de beber ou não a poção branca
            while flag_pb == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                print('\u001b[37;1mDeseja tomar a poção esbranquiçada?\n (1) sim\n (2) não\n')
                poção_branca = input('>>>')
                bt.delete_last_lines(1)
                print(f">>>{poção_branca}\u001b[0m\n")

                if poção_branca == '1': #Bebe
                    flag_pb = True
                    bt.passar_nivel(jogador)
                elif poção_branca == '2': #Não bebe
                    flag_pb = True
                    print('Desconfiado, você decide ignorar o frasco com o líquido branco.\n')
                if flag_pb == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')
            flag_pv = False #Flag para resposta de beber ou não a poção vermelha
            while flag_pv == False: #Garante que o input se repita caso o jogador digite uma opção inválida
                bt.enter()
                print('\u001b[37;1mDeseja tomar a poção vermelha?\n (1) sim\n (2) não\n')
                poção_vermelha = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{poção_vermelha}\u001b[0m\n")

                if poção_vermelha == '1': #Bebe a poção
                    flag_pv = True
                    jogador['hp'] += 25 #Aumenta a vida do jogador
                    print('Você ganhou 25 pontos de vida!\n')
                    print(f'Seu hp: {jogador["hp"]}\n')
                    bt.enter()
                elif poção_vermelha == '2': #Não bebe a poção
                    flag_pv = True
                    print('Você prefere não arriscar e não bebe a poção vermelha.\n')
                if flag_pv == False: #Checa se o jogador digitou um comando inválido
                    print('\nComando não reconhecido, tente novamente.\n')
        elif bau == '2': #Não abre o baú
            flag_bau = True
            print('Você ignora o baú e nada acontece.\n')
        if flag_bau == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')
    print('Você olha para as camas e se pergunta se um rápido cochilo pode ser bom para recuperar as energias ou se é melhor não \nperder tempo.\n')
    flag_cochilo = False  #Flag para resposta de cochilar ou não
    while flag_cochilo == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mO que você escolhe?\n (1) Cochilar\n (2) Não perder tempo\n')
        cochilo = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{cochilo}\u001b[0m\n")

        if cochilo == '1': #Dorme
            flag_cochilo = True
            print('Você deita em uma das camas e aproveita para descansar, em estado semi-alerta. Alguns minutos se passam e você se sente \ndescansado e recuperado.\n')
            jogador['hp'] += 20
            print(f'Você recuperou 20 ponts de hp. Sua vida: {jogador["hp"]}\n')
        elif cochilo == '2': #Não dorme
            flag_cochilo = True
            print('É arriscado demais baixar a guarda desse jeito, melhor não.\n')
        if flag_cochilo == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')
    bt.enter()
    print('Além da porta pela qual você entrou, existem outras duas, mas apenas uma na parede oeste está destrancada e você segue por ela.\n')
    sala_atual = 6 #Manda o jogador para a sala 6
    return sala_atual

def sala4(jogador):
    '''
    Descreve os acontecimentos da sala 4 - armadilha do armário
    Entrada: dicionário com os atributos do jogador
    Saída: sala_atual
    '''
    global sala_atual
    print('Uma vela em cima de uma mesa no centro do cômodo fornece uma fraca iluminação. Estantes com pedaços de armadura e \narmamentos quebrados ou não terminados indicam que o local devia ser utilizado como arsenal anteriormente.\n')
    bt.enter()
    print('Há também um armário de aço com uma única porta cuja maçaneta parece ser de ouro maciço com um pequeno diamante no centro.\n')
    #Teste de inteligencia para saber se o jogador identifica algo estranho
    armadilha = teste_atributo(jogador['inteligência'])
    if armadilha == True: #Identifica algo estranho
        print('Você percebe que a maçaneta possui uma mancha incomum para uma peça de ouro e que o diamante é falso, além de ter algo \npequeno e fino na superfície apontando para fora.\n')
    flag_armario = False #Flag para a resposta de abrir o armário
    while flag_armario == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mVocê tenta abrí-lo?\n (1) sim\n (2) não\n')
        armario = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{armario}\u001b[0m\n")

        if armario == '1': #Abre o armário
            flag_armario = True
            armadilha_armario(jogador)
        elif armario == '2': #Não abre o armário
            flag_armario = True
            print('O que pode ser mais importante que recuperar a relíquia? Seja lá o que tem nesse armário, a recompensa do rei deve ser melhor.\n')
        if flag_armario == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')
    bt.enter()
    print('No meio da parede à esquerda, uma porta com um enorme X vermelho pintado fecha a única saída existente já que, como tem \nacontecido, a porta pela qual você entrou se trancou sozinha.\n '
          'Você sai por ela e, após alguns passos, se depara com uma porta aberta de uma sala escura.\n')
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
    print('Você decide seguir pela porta da esquerda, pensando que poderia tentar o outro caminho caso necessário, porém a porta se\ntranca sozinha assim que você passa por ela. Sem outra opção, você olha a sala em que entrou.\n '
          'Não há nenhum móvel no local, apenas o que parece ser uma grande escultura. Mas quando você se aproxima ela se levanta e\nse vira para você, que percebe que na verdade a estátua era um Troll adormecido!\n')
    #Dicionário com os atributos do troll
    Troll = {'nome': 'Troll', 'hp': 70,  'defesa': 5, 'força': 2}
    bt.enter()
    bt.batalha(Troll, jogador, True)
    bt.enter()
    print('Assim que o Troll morre, um leve tremor percorre a sala. O contorno de uma porta que não existia antes surge na parede a\nsua frente. Ela se abre e você continua sua busca pelo artefato.\n '
          'O corredor mal iluminado vira à esquerda e depois à direita antes de chegar a uma porta feita de grossas barras de ferro\ncruzadas formando uma grade, como a prisão de algo ou alguém.\n')
    bt.enter()
    sala_atual = 8 #Manda o jogador para a sala 8
    return sala_atual

def sala6(jogador):
    global sala_atual
    print('Ao adentrar a sala, você finalmente o vê. Sentado em uma cadeira, com os braços apoiados na mesa, te encarando como se \nesperasse sua chegada. Contudo, o artefato não está em nenhum lugar visível.\n '
          'Na verdade, além da cadeira e da mesa, não há mais nada no cômodo.\n')
    bt.enter()
    #Discurso do Guardião
    print('- Eu sabia que era apenas uma questão de tempo até alguém chegar. Não importo qual lado você representa, mas não posso \ndeixar qualquer um roubar essa relíquia, seja qual for o motivo. Talvez você não\n saiba, mas ela '
          'aumenta muito a força do seu portador e intefere também em seu exército. Minha missão nesse mundo é protegê-la não \nimporta a que custo.\n')
    bt.enter()
    print('Sem esperar uma resposta, o guardião se levanta e te ataca sem nenhuma misericórdia.\n')
    bt.enter()
    #Dicionário com os atributos da primeira parte do boss
    Guardiao = {'nome': 'Guardião da relíquia', 'hp': 75,  'defesa': 5, 'força': 4}
    bt.batalha(Guardiao, jogador, True)
    sala_atual = 0 #Encerra a parte das salas para seguir para o final
    print('Após derrotar o guardião, ele se desfaz em um pequeno monte de poeira verde. Você faz uma busca pela sala, mas não \nencontra nada. Todas as portas estão trancadas e, aparentemente, não há uma saída.\n '
          'Começando a acreditar que está no lugar errado, você se senta na cadeira em que ele estava e vê um discreto botão \ncamuflado na lateral do tampo da mesa. \n'
          'Você o aperta, o teto começa a se mexer e uma nuvem de poeira cai por todo o local. Quando finalmente a poeira abaixa, \nvocê vê uma escada circular no canto da sala e resolve subir.\n')
    return sala_atual

def sala7(jogador):
    global sala_atual
    print('\nApós dar dois passos para a frente e virar à direita, você segue por um corredor não muito longo e pouco iluminado até \nchegar em outra porta. Você entra e escuta um barulho de tranca.\n '
          'Surpreso, tenta abrir a porta, mas ela está trancada.\n')
    bt.enter()
    print('Uma análise rápida e você percebe se tratar de uma cozinha. Um fogão simples e sem lenha num canto, uma pia sem torneira\ne uma geladeira sem porta fazem o local parecer abandonado há anos. \n'
          'Uma pilha de ossos no canto começa a se mexer, formando um esqueleto vivo que te ataca!\n')
    bt.enter()
    #Dicionário com os atributos do Esqueleto parte 1
    Esqueleto_1 = {'nome': 'Esqueleto', 'hp': 65,  'defesa': 4, 'força': 2}
    bt.batalha(Esqueleto_1, jogador, True)
    bt.enter()
    #Dicionário com os atributos do Esqueleto remontado
    Esqueleto_2 = {'nome': 'Esqueleto', 'hp': 35,  'defesa': 6, 'força': 5}
    print('Você pensa ter derrotado o esqueleto, mas assim que se vira, escuta barulhos de ossos batendo e gira outra vez a tempo \nde ver o esqueleto se montando e ficando em pé outra vez.\n')
    bt.enter()
    bt.batalha(Esqueleto_2, jogador, True)
    bt.enter()
    print('Dessa vez, ao derrortá-lo você separa os ossos, prendendo um pouco dentro do forno, um tanto na geladeira e um tanto na \npia, utilizando alguns pedaços de corda que encontrou para amarrá-lo.\n')
    bt.enter()
    print('Nesse momento, há apenas um caminho para seguir, uma porta branca à direita.\n')
    sala_atual = 2
    return sala_atual

def sala8(jogador):
    global sala_atual
    print('A única tocha no alto da parede é suficiente para você ver entender que entrou na jaula de um grande Javali. O animal \ntem certa de 2 metros de comprimento, o pelo cinza está sujo e ele parece faminto, já que a única coisa além dele é um balde com água.\n '
          'Como esperado, ele olha para você, pronto para devorar o novo jantar.\n')
    bt.enter()
    #Dicionário do Javali
    Javali = {'nome': 'Javali', 'hp': 65,  'defesa': 5, 'força': 3}
    bt.batalha(Javali, jogador, True)
    bt.enter()
    print('O Javali desaparece quase por inteiro na frente dos seus olhos, restando apenas sua pele. Você a observa e vê que está \nlimpa por dentro e é mais leve do que parece.\n')
    flag = False
    while flag == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mDeseja vestir a pele do javali?\n (1) sim\n (2) não\n')
        pele = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{pele}\u001b[0m\n")

        if pele == '1':
            flag = True
            print('Você veste a pele e ela adere à sua roupa magicamente, como uma armadura, e sua defesa aumenta!\n')
            jogador['defesa'] += 1
            print(f'Sua defesa atual: {jogador["defesa"]}\n')
        elif pele == '2':
            flag = True
            print('Uma pele como essa só iria atrapalhar, melhor deixar onde está.\n')
        if flag == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')

    bt.enter()
    print('Aparentemente a grade é a única saída, porém está trancada. Lembrando da porta que apareceu sozinha na sala anterior, \nvocê decide explorar as paredes em busca de algo semelhante.\n '
          'Ao encostar na parede da direita, subtamente ela desaparece por completo. Antes que ela volte, você entra no espaço \nescuro atrás dela. Um barulho indica que a parede voltou ao seu lugar.\n '
          'No segundo seguinte, uma série de tochas se acende, iluminando um corredor que segue em frente por alguns passos antes \nde virar à direita.\n')
    bt.enter()
    print('As paredes do corredor estão repletas de pinturas e inscrições que não possuem nenhum significado para você. Distraído \ncom elas, não percebe que as paredes estão se fechando até estarem quase encostando em você. \n'
          'Vendo a velocidade com que elas se aproximam e a distância para sair do corredor, você percebe que não terá tempo de \ncorrer e precisará de um jeito de desarmar.\n')
    bt.enter()

    flag = False
    flag_armadilha = False
    n = 0 #Contador para que o jogador tenha apenas duas tentativas
    while flag == False or flag_armadilha == False: #Garante que o input se repita caso o jogador digite uma opção inválida e permite que o jogador tente mais uma vez
        print('\n\u001b[37;1mVocê tenta parar a armadilha usando força, inteligência ou sorte?\n (1) força\n (2) inteligência\n (3) sorte\n')
        armadilha = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{armadilha}\u001b[0m\n")

        if armadilha == '1': #Tenta desarmar usando força
            flag = True
            print('\nVocê apoia as costas e as mãos em uma parede e coloca os dois pés na outra. As paredes estão próximas o bastante para \nque seus joelhos se dobrem.\n'
                  'Você aplica toda sua força nas pernas, empurrando a parede.\n')
            #Teste de força. Se a força do jogador for maior que a da armadilha ele consegue parar as paredes.
            forca = teste_atributo(jogador['força'], 8, 9)
            if forca == True: #Passa no teste
                flag_armadilha = True
                print('Elas param de se aproximar e você intensifica a força. Um estalo se faz ouvir em todo o corredor e as paredes voltam \npara suas posições iniciais.\n')
                print('\nParabéns! Você conseguiu quebrar o sistema da armadilha e pode seguir seu caminho!\n')
            if forca == False: #Não passa no teste
                print('Por um instante, as paredes param de se aproximar, mas dura apenas alguns segundos antes de voltarem a se aproximar. \nVocê cai no chão e sente uma onda de dor subir por seu corpo.\n')
                jogador['hp'] -= 5
                bt.game_over(jogador)
        elif armadilha == '2': #Tenta desativar usando inteligência
            flag = True
            print('Você olha os itens que tem consigo e tenta elaborar um plano para desativar o sistema da armadilha.\n')
            #Teste de inteligência. Se passar, ele consegue desativar o sistema.
            inteligencia = teste_atributo(jogador['inteligência'], 8, 9)
            if inteligencia == True: #Passa no teste
                flag_armadilha = True
                print('Você observa atentamente as paredes e consegue ver através de um buraco na parede o mecanismo da armadilha. Pega então \numa pedra no chão e joga nesse buraco.\n '
                      'Escuta-se um barulho de algo quebrando e as paredes param de se aproximar.\n\nParabéns! Você conseguiu travar o sistema \nda armadilha!\n')
            if inteligencia == False: #Não passa no teste
                print('Você tenta parar as paredes prendendo sua arma em uma fresta entre a parede e o chão. Até funciona por um tempo e você \ncomeça a correr para sair do corredor,\n '
                      'mas então a arma se solta e acerta seu braço esquerdo. As paredes voltam a se fechar e agora você tem menos tempo para \nencontrar uma solução.\n')
                jogador['hp'] -= 5
                bt.game_over(jogador)
        elif armadilha == '3': #Tenta desarmar usando a sorte
            flag = True
            print('Você resolve confiar na sorte e tenta encontrar algo que pare a armadilha, aliás os moradores precisam passar de alguma \nforma.\n')
            #Teste de sorte. Se a sorte do jogador for maior que a da armadilha, ele encontra o botão para desligar o sistema.
            sorte = teste_atributo(jogador['sorte'], 8, 9)
            if sorte == True: #Passa no teste
                flag_armadilha = True
                print('Você analisa atentamente as paredes e encontra um pequeno botão vermelho. Ao pressioná-lo, escuta um click e as paredes \nparam de se aproximar.\n')
                print('\nParabéns! Você conseguiu desligar o sistema da armadilha e pode seguir seu caminho!\n')
            elif sorte == False: #Não passa no teste
                print('Você procura nas paredes atentamente e vê um botão verde. Pensando ser a solução, o aperta, contudo uma saraivada de \nespinhos sai da parede, um deles te acertando no ombro.\n')
        if flag_armadilha == False and flag == True: #Checa se o jogador conseguiu desativar a armadilha
            print('As paredes continuam se fechando ao seu redor.\n')
            bt.enter()
            n += 1
            if n == 2:
                print('Seu tempo acabou. As paredes se fecham sobre você, colocando um fim a sua jornada.\n')
                jogador['hp'] = 0
                bt.game_over(jogador)

        if flag == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')

    bt.enter()
    print('O corredor faz mais uma curva à esquerda antes de outra porta aparecer.\n')
    bt.enter()
    sala_atual = 4 #Manda o jogador para a sala 4
    return sala_atual

def salao_final(jogador):
    print('Após subir toda a escada, você chega em um grande salão no alto da torre. O cajado está lá, em cima de uma mesa ao \nlado da porta e você corre pegá-lo. Nesse momento você entende o que o guardião disse sobre o encanto dele.\n '
          'Subtamente, seus ferimentos se curam e você se sente mais forte do que em qualquer outro momento da vida.\n')
    bt.enter()
    #Recupera toda a vida do jogador e aumenta todos os atributos em um ponto
    jogador['hp'] = 120
    jogador['defesa'] += 1
    jogador['força'] += 1
    jogador['destreza'] += 1
    jogador['inteligência'] += 1
    jogador['sorte'] += 1
    jogador['carisma'] += 1
    print(f'Seus atributos:\n defesa = {jogador.get("defesa")}\n força = {jogador.get("força")}\n destreza = {jogador.get("destreza")}\n inteligência = {jogador.get("inteligência")}\n sorte = {jogador.get("sorte")}\n carisma = {jogador.get("carisma")}')
    bt.enter()
    print('Você então olha para o ambiente. O primeiro cômodo que não parecia totalmente abandonado. Além da pequena mesa, há um \nlongo sofá branco e vazio de frente para a sacada aberta, de onde se tem uma bela vista da noite na fronteira entre os \nreinos.\n '
          'Tapeçarias representando a criação do artefato e diferentes batalhas cobrem as paredes. Um belo lustre de cristal no \nalto do teto ilumina o ambiente.\n')
    bt.enter()
    print('Quando você se prepara para voltar, uma risada faz você olhar para o sofá. Um homem se levanta e te olha. Surpreso, você\npercebe ser o guardião que derrotou ateriormente. Ele sorri antes de começar a falar, sua voz grave ecoando no ambiente.\n')
    bt.enter()
    print('- Você não pode ter achado que seria tão fácil. Eu observei sua jornada, jovem guerreiro. Apesar de ter matado meus \ncriados, meu animal de estimação e minha marionete, se mostrou merecedor de encontrar esse local e a relíquia.\n '
          'Mas isso não é o bastante. Eu não posso deixá-lo sair daqui com isso, sem mais nem menos.\n')
    bt.enter()
    #Dicionário do Guardião real
    Guardiao_real = {"nome": "Guardião real", 'hp': 100, 'defesa': 6, 'força': 5}
    bt.batalha(Guardiao_real, jogador, True)
    bt.enter()
    print('Após finalmente derrotá-lo, você tem a certeza que o artefato realmente te deixa mais forte. Você poderia ser o mais \nforte de todos os reinos com ele. \n'
          'Voltar a ser um homem livre, obter todas as recompensas do rei deve ser bom, mas será que vale a pena? As opções passam \npor sua mente e você precisa decidir logo.\n')
    bt.enter()
    flag = False
    while flag == False: #Garante que o input se repita caso o jogador digite uma opção inválida
        print('\u001b[37;1mVocê irá devolver o artefato ou fugir com ele?\n (1) Entregar\n (2) Fugir\n')
        final = input('>>>')
        bt.delete_last_lines(1)
        print(f">>>{final}\u001b[0m\n")

        if final == '1': #Final 1 - o jogador devolve o artefato para o rei
            flag = True
            print('Você tinha uma vida antes de ser preso e gostaria muito de recuperá-la. Sem perder tempo, você sai da casa, percebendo \nque agora todas as portas estão abertas.\n '
                  'Agora que conhece o caminho, não tem problemas para voltar para o castelo. O mesmo soldado que te guiou para fora te \nespera nos portões. Você é guiado até a presença do rei de Mitra.\n '
                  'Você recebe a liberdade e uma grande recompensa em ouro e terras. Quando a guerra finalmente estoura, seu reino possui \nvantagem por conta do artefato e vence a guerra.\n')
        elif final == '2': #Final 2 - o jogador foge com o artefato
            flag = True
            print('Sua vida anterior não era assim tão boa e nada que o rei possa oferecer é tão bom quanto à grande quantidade de poder \nque o cajado lhe fornece. Além de tudo, não importa o resultado da guerra se você já estiver longe. \n'
                  'Com o artefato em mãos, você segue para outro reino para se aprofundar no estudo da magia de artefatos. Em menos de um ano, se\ntorna um poderoso e temido mago e ninguém ousa te desafiar ou entrar em seu caminho.\n')
        if flag == False: #Checa se o jogador digitou um comando inválido
            print('\nComando não reconhecido, tente novamente.\n')


def final(jogador):
    '''
    Define os acontecimentos e sua ordem dentro da mansão
    Entrada: dicionário com os atributos do jogador e string com o local que ele foi
    '''
    print('Depois de seguir alguns metros na estrada, a noite cai e você decide que é melhor esperar o sol voltar. Você sai e \nencontra uma pedra grande o bastante para que você possa deitar atrás dela e não ser visto da estrada. \n'
          'Ao acordar, sente suas energias renovadas e feridas curadas.\n')
    jogador['hp'] = 120
    print(f'Seu hp: {jogador["hp"]}')
    bt.enter()
    print('Volta então retorna para a estrada e continua o caminho até finalmente avistar seu destino.\n')
    print('Uma casa comum, de pedra cinza, sem muitos detalhes a vista. O que chama a atenção, porém, é uma grande torre do lado \ndireito, sem portas ou janelas.\n '
          'A porta preta da frente não é exatamente convidativa, mas mesmo assim você adentra o local.\n')
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
    bt.enter()
    print('Você terminou o jogo!\n\n\u001b[37;1mDeseja jogar outra vez:\n (1) sim\n (2) não\n')
    jogar_nov = input('>>>')
    bt.delete_last_lines(1)
    print(f">>>{jogar_nov}\u001b[0m\n")

    if jogar_nov == '1':
        bt.restart_program()
    elif jogar_nov == '2':
        sys.exit()
