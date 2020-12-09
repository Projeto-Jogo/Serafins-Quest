# MÓDULO "DESERTO"

import Batalha as bt  # Importa o módulo "Batalha"


def dunas(jogador, objetos_coletados, hp):
    # Função utilizada para a trajetória do jogador nas dunas de areia do deserto

    print("ADICIONAR DESCRIÇÃO DAS DUNAS DO DESERTO")
    a = b = c = d = e = f = 0  # Variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    pedra = 0
    pocao = 0
    objetos_coletados_nas_dunas = []

    if "pedra" in objetos_coletados and "poção" in objetos_coletados:  # Se o jogador já coletou a pedra e a poção, aparece um aviso de que não há mais objetos para coletar no local
        return (f'Você ja coletou os objetos que necessitava aqui!')
    elif "pedra" in objetos_coletados and "poção" not in objetos_coletados:  # Se o jogador já coletou a pedra, encontra apenas uma poção
        while a < 1:
            escolha_1 = int(input(
                "Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não"))  # O jogador escolhe se quer coletar a poção ou não
            if escolha_1 == 1:
                a += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("poção")
                objetos_coletados_nas_dunas.append("poção")
                while b < 1:
                    escolha_2 = int(input("Beber poção? 1 - Sim / 2 - Não"))
                    if escolha_2 == 1:
                        b += 1
                        bt.delete_last_lines(1)
                        hp -= 10
                        return (f'Ah, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {hp}')
                        if hp <= 0:
                            bt.game_over()
                    elif escolha_2 == 2:
                        b += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                        print("Poção coleada!")
                        return (f'Seu novo item é poção!')
                    else:
                        print("Escolha uma opção válida!")
            elif escolha_1 == 2:
                a += 1
                print("OK!")
                return (f'Você não coletou nenhum novo item!')
            else:
                print("Comando não conhecido, tente novamente.")
    elif "poção" in objetos_coletados and "pedra" not in objetos_coletados:
        while c < 1:
            c += 1
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                c += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("pedra")
                objetos_coletados_nas_dunas.append("pedra")
                print("Pedra coletada!")
                return (f'Seu novo item é pedra!')
            elif escolha == 2:
                c += 1
                print("OK!")
                bt.delete_last_lines(1)
                return (f'Você não coletou nenhum novo item!')
            else:
                print("Comando não conhecido, tente novamente.")
    else:
        while d < 1:
            escolha = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                pocao = 1
                d += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("poção")
                objetos_coletados_nas_dunas.append("poção")
                while e < 1:
                    escolha_2 = int(input("Beber poção? 1 - Sim / 2 - Não"))
                    if escolha_2 == 1:
                        e += 1
                        bt.delete_last_lines(1)
                        hp -= 10
                        print(f'Ah, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {hp}')
                    elif escolha_2 == 2:
                        e += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                        print("Poção coletada!")
                    else:
                        print("Escolha uma opção válida!")
            elif escolha == 2:
                d += 1
                print("OK!")
            else:
                print("Comando não conhecido, tente novamente.")
        print("ADICIONAR DESCRIÇÃO DE UM CAMINHO")
        bt.enter()
        while f < 1:
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                pedra = 1
                f += 1
                # bt.delete_last_lines(1)
                objetos_coletados.append("pedra")
                objetos_coletados_nas_dunas.append("pedra")
                print("Pedra coletada!")
            elif escolha == 2:
                f += 1
                print("OK!")
            else:
                print("Escolha uma opção válida!")
                
        if pocao == 1 and pedra == 1:
            return (f'Seus novos itens são {objetos_coletados_nas_dunas[0]} e {objetos_coletados_nas_dunas[1]}!')
        elif pocao == 1 and pedra == 0:
            return(f'Seu novo item é {objetos_coletados_nas_dunas[0]}')
        elif pocao == 0 and pedra == 1:
            return(f'Seu novo item é {objetos_coletados_nas_dunas[0]}')
        else:
            return(f'Você não coletou nenhum novo item!')

def topo_da_montanha(objetos_coletados):
    # Funçao utilizada para a trajetória do jogador no topo de uma montanha no deserto
    a = 0
    if "flor" in objetos_coletados:
        return (f'Você ja coletou o objeto que necessitava aqui!')
    else:
        while a < 1:
            escolha = int(input("Você encontrou uma flor do deserto! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("flor")
                a += 1
                bt.delete_last_lines(1)
                return (f'Seu novo item é uma flor do deserto!')
            elif escolha == 2:
                a += 1
                print("OK!")
                return (f'Você não coletou novos itens!')
            else:
                print("Comando não conhecido, tente novamente.")


def oasis(jogador, objetos_coletados, atributos, hp, arma):

# Função utilizada para a trajetória do jogador em um oasis no deserto

    a = b = c = d = e = f = 0 #
    desbloqueio = False
    missao_cumprida = False
    combinacao_correta = ["poção", "flor", "runa", "pedra"]
    pocoes = []
    
    print("Apresente uma sequência de 4 objetos como código para desbloquear a passagem ao oasis!")
    objeto_1 = input("Qual é o primeiro objeto da sequência?")
    if objeto_1 not in combinacao_correta:
        print("Objeto não identificado, tente novamente.")
        return oasis(objetos_coletados, atributos)
    elif objeto_1 in combinacao_correta and objeto_1 not in objetos_coletados:
        return(f'Você não possui o objeto {objeto_1}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente desbloquear a passagem ao oasis novamente!1')
    else:
        objeto_2 = input("Qual é o segundo objeto da sequência?")
        if objeto_2 not in combinacao_correta:
            print("Objeto não identificado, tente novamente.")
            return oasis(objetos_coletados, atributos)
        elif objeto_2 in combinacao_correta and objeto_2 not in objetos_coletados:
            return(f'Você não possui o objeto {objeto_2}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')    
        else:
            objeto_3 = input("Qual é o terceiro objeto da sequência?")
            if objeto_3 not in combinacao_correta:
                print("Objeto não identificado, tente novamente.")
                return oasis(objetos_coletados, atributos)         
            elif objeto_3 in combinacao_correta and objeto_3 not in objetos_coletados:
                return(f'Você não possui o objeto {objeto_3}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')
            else:
                objeto_4 = input("Qual é o quarto objeto da sequência?")
                if objeto_4 not in combinacao_correta:
                    print("Objeto não identificado, tente novamente.")
                    return oasis(objetos_coletados, atributos)
                elif objeto_4 in combinacao_correta and objeto_4 not in objetos_coletados:
                    return(f'Você não possui o objeto {objeto_4}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')
                else:
                    if(objeto_1 == combinacao_correta[0] and objeto_2 == combinacao_correta[1] and objeto_3 == combinacao_correta[2] and objeto_4 == combinacao_correta[3]):
                        desbloqueio = True
                        bt.delete_last_lines(5)
                        print(f'Parabéns! Você conseguiu entrar no ao oasis!')
                        bt.enter()

                        bt.passar_nivel(jogador)
                        print("ADICIONAR DESCRIÇÃO DO OASIS")
                        bt.enter()

                        print("Há uma serpente no caminho!")
                        print(bt.batalha(Serpente, jogador))

                        print("Siga para o lago agora...")
                        bt.enter()
                        bt.delete_last_lines(1)
                        print("Você mergulhou no lago!")
                        bt.enter()
                        bt.delete_last_lines(1)
                        print("ADICIONAR DESCRIÇÃO DO LAGO")
                        print("Parece que há algo lá no fundo, a alguns metros...")
                        bt.enter()
                        #bt.delete_last_lines(1)
                        print("Nadando e chegando mais perto, você vê que é um báu!")
                        while c < 1:
                            escolha_1 = int(input("O que deseja fazer? 1 - Coletar o baú / 2 - Sair do lago "))
                            if escolha_1 == 1:
                                c += 1
                                bt.delete_last_lines(1)
                                print("Você pegou o baú!")
                                print("Saia do lago agora e veja o que há dentro dele...")
                                bt.enter()
                                print("ADICIONAR DESCRIÇÃO DO JOGADOR SAINDO DO LAGO")
                                bt.delete_last_lines(1)
                                abertura_do_bau = int(input("Digite 1 para abrir o baú! "))
                                if abertura_do_bau == 1:
                                    d += 1
                                    if "chave" in objetos_coletados:
                                        print("Você conseguiu!")
                                        print(bt.passar_nivel(jogador))
                                        while e < 1:
                                            beber_pocao_brilhante = int(input("Há uma poção brilhante lá dentro! Digite 1 para bebê-la..."))
                                            if beber_pocao_brilhante == 1:
                                                e += 1
                                                hp += 20
                                                objetos_coletados.append("poção brilhante")
                                                print(f'Você ganhou 20 HPs após beber a poção! Seus HPs: {hp}')

                                        print("Também há uma nota dentro do baú... leia!")
                                        bt.enter()
                                        bt.delete_last_lines(1)
                                        print("Na nota está escrito 'URSO'..")
                                        print("Hmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
                                        bt.enter()
                                        while f < 1:
                                            nova_arma = int(input("Você encontrou um chicote no caminho! Digite 1 para obtê-lo como arma!"))
                                            if nova_arma == 1:
                                                f += 1
                                                arma = "chicote"
                                                print(f'Sua nova arma: {arma}')
                                            else:
                                                print("Comando não conhecido, tente novamente.")
                                        missao_cumprida = True
                                    else:
                                        d += 1
                                        print("Oops! Você ainda não tem a chave para abrir o baú! Continue sua exploração pelo deserto e colete-a!")
                                else:
                                    print("Abra o baú!")
                            elif escolha_1 == 2:
                                c += 1
                                print("Você saiu do lago. Parece que não há mais nada para fazer aqui...")
                            else:
                                print("Comando não conhecido, tente novamente.")
    if desbloqueio == False:
        return(f'Combinação incorreta! Você não conseguiu acesso ao oasis! Tente novamente!')
    if missao_cumprida == False:
        return(f'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...')
    elif missao_cumprida == True:
        return(f'Parabéns! Você cumpriu esta etapa, obtendo uma dica para seguir em sua jornada!')

def retornar(local, objetos_coletados, atributos):
    
    # Função utilizada para que o jogador possa retornar a locais que ele já explorou anteriormente
    i = 0
    j = 0
    
    if local == "Topo da montanha":
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ O TOPO DA MONTANHA")
        print("Você voltou ao topo da montanha!")
        bt.delete_last_lines(1)
        print(topo_da_montanha(objetos_coletados))
        if "chave" not in objetos_coletados:
                while i < 1:
                    coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        i += 1
                        objetos_coletados.append("chave")
                        print("Chave coletada!")
                        print("Seu novo item é chave!")
                    elif coleta_de_objetos == 2:
                        i += 1
                        print("OK!")
        print("Siga às dunas agora...")
        bt.nter()
        bt.delete_last_lines(1)
        print(dunas(objetos_coletados))
        print("Agora só resta explorar o oasis novamente...")
        print(oasis(objetos_coletados, atributos))
        if "poção brilhante" not in objetos_coletados:
            return (f'Você não conseguiu cumprir a missão...')
        else:
            return (f'Dessa vez você conseguiu!')

    elif local == "Dunas":
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ AS DUNAS")
        print("Você voltou às dunas")
        bt.delete_last_lines(1)
        print(dunas(objetos_coletados))
        print("Siga ao topo da montanha agora...")
        bt.enter()
        bt.delete_last_lines(1)
        print(topo_da_montanha(objetos_coletados))
        print("Agora só resta explorar o oasis novamente...")
        if "runa" not in objetos_coletados:
                while j < 1:
                    coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        j += 1
                        objetos_coletados.append("runa")
                        print("Runa coletada!")
                        print("Seu novo item é runa!")
                    elif coleta_de_objetos == 2:
                        j += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                    else:
                        print("Comando não conhecido, tente novamente.")
        print(oasis(objetos_coletados, atributos))
        if "poção_brilhante" not in objetos_coletados:
            return (f'Você não conseguiu cumprir a missão...')
        else:
            return (f'Dessa vez você conseguiu!')

def Deserto():
# Função principal que chama as demais funções (dunas(), topo_da_montanha() e oasis()), descrevendo toda a trajetória do jogador pela etapa do deserto.
    #
    #

    r = s = t = u = v = w = x = y = z = 0  # Variáveis de controle para o mecanismo de repetição (caso o jogador tenha digitado um comando inválido)
    meus_objetos_coletados = []
    forca = jogador["força"]
    destreza = jogador["destreza"]
    inteligencia = jogador["inteligência"]
    sorte = jogador["sorte"]
    carisma = jogador["carisma"]
    hp = jogador["hp"]
    arma = jogador["arma"]
    meus_atributos = [forca, destreza, inteligencia, sorte, carisma]
    
    print("Você está no deserto!")
    bt.enter()
    print("ADICIONAR DESCRIÇÃO INTRODUTÓRIA DO DESERTO")
    print(enter())
    bt.delete_last_lines(1)

    while r < 1:
        escolha_1 = int(input("Escolha um dos caminhos para seguir: 1 - Caminho 1 / 2 - Caminho 2 / 3 - Caminho 3"))
        if escolha_1 == 1:
            # CAMINHO 1: TOPO DA MONTANHA - OASIS - DUNAS
            r += 1
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ O TOPO DA MONTANHA")
            print("Você está no topo da montanha!")
            print(bt.enter())
            bt.delete_last_lines(1)
            print(topo_da_montanha(meus_objetos_coletados))
            print("Você está prosseguindo sua caminhada...")
            bt.delete_last_lines(1)
            print(enter())
            bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados:
                while s < 1:
                    coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        s += 1
                        meus_objetos_coletados.append("runa")
                        print("Runa coletada!")
                        print("Seu novo item é runa!")
                    elif coleta_de_objetos == 2:
                        s += 1
                        print("OK!")
                        # bt.delete_last_lines(1)
                    else:
                        print("Comando não conhecido, tente novamente.")

            print(enter())
            bt.delete_last_lines(1)
            print("O oasis está a alguns metros... siga até lá!")
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E O OASIS")
            print("Você chegou ao oásis...")
            bt.delete_last_lines(1)
            print(oasis(meus_objetos_coletados, meus_atributos))
            print("Só resta um local para explorar agora...")
            print(bt.enter())
            bt.delete_last_lines(1)
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS")

            print("Você encontrou uma serpente no caminho!")
            bt.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
            print(bt.enter())
            bt.delete_last_lines(1)
            
            if "poção" not in meus_objetos_coletados:
                while t < 1:
                    coleta_de_objetos = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    print("Você pode guardar esta poção mas não bebê-la!")
                    if coleta_de_objetos == 1:
                        t += 1
                        meus_objetos_coletados.append("poção")
                        print("Poção coletada!")
                        print("Seu novo item é poção!")
                    elif coleta_de_objetos == 2:
                        t += 1
                        print("OK!")
                    else:
                        print("Comando não conhecido, tente novamente.")

            print("Você chegou às dunas do deserto...")
            print(dunas(meus_objetos_coletados))
            
            if "poção brilhante" not in meus_objetos_coletados:
                print("Você não conseguiu acesso ao oasis para cumprir sua missão nesta etapa...")
                print("Você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("Primeiramente siga às dunas...")
                print("ADICIONAR DESCRIÇÃO DO CAMINHO ÀS DUNAS")
                bt.enter()
                print(retornar("Dunas", meus_objetos_coletados, meus_atributos))
                if "poção brilhante" not in meus_objetos_coletados:
                    print("Hmm... parece que você não conseguiu de novo. Aproveite sua última chance!")
                    bt.enter()
                    print("ADICIONAR DESCRIÇÃO DO CAMINHO AO TOPO DA MONTANHA")
                    print(retornar("Topo da montanha", meus_objetos_coletados, meus_atributos))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("Suas chances acabaram!")
                        return(f'Você não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')

        elif escolha_1 == 2:
            # CAMINHO 2: DUNAS - TOPO DA MONTANHA - OASIS
            r += 1
            print("Você está nas dunas do deserto...")
            print("ADICIONAR DESCRIÇÃO DAS DUNAS")
            print(bt.enter())
            bt.delete_last_lines(1)
            print(dunas(meus_objetos_coletados))
            print("Você está prosseguindo sua caminhada...")
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")

            if "chave" not in meus_objetos_coletados:
                while u < 1:
                    coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        u += 1
                        meus_objetos_coletados.append("chave")
                        print("Chave coletada!")
                        print("Seu novo item é chave!")
                    elif coleta_de_objetos == 2:
                        u += 1
                        print("OK!")

            print(enter())
            bt.delete_last_lines(1)
            print("Você chegou ao topo da montanha...")
            print(topo_da_montanha(meus_objetos_coletados))
            print("Só resta um local para explorar agora...")
            print("Um oasis está há alguns metros... siga até lá!")
            print(bt.enter())
            # bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados:
                while v < 1:
                    coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        v += 1
                        meus_objetos_coletados.append("runa")
                        print("Runa coletada!")
                        print("Seu novo item é runa!")
                    elif coleta_de_objetos == 2:
                        v += 1
                        print("OK!")

            print(bt.enter())
            bt.delete_last_lines(1)
            print("Você chegou ao oásis...")
            print(oasis(meus_objetos_coletados, meus_atributos))
            
            if "poção brilhante" not in meus_objetos_coletados:
                print("Você não conseguiu acesso ao oasis para cumprir sua missão nesta etapa...")
                print("Você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("Primeiramente siga novamente ao topo da montanha...")
                print("ADICIONAR DESCRIÇÃO DO CAMINHO AO TOPO DA MONTANHA")
                bt.enter()
                print(retornar("Topo da montanha", meus_objetos_coletados, meus_atributos))
                if "poção brilhante" not in meus_objetos_coletados:
                    print("Hmm... parece que você não conseguiu de novo. Aproveite sua última chance!")
                    enter()
                    print("ADICIONAR DESCRIÇÃO DO CAMINHO ÀS DUNAS")
                    print(retornar("Dunas", meus_objetos_coletados, meus_atributos))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("Suas chances acabaram!")
                        return(f'Você não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')

        elif escolha_1 == 3:
            # CAMINHO 3: OASIS - DUNAS - TOPO DA MONTANHA
            r += 1
            print("Você está no oásis!")
            print(oasis(meus_objetos_coletados, meus_atributos))
            print("Você está prosseguindo sua caminhada...")
            print(bt.enter())
            bt.delete_last_lines(1)
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS")
            print("Você encontrou uma serpente no caminho!")
            bt.batalha(Serpente, jogador)  # Chamada da função "batalha" do módulo "Batalha"
            print("ADICIONAR MAIS DESCRIÇÃO DE CAMINHO")

            if "runa" not in meus_objetos_coletados:
                while w < 1:
                    coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        w += 1
                        meus_objetos_coletados.append("runa")
                        print("Runa coletada!")
                        print("Seu novo item é runa!")
                    elif coleta_de_objetos == 2:
                        w += 1
                        print("OK!")
                    else:
                        print("Comando não conhecido, tente novamente.")

            print("Você chegou às dunas do deserto...")
            bt.enter()
            bt.delete_last_lines(1)
            print(dunas(meus_objetos_coletados))
            print("Você está prosseguindo sua caminhada...")
            bt.delete_last_lines()
            print("Só resta um local para explorar agora...")
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")

            if "chave" not in meus_objetos_coletados:
                while x < 1:
                    coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        x += 1
                        meus_objetos_coletados.append("chave")
                        print("Chave coletada!")
                        print("Seu novo item é chave!")
                    elif coleta_de_objetos == 2:
                        x += 1
                        print("OK!")
                    else:
                        print("Comando não conhecido, tente novamente.")

            print("Você chegou ao topo da montanha...")
            bt.enter()
            # bt.delete_last_lines(1)
            print(topo_da_montanha(meus_objetos_coletados))

            if "poção brilhante" not in meus_objetos_coletados:
                print("Você não conseguiu acesso ao oasis para cumprir sua missão nesta etapa...")
                print("Você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("Primeiramente siga às dunas...")
                print("ADICIONAR DESCRIÇÃO DO CAMINHO ÀS DUNAS")
                bt.enter()
                print(retornar("Dunas", meus_objetos_coletados, meus_atributos))
                if "poção brilhante" not in meus_objetos_coletados:
                    print("Hmm... parece que você não conseguiu de novo. Aproveite sua última chance!")
                    bt.enter()
                    print("ADICIONAR DESCRIÇÃO DO CAMINHO AO TOPO DA MONTANHA")
                    print(retornar("Topo da montanha", meus_objetos_coletados, meus_atributos))
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("Suas chances acabaram!")
                        return(f'Você não cumpriu esta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')					  
                    else:
                        return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
                else:
                    return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
            else:
                return(f'Você cumpriu a missão! Está pronto(a) para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')
