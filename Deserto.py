# MÓDULO "DESERTO"

import Batalha as bt  # Importa o módulo "Batalha"


def dunas(jogador, objetos_coletados, hp, arma):
    
    # Função utilizada para a trajetória do jogador nas dunas do deserto
    
    a = b = c = d = e = f = 0  # Variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    pedra = 0 # Variável utilizada para saber se o jogador coletou uma pedra nas dunas
    pocao = 0 # Variável utilizada para saber se o jogador coletou uma poção nas dunas
    objetos_coletados_nas_dunas = []
    
    print('\nADICIONAR DESCRIÇÃO DAS DUNAS DO DESERTO')

    if "pedra" in objetos_coletados and "poção" in objetos_coletados:  # Se o jogador já coletou a pedra e a poção, aparece um aviso de que não há mais objetos para coletar no local
        return (f'\nVocê ja coletou os objetos que necessitava aqui!')
    elif "pedra" in objetos_coletados and "poção" not in objetos_coletados:  # Se o jogador já coletou a pedra mas não a poção, ele encontra a poção
        while a < 1:
            escolha_1 = int(input('\nVocê encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>'))  # O jogador escolhe se quer coletar a poção ou não
            if escolha_1 == 1:
                a += 1
                bt.delete_last_lines(1) # Chamada da função "delete_last_lines(n)" do módulo "Batalha"
                objetos_coletados.append("poção") # Se ele escolhe coletar a poção, esta é adicionada à sua lista geral de objetos coletados
                objetos_coletados_nas_dunas.append("poção") # A poção também é adicionada à lista específica de objetos coletados nas dunas
                while b < 1: # O jogador escolhe se quer beber a poção ou não
                    escolha_2 = int(input('\n Beber poção? 1 - Sim / 2 - Não  >>>')) # O jogador escolhe se quer beber a poção ou não
                    if escolha_2 == 1: 
                        b += 1
                        bt.delete_last_lines(1)
                        hp -= 10  # Se o jogador beber a poção, perde 10 HPs
                        return (f'\nAh, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {hp}')
                        if hp <= 0: # Se após perder 10 HPs seu número de HPs for igual ou menor que zero, ele perde o jogo
                            bt.game_over(jogador) # Chamada da função "game_over()" do módulo "Batalha"
                    elif escolha_2 == 2: # 
                        b += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                        return(f'\Você não coletou novos itens!')
                    else:
                        print('\nEscolha uma opção válida!') 
            elif escolha_1 == 2:
                a += 1
                print("OK!")
                return (f'\nVocê não coletou nenhum novo item!')
            else:
                print('\nComando não conhecido, tente novamente.')
    elif "poção" in objetos_coletados and "pedra" not in objetos_coletados:
        while c < 1:
            c += 1
            escolha = int(input('\nVocê encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>'))
            if escolha == 1:
                c += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("pedra")
                objetos_coletados_nas_dunas.append("pedra")
                print("\n Pedra coletada!")
                return (f'\nSeu novo item é pedra!')
            elif escolha == 2:
                c += 1
                print("OK!")
                bt.delete_last_lines(1)
                return (f'\nVocê não coletou nenhum novo item!')
            else:
                print('\nComando não conhecido, tente novamente.')
    else:
        while d < 1:
            escolha = int(input('\nVocê encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>'))
            if escolha == 1:
                pocao = 1
                d += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("poção")
                objetos_coletados_nas_dunas.append("poção")
                while e < 1:
                    escolha_2 = int(input('\nBeber poção? 1 - Sim / 2 - Não  >>>'))
                    if escolha_2 == 1:
                        e += 1
                        bt.delete_last_lines(1)
                        hp -= 10
                        print(f'\nAh, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {hp}')
                    elif escolha_2 == 2:
                        e += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                        print('\nPoção coletada!')
                    else:
                        print('\nEscolha uma opção válida!')
            elif escolha == 2:
                d += 1
                print("OK!")
            else:
                print('\nComando não conhecido, tente novamente.')
        print("ADICIONAR DESCRIÇÃO DE UM CAMINHO")
        bt.enter()
        while f < 1:
            escolha = int(input('\nVocê encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>'))
            if escolha == 1:
                pedra = 1
                f += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("pedra")
                objetos_coletados_nas_dunas.append("pedra")
                print('\nPedra coletada!')
            elif escolha == 2:
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
    
    a = 0
    if "flor" in objetos_coletados:
        return (f'\nVocê ja coletou o objeto que necessitava aqui!')
    else:
        while a < 1:
            escolha = int(input('\nVocê encontrou uma flor do deserto! Deseja coletá-la? 1 - Sim ou 2 - Não  >>>'))
            if escolha == 1:
                objetos_coletados.append("flor")
                a += 1
                bt.delete_last_lines(1)
                return (f'\nSeu novo item é uma flor do deserto!')
            elif escolha == 2:
                a += 1
                print("OK!")
                return (f'\nVocê não coletou novos itens!')
            else:
                print('\nComando não conhecido, tente novamente.')


def oasis(jogador, objetos_coletados, atributos, hp, arma):

# Função utilizada para a trajetória do jogador em um oasis no deserto

    a = b = c = d = e = f = 0 #
    Serpente = {"nome": "Serpente", 'hp': 30,  'defesa': 2, 'força': 2}
    desbloqueio = False
    missao_cumprida = False
    combinacao_correta = ["poção", "flor", "runa", "pedra"]
    pocoes = []
    
    print("Apresente uma sequência de 4 objetos como código para desbloquear a passagem ao oasis!")
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

                        print("\nSiga para o lago agora...")
                        bt.enter()
                        bt.delete_last_lines(1)
                        print("\nVocê mergulhou no lago!")
                        bt.enter()
                        bt.delete_last_lines(1)
                        print("ADICIONAR DESCRIÇÃO DO LAGO")
                        print("\n Parece que há algo lá no fundo, a alguns metros...")
                        bt.enter()
                        bt.delete_last_lines(1)
                        print("\nNadando e chegando mais perto, você vê que é um báu!")
                        while c < 1:
                            escolha_1 = int(input("\n O que deseja fazer? 1 - Coletar o baú / 2 - Sair do lago  >>>"))
                            if escolha_1 == 1:
                                c += 1
                                bt.delete_last_lines(1)
                                print("\nVocê pegou o baú!")
                                print("\nSaia do lago agora e veja o que há dentro dele...")
                                bt.enter()
                                print("ADICIONAR DESCRIÇÃO DO JOGADOR SAINDO DO LAGO")
                                bt.delete_last_lines(1)
                                abertura_do_bau = int(input("Digite 1 para abrir o baú!  >>>"))
                                if abertura_do_bau == 1:
                                    d += 1
                                    if "chave" in objetos_coletados:
                                        print("\nVocê conseguiu!")
                                        bt.passar_nivel(jogador)
                                        while e < 1:
                                            beber_pocao_brilhante = int(input("\nHá uma poção brilhante lá dentro! Digite 1 para bebê-la...  >>>"))
                                            if beber_pocao_brilhante == 1:
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
                                            nova_arma = int(input("\nVocê encontrou um chicote no caminho! Digite 1 para obtê-lo como arma!  >>>"))
                                            if nova_arma == 1:
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
                            elif escolha_1 == 2:
                                c += 1
                                print("\nVocê saiu do lago. Parece que não há mais nada para fazer aqui...")
                            else:
                                print("\nComando não conhecido, tente novamente.")
    if desbloqueio == False:
        return(f'\nCombinação incorreta! Você não conseguiu acesso ao oasis! Tente novamente!')
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
        print("\nVocê voltou ao topo da montanha!")
        bt.delete_last_lines(1)
        print(topo_da_montanha(objetos_coletados))
        if "chave" not in objetos_coletados:
                while i < 1:
                    coleta_de_objetos = int(input("\nVocê encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"  >>>))
                    if coleta_de_objetos == 1:
                        i += 1
                        objetos_coletados.append("chave")
                        print("\nChave coletada!")
                        print("\nSeu novo item é chave!")
                    elif coleta_de_objetos == 2:
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
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ AS DUNAS")
        print("\nVocê voltou às dunas")
        bt.delete_last_lines(1)
        print(dunas(jogador, objetos_coletados, hp, arma))
        print("\nSiga ao topo da montanha agora...")
        bt.enter()
        bt.delete_last_lines(1)
        print(topo_da_montanha(objetos_coletados))
        print("\nAgora só resta explorar o oasis novamente...")
        if "runa" not in objetos_coletados:
                while j < 1:
                    coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não  >>>"))
                    if coleta_de_objetos == 1:
                        j += 1
                        objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nSeu novo item é runa!")
                    elif coleta_de_objetos == 2:
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
    
    print("\nVocê está no deserto!")
    bt.enter()
    print("ADICIONAR DESCRIÇÃO INTRODUTÓRIA DO DESERTO")
    bt.enter()
    bt.delete_last_lines(1)

    while r < 1:
        escolha_1 = int(input("\nEscolha um dos caminhos para seguir: 1 - Caminho 1 / 2 - Caminho 2 / 3 - Caminho 3  >>>"))
        if escolha_1 == 1:
            # CAMINHO 1: TOPO DA MONTANHA - OASIS - DUNAS
            r += 1
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ O TOPO DA MONTANHA")
            print("\nVocê está no topo da montanha!")
            bt.enter()
            bt.delete_last_lines(1)
            print(topo_da_montanha(meus_objetos_coletados))
            print("\nVocê está prosseguindo sua caminhada...")
            bt.delete_last_lines(1)
            bt.enter()
            bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados:
                while s < 1:
                    coleta_de_objetos = int(input("\nVocê encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não  >>>"))
                    if coleta_de_objetos == 1:
                        s += 1
                        meus_objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nSeu novo item é runa!")
                    elif coleta_de_objetos == 2:
                        s += 1
                        print("OK!")
                        # bt.delete_last_lines(1)
                    else:
                        print("\nComando não conhecido, tente novamente.")

            bt.enter()
            bt.delete_last_lines(1)
            print("\nO oasis está a alguns metros... siga até lá!")
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E O OASIS")
            print("\nVocê chegou ao oásis...")
            bt.delete_last_lines(1)
            print(oasis(jogador, meus_objetos_coletados, meus_atributos, hp, arma))
            print("\nSó resta um local para explorar agora...")
            bt.enter()
            bt.delete_last_lines(1)
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS")

            print("\nVocê encontrou uma serpente no caminho!")
            bt.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
            bt.enter()
            bt.delete_last_lines(1)
            
            if "poção" not in meus_objetos_coletados:
                while t < 1:
                    coleta_de_objetos = int(input("\n Você encontrou uma poção! Deseja coletá-la? 1 - Sim / 2 - Não  >>>"))
                    print("\nVocê pode guardar esta poção mas não bebê-la!")
                    if coleta_de_objetos == 1:
                        t += 1
                        meus_objetos_coletados.append("poção")
                        print("\nPoção coletada!")
                        print("\nSeu novo item é poção!")
                    elif coleta_de_objetos == 2:
                        t += 1
                        print("\nOK!")
                    else:
                        print("\nComando não conhecido, tente novamente.")

            print("Você chegou às dunas do deserto...")
            print(dunas(jogador, meus_objetos_coletados, hp, arma))
            
            if "poção brilhante" not in meus_objetos_coletados:
                print("\nVocê tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nPrimeiramente siga às dunas...")
                print("\nADICIONAR DESCRIÇÃO DO CAMINHO ÀS DUNAS")
                bt.enter()
                print(retornar("Dunas", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance!")
                    bt.enter()
                    print("ADICIONAR DESCRIÇÃO DO CAMINHO AO TOPO DA MONTANHA")
                    print(retornar("Topo da montanha", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram!")
                        return(f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')

        elif escolha_1 == 2:
            # CAMINHO 2: DUNAS - TOPO DA MONTANHA - OASIS
            r += 1
            print("\nVocê está nas dunas do deserto...")
            print("\nADICIONAR DESCRIÇÃO DAS DUNAS")
            bt.enter()
            bt.delete_last_lines(1)
            print(dunas(jogador, meus_objetos_coletados, hp, arma))
            print("\nVocê está prosseguindo sua caminhada...")
            print("\nADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")

            if "chave" not in meus_objetos_coletados:
                while u < 1:
                    coleta_de_objetos = int(input("\nVocê encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não  >>>"))
                    if coleta_de_objetos == 1:
                        u += 1
                        meus_objetos_coletados.append("chave")
                        print("\nChave coletada!")
                        print("\nSeu novo item é chave!")
                    elif coleta_de_objetos == 2:
                        u += 1
                        print("\nOK!")

            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê chegou ao topo da montanha...")
            print(topo_da_montanha(meus_objetos_coletados))
            print("\nSó resta um local para explorar agora...")
            print("Um oasis está há alguns metros... siga até lá!")
            bt.enter()
            bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados:
                while v < 1:
                    coleta_de_objetos = int(input("\nVocê encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não  >>>"))
                    if coleta_de_objetos == 1:
                        v += 1
                        meus_objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nSeu novo item é runa!")
                    elif coleta_de_objetos == 2:
                        v += 1
                        print("OK!")

            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê chegou ao oásis...")
            print(oasis(jogador, meus_objetos_coletados, meus_atributos, hp, arma))
            
            if "poção brilhante" not in meus_objetos_coletados:
                print("\nVocê não conseguiu acesso ao oasis para cumprir sua missão nesta etapa...")
                print("\nVocê tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nPrimeiramente siga novamente ao topo da montanha...")
                print("\nADICIONAR DESCRIÇÃO DO CAMINHO AO TOPO DA MONTANHA")
                bt.enter()
                print(retornar("Topo da montanha", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance!")
                    bt.enter()
                    print("\nADICIONAR DESCRIÇÃO DO CAMINHO ÀS DUNAS")
                    print(retornar("Dunas", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram!")
                        return(f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')

        elif escolha_1 == 3:
            # CAMINHO 3: OASIS - DUNAS - TOPO DA MONTANHA
            r += 1
            print("\nVocê está no oásis!")
            print(oasis(jogador, meus_objetos_coletados, meus_atributos, hp, arma))
            print("\nVocê está prosseguindo sua caminhada...")
            bt.enter()
            bt.delete_last_lines(1)
            print("\nADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS")
            print("\nVocê encontrou uma serpente no caminho!")
            bt.batalha(Serpente, jogador)  # Chamada da função "batalha" do módulo "Batalha"
            print("\nADICIONAR MAIS DESCRIÇÃO DE CAMINHO")

            if "runa" not in meus_objetos_coletados:
                while w < 1:
                    coleta_de_objetos = int(input("\nVocê encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não  >>>"))
                    if coleta_de_objetos == 1:
                        w += 1
                        meus_objetos_coletados.append("runa")
                        print("\nRuna coletada!")
                        print("\nSeu novo item é runa!")
                    elif coleta_de_objetos == 2:
                        w += 1
                        print("OK!")
                    else:
                        print("\nComando não conhecido, tente novamente.")

            print("\nVocê chegou às dunas do deserto...")
            bt.enter()
            bt.delete_last_lines(1)
            print(dunas(jogador, meus_objetos_coletados, hp, arma))
            print("\nVocê está prosseguindo sua caminhada...")
            bt.delete_last_lines(1)
            print("\nSó resta um local para explorar agora...")
            print("\nADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")

            if "chave" not in meus_objetos_coletados:
                while x < 1:
                    coleta_de_objetos = int(input("\nVocê encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não  >>>"))
                    if coleta_de_objetos == 1:
                        x += 1
                        meus_objetos_coletados.append("chave")
                        print("\nChave coletada!")
                        print("\nSeu novo item é chave!")
                    elif coleta_de_objetos == 2:
                        x += 1
                        print("OK!")
                    else:
                        print("\nComando não conhecido, tente novamente.")

            print("\nVocê chegou ao topo da montanha...")
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
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance!")
                    bt.enter()
                    print("\nADICIONAR DESCRIÇÃO DO CAMINHO AO TOPO DA MONTANHA")
                    print(retornar("Topo da montanha", jogador, meus_objetos_coletados, meus_atributos, hp, arma))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram!")
                        return(f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
