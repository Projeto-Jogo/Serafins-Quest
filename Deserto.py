# MÓDULO "DESERTO"

import Batalha as bt  # Importa o módulo "Batalha"


def dunas(jogador, objetos_coletados, hp, arma):
    
    # Função utilizada para a trajetória do jogador nas dunas do deserto
    
    a = b = c = d = e = f = 0  # Variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    pedra = 0 # Variável utilizada para saber se o jogador coletou uma pedra nas dunas
    pocao = 0 # Variável utilizada para saber se o jogador coletou uma poção nas dunas
    objetos_coletados_nas_dunas = []
    
    print('\nVocê se encontra nas dunas do deserto, que parecem não ter fim. O vento é forte, fazendo com que elas se movimentem. Não há nada ao seu redor além de areia, e você não sabe para onde ir...')
    bt.enter()
    
    print('\n Você vê algo na areia, a poucos metros...')
    bt.enter()
    if "pedra" in objetos_coletados and "poção" in objetos_coletados:  # Se o jogador já coletou a pedra e a poção, aparece um aviso de que não há mais objetos para coletar no local
        return (f'\nVocê ja coletou os objetos que necessitava aqui!')
    elif "pedra" in objetos_coletados and "poção" not in objetos_coletados:  # Se o jogador já coletou a pedra mas não a poção, ele encontra a poção
        while a < 1:
            escolha_1 = input('\nChegando mais perto, você vê que é uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>')  # O jogador escolhe se quer coletar a poção ou não
            if escolha_1 == "1":
                a += 1
                bt.delete_last_lines(1) # Chamada da função "delete_last_lines(n)" do módulo "Batalha"
                objetos_coletados.append("poção") # Se ele escolhe coletar a poção, esta é adicionada à sua lista geral de objetos coletados
                objetos_coletados_nas_dunas.append("poção") # A poção também é adicionada à lista específica de objetos coletados nas dunas
                while b < 1: # O jogador escolhe se quer beber a poção ou não
                    escolha_2 = input('\n Beber poção? 1 - Sim / 2 - Não  >>>') # O jogador escolhe se quer beber a poção ou não
                    if escolha_2 == "1": 
                        b += 1
                        bt.delete_last_lines(1)
                        hp -= 10  # Se o jogador beber a poção, perde 10 HPs
                        if hp <= 0: # Se após perder 10 HPs seu número de HPs for igual ou menor que zero, ele perde o jogo
                            bt.game_over(jogador) # Chamada da função "game_over()" do módulo "Batalha"
                        return (f'\nAh, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {hp}')
                    elif escolha_2 == "2": # 
                        b += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                        return(f'\nVocê não coletou novos itens!')
                    else:
                        print('\nEscolha uma opção válida!') 
            elif escolha_1 == "2":
                a += 1
                print("OK!")
                return (f'\nVocê não coletou nenhum novo item!')
            else:
                print('\nComando não conhecido, tente novamente.')
    elif "poção" in objetos_coletados and "pedra" not in objetos_coletados:
        while c < 1:
            c += 1
            print('\n Você vê algo na areia, a poucos metros...')
            bt.enter()
            escolha = input('\nChegando mais perto, você vê que é uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>')
            if escolha == "1":
                c += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("pedra")
                objetos_coletados_nas_dunas.append("pedra")
                print("\n Pedra coletada!")
                return (f'\nSeu novo item é pedra!')
            elif escolha == "2":
                c += 1
                print("OK!")
                bt.delete_last_lines(1)
                return (f'\nVocê não coletou nenhum novo item!')
            else:
                print('\nComando não conhecido, tente novamente.')
    else:
        while d < 1:
            print('\n Você vê algo na areia, a poucos metros...')
            bt.enter()
            escolha = input('\nChegando masi perto, vê que é uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>')
            if escolha == "1":
                pocao = 1
                d += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("poção")
                objetos_coletados_nas_dunas.append("poção")
                while e < 1:
                    escolha_2 = input('\nBeber poção? 1 - Sim / 2 - Não  >>>')
                    if escolha_2 == "1":
                        e += 1
                        bt.delete_last_lines(1)
                        hp -= 10
                        print(f'\nAh, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {hp}')
                    elif escolha_2 == "2":
                        e += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                        print('\nPoção coletada!')
                    else:
                        print('\nEscolha uma opção válida!')
            elif escolha == "2":
                d += 1
                print("OK!")
            else:
                print('\nComando não conhecido, tente novamente.')
        print("ADICIONAR DESCRIÇÃO DE UM CAMINHO")
        bt.enter()
        while f < 1:
            escolha = input('\nCaminhando mais um pouco, você encontra uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>')
            if escolha == "1":
                pedra = 1
                f += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("pedra")
                objetos_coletados_nas_dunas.append("pedra")
                print('\nPedra coletada!')
            elif escolha == "2":
                f += 1
                print('OK!')
            else:
                print('\nEscolha uma opção válida!')
                
        if pocao == 1 and pedra == 1:
            return (f'\nSeus novos itens são {objetos_coletados_nas_dunas[0]} e {objetos_coletados_nas_dunas[1]}!')
        elif pocao == 1 and pedra == 0:
            return(f'\nSeu novo item é {objetos_coletados_nas_dunas[0]}')
        elif pocao == 0 and pedra == 1:
            return(f'\nSeu novo item é {objetos_coletados_nas_dunas[0]}')
        else:
            return(f'\nVocê não coletou nenhum novo item!')

def topo_da_montanha(objetos_coletados):
    
    # Funçao utilizada para a trajetória do jogador no topo de uma montanha no deserto
    
    a = 0 # Variável utilizada para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida

    print('\nVocê se encontra no topo da montanha. O vento é mais ainda mais forte e, pela altura, você tem uma visão ampla de grande parte do deserto...')
        
    if "flor" in objetos_coletados:
        return (f'\nVocê ja coletou o objeto que necessitava aqui!')
    else:
        while a < 1:
            print('\nVocê vê uma flor do deserto a poucos metros e caminha até ela...')
            bt.enter()
            escolha = input('\nDeseja coletá-la? 1 - Sim / 2 - Não  >>>')
            if escolha == "1":
                objetos_coletados.append("flor")
                a += 1
                bt.delete_last_lines(1)
                return (f'\nA flor do deserto foi adicionada aos seus itens!')
            elif escolha == "2":
                a += 1
                print("OK!")
                return (f'\nVocê não coletou novos itens!')
            else:
                print('\nComando não conhecido, tente novamente.')

def oasis(jogador, objetos_coletados, atributos, hp, arma):

# Função utilizada para a trajetória do jogador em um oasis no deserto

    a = b = c = d = e = f = 0 # Variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    Serpente = {"nome": "Serpente", 'hp': 30,  'defesa': 2, 'força': 2}
    desbloqueio = False
    missao_cumprida = False
    combinacao_correta = ["poção", "flor", "runa", "pedra"]
    pocoes = []
    
    print('\nVocê se encontra próximo ao oásis, que se destaca muito em meio àquela paisagem remota... é quase surreal ver um imenso lago, a vegetação e alguns coqueiros em meio ao deserto.')
    bt.enter()
    print('\nPorém, você não pode ir até ele, pois há um bloqueio na passagem...')
    print('\nPara desbloquear o caminho você deve apresentar 4 objetos dos quais você coletou, em uma determinada sequência...')
    objeto_1 = input('\nQual é o primeiro objeto da sequência?  >>>')
    if objeto_1 not in combinacao_correta:
        print('\nObjeto não identificado, tente novamente.')
        return oasis(jogador, objetos_coletados, atributos, hp, arma)
    elif objeto_1 in combinacao_correta and objeto_1 not in objetos_coletados:
        return(f'\nVocê não possui o objeto {objeto_1}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente desbloquear a passagem ao oasis novamente!')
    else:
        objeto_2 = input('\nQual é o segundo objeto da sequência?  >>>')
        if objeto_2 not in combinacao_correta:
            print("\nObjeto não identificado, tente novamente.")
            return oasis(jogador, objetos_coletados, atributos, hp, arma)
        elif objeto_2 in combinacao_correta and objeto_2 not in objetos_coletados:
            return(f'\nVocê não possui o objeto {objeto_2}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')    
        else:
            objeto_3 = input("\nQual é o terceiro objeto da sequência?  >>>")
            if objeto_3 not in combinacao_correta:
                print('\nObjeto não identificado, tente novamente.')
                return oasis(jogador, objetos_coletados, atributos, hp, arma)         
            elif objeto_3 in combinacao_correta and objeto_3 not in objetos_coletados:
                return(f'\nVocê não possui o objeto {objeto_3}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')
            else:
                objeto_4 = input('\nQual é o quarto objeto da sequência?  >>>')
                if objeto_4 not in combinacao_correta:
                    print('\nObjeto não identificado, tente novamente.')
                    return oasis(jogador, objetos_coletados, atributos, hp, arma)
                elif objeto_4 in combinacao_correta and objeto_4 not in objetos_coletados:
                    return(f'\nVocê não possui o objeto {objeto_4}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')
                else:
                    if(objeto_1 == combinacao_correta[0] and objeto_2 == combinacao_correta[1] and objeto_3 == combinacao_correta[2] and objeto_4 == combinacao_correta[3]):
                        desbloqueio = True
                        bt.delete_last_lines(5)
                        print(f'\nMuito bem! Você conseguiu entrar no ao oasis!')
                        bt.enter()
                        bt.passar_nivel(jogador)
                        print("ADICIONAR DESCRIÇÃO DO OASIS")
                        bt.enter()
                        print("\nVocê encontrou uma serpente no caminho!")
                        print(bt.batalha(Serpente, jogador))
                        print("\nVocê segue para o lago agora...")
                        bt.enter()
                        bt.delete_last_lines(1)
                        print("\nVocê mergulhou no lago!")
                        bt.delete_last_lines(1)
                        print("O lago é profundo e sua água é turva. Você não consegue enxergar muito bem, mas vê algo ao fundo...")
                        bt.enter()
                        bt.delete_last_lines(1)
                        print("\nNadando e chegando mais perto, você percebe que é um báu!")
                        while c < 1:
                            escolha_1 = input("\n O que deseja fazer? 1 - Coletar o baú / 2 - Sair do lago  >>>")
                            if escolha_1 == "1":
                                c += 1
                                bt.delete_last_lines(1)
                                print("\nVocê pegou o baú!")
                                print("\nSaia do lago agora e veja o que há dentro dele...")
                                bt.enter()
                                print("Você sai do lago, sentando-se à sua beira...")
                                bt.delete_last_lines(1)
                                abertura_do_bau = input("Digite 1 para abrir o baú!  >>>")
                                if abertura_do_bau == "1":
                                    d += 1
                                    if "chave" in objetos_coletados:
                                        print("\nVocê conseguiu!")
                                        bt.passar_nivel(jogador)
                                        while e < 1:
                                            beber_pocao_brilhante = input("\nHá uma poção brilhante lá dentro! Digite 1 para bebê-la...  >>>")
                                            if beber_pocao_brilhante == "1":
                                                e += 1
                                                hp += 20
                                                objetos_coletados.append("poção brilhante")
                                                print(f'\nVocê ganhou 20 HPs após beber a poção! Seus HPs: {hp}')

                                        print("\nTambém há uma nota dentro do baú... leia!")
                                        bt.enter()
                                        bt.delete_last_lines(1)
                                        print("\nNa nota está escrito 'URSO'..")
                                        print("\nHmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
                                        bt.enter()
                                        while f < 1:
                                            nova_arma = input("\nVocê encontrou um chicote no caminho! Digite 1 para obtê-lo como arma!  >>>")
                                            if nova_arma == "1":
                                                f += 1
                                                arma = "chicote"
                                                print(f'\nSua nova arma: {arma}')
                                            else:
                                                print("\nComando não conhecido, tente novamente.")
                                        missao_cumprida = True
                                    else:
                                        d += 1
                                        print("\nOops! Você ainda não tem a chave para abrir o baú! Continue sua exploração pelo deserto e colete-a!")
                                else:
                                    print("\nAbra o baú!")
                            elif escolha_1 == "2":
                                c += 1
                                print('\nVocê sai do lago, sentando-se à sua beira...')
                                bt.enter()
                                print("\nParece que não há mais nada para fazer aqui...")
                            else:
                                print("\nComando não conhecido, tente novamente.")
    if desbloqueio == False:
        return(f'\nCombinação incorreta! Você não conseguiu advinhar a sequência e obter acesso ao oasis! Tente novamente!')
    if missao_cumprida == False:
        return(f'\nVocê não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...')
    elif missao_cumprida == True:
        return(f'\nParabéns! Você cumpriu esta etapa, obtendo uma dica para seguir em sua jornada!')

def retornar(local, jogador, objetos_coletados, atributos, hp, arma):
    
    # Função utilizada para que o jogador possa retornar a locais que ele já explorou anteriormente
    i = 0
    j = 0
    
    if local == "Topo da montanha":
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ O TOPO DA MONTANHA")
        print("\nVocê voltou ao topo da montanha...")
        bt.delete_last_lines(1)
        print(topo_da_montanha(objetos_coletados))
        if "chave" not in objetos_coletados:
                while i < 1:
                    coleta_de_objetos = input("\nVocê encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    if coleta_de_objetos == "1":
                        i += 1
                        objetos_coletados.append("chave")
                        print("\nChave coletada!")
                        print("\nSeu novo item é chave!")
                    elif coleta_de_objetos == "2":
                        i += 1
                        print("OK!")
        print("\nSiga às dunas agora...")
        bt.enter()
        bt.delete_last_lines(1)
        print(dunas(jogador, objetos_coletados, hp, arma ))
        print("\nAgora só resta explorar o oasis novamente...")
        print(oasis(jogador, objetos_coletados, atributos, hp, arma))
        if "poção brilhante" not in objetos_coletados:
            return (f'\nVocê não conseguiu cumprir a missão...')
        else:
            return (f'\nDessa vez você conseguiu!')

    elif local == "Dunas":
        print("\nVocê voltou às dunas...")
        bt.delete_last_lines(1)
        print(dunas(jogador, objetos_coletados, hp, arma))
        print("\nSiga ao topo da montanha agora...")
        bt.enter()
        bt.delete_last_lines(1)
        print(topo_da_montanha(objetos_coletados))
        print("\nAgora só resta explorar o oasis novamente...")
        if "runa" not in objetos_coletados:
                while j < 1:
                    coleta_de_objetos = input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    if coleta_de_objetos == "1":
                        j += 1
                        objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nSeu novo item é runa!")
                    elif coleta_de_objetos == "2":
                        j += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                    else:
                        print("\nComando não conhecido, tente novamente.")
        print(oasis(jogador, objetos_coletados, atributos, hp, arma))
        if "poção_brilhante" not in objetos_coletados:
            return (f'\nVocê não conseguiu cumprir a missão...')
        else:
            return (f'\nDessa vez você conseguiu!')

def Deserto(jogador):
    
# Função principal que chama as demais funções (dunas(), topo_da_montanha() e oasis()), descrevendo toda a trajetória do jogador pela etapa do deserto.

    r = s = t = u = v = w = x = y = z = 0  # Variáveis de controle para o mecanismo de repetição (caso o jogador tenha digitado um comando inválido)
    Serpente = {"nome": "Serpente", 'hp': 30,  'defesa': 2, 'força': 2}
    meus_objetos_coletados = []
    forca = jogador["força"]
    destreza = jogador["destreza"]
    inteligencia = jogador["inteligência"]
    sorte = jogador["sorte"]
    carisma = jogador["carisma"]
    hp = jogador["hp"]
    arma = jogador["arma"]
    meus_atributos = [forca, destreza, inteligencia, sorte, carisma]
    
    print("\nVOCÊ CHEGOU AO DESERTO!")
    bt.enter()
    print("\nSua primeira visão é de uma planície interminável e você se sente perdido(a)...")
    bt.enter()
    bt.delete_last_lines(1)

    while r < 1:
        escolha_1 = input("\nInicialmente, você tem três opções de caminhos para seguir. Escolha um deles: 1 - Caminho 1 / 2 - Caminho 2 / 3 - Caminho 3  >>>")
        if escolha_1 == "1":
            # CAMINHO 1: TOPO DA MONTANHA - OASIS - DUNAS
            r += 1
            print("\nVocê escolheu o caminho 1. Você segue para o leste, a caminho de uma grande montanha...")
            bt.enter()
            print("\nO caminho é relativamente longo, mas você caminha rapidamente e não demora muito a encontrar a montanha.")
            print("\nSeu destino é o topo da montanha. Ao chegar até ela, você encontra uma subida bastante íngreme.")
            bt.enter()      
            print("\nApós uma longa caminhada, você finalmente chega ao topo da montanha...")
            bt.enter()
            bt.delete_last_lines(1)
            print(topo_da_montanha(meus_objetos_coletados))
            print("\nVocê está descendo a montanha agora...")
            bt.delete_last_lines(1)
            bt.enter()
            bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados:
                while s < 1:
                    coleta_de_objetos = input("\nVocê encontrou uma runa no caminho! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    if coleta_de_objetos == "1":
                        s += 1
                        meus_objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nA runa foi adicionada ao seus itens!")
                    elif coleta_de_objetos == "2":
                        s += 1
                        print("OK!")
                        # bt.delete_last_lines(1)
                    else:
                        print("\nComando não conhecido, tente novamente.")

            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê continua seu caminho por uma longa estrada de areia, onde não vê nada além de alguns cactos ao redor.")
            
            print("\nApós aproximadamente 1 hora de caminhada, você está quase chegando ao seu próximo destino...")
            print("\nHá um oasis está a alguns metros de distância e você deve seguir até lá!")
            bt.enter()
            print("\nVocê chegou ao oásis...")
            bt.delete_last_lines(1)
            print(oasis(jogador, meus_objetos_coletados, meus_atributos, hp, arma))
            print("\nSó resta um local para explorar agora...")
            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê segue em direção ao seu destino final no deserto...")
            print("\nVocê continua caminhando pela mesma estrada...")
            bt.enter()
            print("\nVocê entra em um estreito caminho, partindo da estrada, e segue para leste...")

            print("\nVocê encontrou uma serpente no caminho!")
            bt.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê então segue em sua caminhada...")
            bt.enter()
            print("\nVocê vê algo na areia, a poucos metros...")
            if "poção" not in meus_objetos_coletados:
                while t < 1:
                    coleta_de_objetos = input("\n Chegando mais perto, você vê que é uma poção! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    print("\nVocê pode guardar esta poção, mas não bebê-la!")
                    if coleta_de_objetos == "1":
                        t += 1
                        meus_objetos_coletados.append("poção")
                        print("\nPoção coletada!")
                        print("\nSeu novo item é poção!")
                    elif coleta_de_objetos == "2":
                        t += 1
                        print("\nOK!")
                    else:
                        print("\nComando não conhecido, tente novamente.")

            print("\nFinalmente, após alguns minutos de caminhada, você chega ao destino.")
            print(dunas(jogador, meus_objetos_coletados, hp, arma))
            
            if "poção brilhante" not in meus_objetos_coletados:
                print("\nParece que o caminho que você escolheu não era o correto.")
                print("\nPor isso, você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nVocê pode começar explorando as dunas novamente...")
                bt.enter()
                print(retornar("Dunas", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                
                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance agora!")
                    bt.enter()
                    print("Você tem uma chance de explorar o topo da montanha novamente... você segue até lá.")
                    bt.enter()
                    print("O caminho da subida é cansativo, mas você finalmente chega ao destino...")
                    print(retornar("Topo da montanha", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram... você não pode mais explorar nenhum local no deserto.")
                        return(f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')

        elif escolha_1 == "2":
            # CAMINHO 2: DUNAS - TOPO DA MONTANHA - OASIS
            r += 1
            print("\nVocê escolheu o caminho 2. Você segue por um caminho estreito..")
            bt.enter()
            print("\nApós uma curta caminhada, você chega às dunas do deserto...")
            bt.enter()
            bt.delete_last_lines(1)
            print(dunas(jogador, meus_objetos_coletados, hp, arma))
            print("\nVocê continua seu caminho...")
            bt.enter()
            print("\Você segue por uma longa estrada. A temperatura está bastante elevada, fazendo com que o caminho pareça ainda mais longo.")

            if "chave" not in meus_objetos_coletados:
                while u < 1:
                    coleta_de_objetos = input("\nVocê encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    if coleta_de_objetos == "1":
                        u += 1
                        meus_objetos_coletados.append("chave")
                        print("\nChave coletada!")
                        print("\nSeu novo item é chave!")
                    elif coleta_de_objetos == "2":
                        u += 1
                        print("\nOK!")

            bt.enter()
            bt.delete_last_lines(1)
            print("\nApós aproximadamente 1 hora, você avista a montanha ao longe...")
            bt.enter()
            print("\nQuando você finalmente chega à montanha, percebe que o caminho para subi-la será longo e sinuoso...")
            print("\nMesmo assim, você não pode desistir. Você começa a subir a montanha, percebendo um caminho muito íngreme.")
            bt.enter()
            print("\nApós a difícil caminhada, você finalmente chega ao topo da montanha...")
            print(topo_da_montanha(meus_objetos_coletados))
            print("\nVocê está descendo a montanha agora...")
            print("\nSó resta um local para explorar agora...")
            bt.enter()
            print("Um oasis está há alguns metros... siga até lá!")
            bt.enter()
            bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados:
                while v < 1:
                    coleta_de_objetos = input("\nVocê encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    if coleta_de_objetos == "1":
                        v += 1
                        meus_objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nSeu novo item é runa!")
                    elif coleta_de_objetos == "2":
                        v += 1
                        print("OK!")

            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê chegou ao oásis...")
            print(oasis(jogador, meus_objetos_coletados, meus_atributos, hp, arma))
            
            if "poção brilhante" not in meus_objetos_coletados:
                print("\nParece que o caminho que você escolheu não era o correto.")
                print("\nPor isso, você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nVocê pode começar explorando o topo da montanha novamente...")
                bt.enter()
                print(retornar("Topo da montanha", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance agora!")
                    bt.enter()
                    print("Você tem uma chance para explorar as dunas do deserto novamente ... você segue até lá.")
                    bt.enter()
                    print(retornar("Dunas", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram... você não pode mais explorar nenhum local no deserto.")
                        return(f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
 
        elif escolha_1 == "3":
             # CAMINHO 3: OASIS - DUNAS - TOPO DA MONTANHA
            r += 1
            print("\nVocê segue por um estreito caminho. Não há praticamente nada ao seu redor além de alguns cactos ao redor.")
            bt.enter()
            print("\nVocê também avista um lagarto do deserto em certo ponto da caminhada...")
            bt.enter()
            print("\n1 hora depois, você finalmente tem uma bonita vista à sua frente: há um oasis a alguns metros!")
            print(oasis(jogador, meus_objetos_coletados, meus_atributos, hp, arma))
            print("\nVocê está prosseguindo sua caminhada...")
            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê segue em direção ao seu próximo destino...")
            print("\nVocê caminha por uma longa estrada...")
            bt.enter()
            print("\nVocê entra em um outra estreito caminho, partindo da estrada, e segue para leste...")
 
            print("\nVocê encontrou uma serpente!")
            bt.batalha(Serpente, jogador)  # Chamada da função "batalha" do módulo "Batalha"
            print("\nADICIONAR MAIS DESCRIÇÃO DE CAMINHO")
 
            if "runa" not in meus_objetos_coletados:
                while w < 1:
                    coleta_de_objetos = input("\nVocê encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    if coleta_de_objetos == "1":
                        w += 1
                        meus_objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nSeu novo item é runa!")
                    elif coleta_de_objetos == "2":
                        w += 1
                        print("OK!")
                    else:
                        print("\nComando não conhecido, tente novamente.")
       
            print("\nFinalmente você vê às dunas do deserto, não muito distantes...")
            print("\nVocê segue até lá...")
            bt.enter()
            bt.delete_last_lines(1)
            print(dunas(jogador, meus_objetos_coletados, hp, arma))
            print("\nVocê está prosseguindo sua caminhada...")
            bt.delete_last_lines(1)
            print("\nSó resta um local para explorar agora...")
            print("\nVocê segue por uma longa estrada. A temperatura está bastante elevada, fazendo com que o caminho pareça ainda mais longo.")
 
            if "chave" not in meus_objetos_coletados:
                while x < 1:
                    coleta_de_objetos = input("\nVocê encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não  >>>")
                    if coleta_de_objetos == "1":
                        x += 1
                        meus_objetos_coletados.append("chave")
                        print("\nChave coletada!")
                        print("\nSeu novo item é chave!")
                    elif coleta_de_objetos == "2":
                        x += 1
                        print("OK!")
                    else:
                        print("\nComando não conhecido, tente novamente.")
 
            print("\nApós aproximadamente 1 hora, você avista a montanha ao longe...")
            bt.enter()
            print("\nQuando você finalmente chega à montanha, percebe que o caminho para subi-la será longo e sinuoso...")
            print("\nMesmo assim, você não pode desistir. Você começa a subir a montanha, percebendo um caminho muito íngreme.")
            bt.enter()
            print("\nApós a difícil caminhada, você finalmente chega ao topo da montanha...")
            bt.enter()
            bt.delete_last_lines(1)
            print(topo_da_montanha(meus_objetos_coletados))
 
            if "poção brilhante" not in meus_objetos_coletados:
                print("\nVocê não conseguiu acesso ao oasis para cumprir sua missão nesta etapa...")
                print("\nVocê tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nPrimeiramente siga às dunas...")
                print("\nADICIONAR DESCRIÇÃO DO CAMINHO ÀS DUNAS")
                bt.enter()
                print(retornar("Dunas", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                 
                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance agora!")
                    bt.enter()
                    print("Você tem uma chance de explorar o topo da montanha novamente... você segue até lá.")
                    bt.enter()
                    print("O caminho da subida é cansativo, mas você finalmente chega ao destino...")
                    print(retornar("Topo da montanha", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram... você não pode mais explorar nenhum local no deserto.")
                        return(f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
