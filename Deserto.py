# MÓDULO "DESERTO"

import Batalha as bt  # Importa o módulo "Batalha"


def dunas(jogador, objetos_coletados):
    # Função utilizada para a trajetória do jogador nas dunas do deserto

    a = b = c = d = e = f = 0  # Variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    pedra = 0  # Variável utilizada para saber se o jogador coletou uma pedra nas dunas
    pocao = 0  # Variável utilizada para saber se o jogador coletou uma poção nas dunas
    objetos_coletados_nas_dunas = []
    
    if "pedra" in objetos_coletados and "poção" in objetos_coletados:  # Se o jogador já coletou a pedra e a poção, aparece um aviso de que não há mais objetos para coletar no local
        return (f'\nVocê ja coletou os objetos que necessitava aqui!')
    elif "pedra" in objetos_coletados and "poção" not in objetos_coletados:  # Se o jogador já coletou a pedra mas não a poção, ele encontra a poção
        while a < 1:
            print(
                '\n\u001b[37;1mChegando mais perto, você vê que é uma poção! Deseja coletá-la?\n (1) sim\n (2) não')  # O jogador escolhe se quer coletar a poção ou não
            escolha_1 = input(">>>")
            bt.delete_last_lines(1)
            print(f">>>{escolha_1}\u001b[0m\n")
            if escolha_1 == "1":
                a += 1
                bt.delete_last_lines(1)  # Chamada da função "delete_last_lines(n)" do módulo "Batalha, para deletar a linha anterior"
                objetos_coletados.append(
                    "poção")  # Se ele escolhe coletar a poção, esta é adicionada à sua lista geral de objetos coletados
                objetos_coletados_nas_dunas.append("poção")  # A poção também é adicionada à lista específica de objetos coletados nas dunas
                while b < 1:  # O jogador escolhe se quer beber a poção ou não
                    print('\n\u001b[37;1mBeber poção?\n (1) sim\n (2) não')  # O jogador escolhe se quer beber a poção ou não
                    escolha_2 = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{escolha_2}\u001b[0m\n")
                    if escolha_2 == "1":
                        b += 1
                        bt.delete_last_lines(1)
                        jogador["hp"] -= 10  # Se o jogador beber a poção, perde 10 HPs
                        bt.game_over(jogador)  # Chamada da função "game_over()" do módulo "Batalha"
                        return (f'\nAh, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {jogador["hp"]}')
                    elif escolha_2 == "2":  #  Se o jogador não beber a poção, apenas recebe um aviso
                        b += 1
                        print("OK!")
                        bt.delete_last_lines(1)
                        return (f'\nVocê não coletou novos itens!')
                    else:
                        print('\nEscolha uma opção válida!') # Verifica se o jogador escolheu uma opção válida (1 ou 2)
            elif escolha_1 == "2": # Se o jogador não quiser coletar a poção, apenas recebe um aviso 
                a += 1
                print("OK!")
                return (f'\nVocê não coletou nenhum novo item!')
            else:
                print('\nComando não conhecido, tente novamente.')
    elif "poção" in objetos_coletados and "pedra" not in objetos_coletados: # Se o jogador ainda não coletou a pedra, esta aparece no caminho para ele
        while c < 1:
            c += 1
            print('\n Você vê algo na areia, a poucos metros...')
            bt.enter()
            print('\n\u001b[37;1mChegando mais perto, você vê que é uma pedra preciosa! Deseja coletá-la?\n (1) sim\n (2) não') # Pergunda se o jogador deseja coletar a pedra preciosa
            escolha = input(">>>")
            bt.delete_last_lines(1)
            print(f">>>{escolha}\u001b[0m\n")
            if escolha == "1": 
                c += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("pedra") # Se o jogador escolher coletá-la, a é colocada em sua lista de objetos coletados
                objetos_coletados_nas_dunas.append("pedra")
                print("\n Pedra coletada!")
                return (f'\nSeu novo item é uma pedra preciosa!')
            elif escolha == "2":
                c += 1
                print("OK!")
                bt.delete_last_lines(1)
                return (f'\nVocê não coletou nenhum novo item!')
            else:
                print('\nComando não conhecido, tente novamente.') #Verifica se o jogador escolheu uma opção válida
    else:
        while d < 1:
            print('\n Você vê algo na areia, a poucos metros...')
            bt.enter()
            print('\n\u001b[37;1mChegando mais perto, vê que é uma poção! Deseja coletá-la?\n (1) sim\n (2) não') 
            escolha = input(">>>")
            bt.delete_last_lines(1)
            print(f">>>{escolha}\u001b[0m\n")
            if escolha == "1":
                pocao = 1
                d += 1
                bt.delete_last_lines(1)
                objetos_coletados.append("poção")
                objetos_coletados_nas_dunas.append("poção")
                while e < 1:
                    print('\n\u001b[37;1mBeber poção?\n (1) sim\n (2) não')
                    escolha_2 = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{escolha_2}\u001b[0m\n")
                    if escolha_2 == "1":
                        e += 1
                        bt.delete_last_lines(1)
                        jogador["hp"] -= 10
                        print(f'\nAh, não! Esta poção é perigosa! Você perdeu 10 HPs! Seus HPs: {jogador["hp"]}')
                        if jogador["hp"] <= 0:
                            bt.game_over(jogador)
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
        bt.enter()
        while f < 1:
            print('\n\u001b[37;1mCaminhando mais um pouco, você encontra uma pedra preciosa! Deseja coletá-la?\n (1) sim\n (2) não')
            escolha = input(">>>")
            bt.delete_last_lines(1)
            print(f">>>{escolha}\u001b[0m\n")
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
            return (f'\nSeu novo item é {objetos_coletados_nas_dunas[0]}')
        elif pocao == 0 and pedra == 1:
            return (f'\nSeu novo item é {objetos_coletados_nas_dunas[0]}')
        else:
            return (f'\nVocê não coletou nenhum novo item!')


def topo_da_montanha(objetos_coletados):
    # Funçao utilizada para a trajetória do jogador no topo de uma montanha no deserto

    a = 0  # Variável utilizada para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida

    if "flor" in objetos_coletados: # Se o jogador já coletou a flor do deserto na montanha, aparece um aviso de que ele já coletou tudo o que precisava nesse local
        return (f'\nVocê ja coletou o objeto que necessitava aqui!')
    else: # Se o jogador ainda não coletou a flor do deserto, esta aparece no caminho para que ele colete
        while a < 1: 
            print('\nVocê vê uma flor do deserto a poucos metros e caminha até ela...')
            bt.enter()
            print('\n\u001b[37;1mDeseja coletá-la?\n (1) sim\n (2) não')
            escolha = input(">>>")
            bt.delete_last_lines(1)
            print(f">>>{escolha}\u001b[0m\n")
            if escolha == "1": # Se o jogador escolher coletar a flor, ela é adicionada à sua lista de objetos coletados
                objetos_coletados.append("flor")
                a += 1
                bt.delete_last_lines(1)
                return (f'\nA flor do deserto foi adicionada aos seus itens!') 
            elif escolha == "2":
                a += 1
                print("OK!")
                return (f'\nVocê não coletou novos itens!')
            else:
                print('\nComando não conhecido, tente novamente.') # Verifica se o jogador fez uma escolha válida


primeira_vez = True


def oasis(jogador, objetos_coletados):
    # Função utilizada para a trajetória do jogador em um oasis no deserto

    global primeira_vez

    a = b = c = d = e = f = 0  # Variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    Serpente = {"nome": "Serpente", 'hp': 30, 'defesa': 2, 'força': 2} # Definição do inimigo: serpente
    desbloqueio = False
    missao_cumprida = False
    combinacao_correta = ["poção", "flor", "runa", "pedra"] # Combinação correta de objetos para resolver o enigma do oásis
    pocoes = []

    for n in range(len(objetos_coletados)):
        print(objetos_coletados[n], end=" ")

    if len(objetos_coletados) < 4: # Se o jogador não possuir os 4 objetos para resolver o enigma, é enviado a outros locais do deserto para que possa colecá-los
        return (f'\nParece que você ainda não possui os 4 objetos necessários! Explore outros locais do deserto primeiro e colete objetos...')
    else:
        print('\n\n\u001b[37;1mQual é o primeiro objeto da sequência?')
        objeto_1 = input(">>>")
        bt.delete_last_lines(1)
        print(f">>>{objeto_1}\u001b[0m\n")
        if objeto_1 not in combinacao_correta:
            print('\nObjeto não identificado, tente novamente.') # Verifica se o jogador digitou o nome de um objeto válido
            return oasis(jogador, objetos_coletados)
        elif objeto_1 in combinacao_correta and objeto_1 not in objetos_coletados: # Avisa se o jogador realmente possui o objeto informado
            return (
                f'\nVocê não possui o objeto {objeto_1}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente \ndesbloquear a passagem ao oasis novamente!')
        else:
            print('\n\u001b[37;1mQual é o segundo objeto da sequência?')
            objeto_2 = input(">>>")
            bt.delete_last_lines(1)
            print(f">>>{objeto_2}\u001b[0m\n")
            if objeto_2 not in combinacao_correta:
                print('\nObjeto não identificado, tente novamente.')
                return oasis(jogador, objetos_coletados)
            elif objeto_2 in combinacao_correta and objeto_2 not in objetos_coletados:
                return (
                    f'\nVocê não possui o objeto {objeto_2}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente \nconseguir a passagem ao oasis novamente!')
            else:
                print('\n\u001b[37;1mQual é o terceiro objeto da sequência?')
                objeto_3 = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{objeto_3}\u001b[0m\n")
                if objeto_3 not in combinacao_correta:
                    print('\nObjeto não identificado, tente novamente.')
                    return oasis(jogador, objetos_coletados)
                elif objeto_3 in combinacao_correta and objeto_3 not in objetos_coletados:
                    return (
                        f'\nVocê não possui o objeto {objeto_3}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente \nconseguir a passagem ao oasis novamente!')
                else:
                    print('\n\u001b[37;1mQual é o quarto objeto da sequência?')
                    objeto_4 = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{objeto_4}\u001b[0m\n")
                    if objeto_4 not in combinacao_correta:
                        print('\nObjeto não identificado, tente novamente.')
                        return oasis(jogador, objetos_coletados)
                    elif objeto_4 in combinacao_correta and objeto_4 not in objetos_coletados:
                        return (
                            f'\nVocê não possui o objeto {objeto_4}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente \nconseguir a passagem ao oasis novamente!')
                    else:
                        if (objeto_1 == combinacao_correta[0] and objeto_2 == combinacao_correta[1] and objeto_3 ==
                                combinacao_correta[2] and objeto_4 == combinacao_correta[3]): # Se o jogador acertar a combinação de objetos do enigma:
                            desbloqueio = True
                            bt.delete_last_lines(5)
                            print(f'\nMuito bem! Você conseguiu entrar no oásis!') # O jogador desbloqueia o acesso ao oásis
                            bt.enter()
                            if primeira_vez == True:
                                bt.passar_nivel(jogador)
                                primeira_vez = False
                                bt.enter()
                            print('\nVocê encontrou uma serpente no caminho!')
                            print(bt.batalha(Serpente, jogador)) # Chama a função 'batalha' do módulo 'Batalha' para a batalha com a Serpente
                            print('\nVocê segue para o lago agora...')
                            bt.enter()
                            bt.delete_last_lines(1)
                            print('\nVocê mergulhou no lago!')
                            bt.delete_last_lines(1)
                            print(
                                'O lago é profundo e sua água é turva. Você não consegue enxergar muito bem, mas vê algo no fundo...')
                            bt.enter()
                            bt.delete_last_lines(1)
                            print('\nNadando e chegando mais perto, você percebe que é um baú!')

                            while c < 1:
                                print('\n\u001b[37;1mO que deseja fazer?\n (1) Coletar o baú\n (2) Sair do lago') # O jogador escolhe se quer coletar o baú submerso no lago ou se quer sair do lago
                                escolha_1 = input(">>>")
                                bt.delete_last_lines(1)
                                print(f">>>{escolha_1}\u001b[0m\n")
                                if escolha_1 == "1": # Se o jogador escolher coletar o baú:
                                    c += 1
                                    bt.delete_last_lines(1)
                                    print("\nVocê pegou o baú!")
                                    print("\nSaia do lago agora e veja o que há dentro dele...")
                                    bt.enter()
                                    print("Você sai do lago, sentando-se à sua beira...")
                                    bt.delete_last_lines(1)
                                    while d < 1:
                                        print("\u001b[37;1mDigite 1 para abrir o baú!")
                                        abertura_do_bau = input(">>>")
                                        bt.delete_last_lines(1)
                                        print(f">>>{abertura_do_bau}\u001b[0m\n")
                                        if abertura_do_bau == "1":
                                            d += 1
                                            if "chave" in objetos_coletados: # Verifica se o jogador tem a chave para abrir o baú
                                                print("\nVocê conseguiu!")
                                                while e < 1:
                                                    print(
                                                        "\n\u001b[37;1mHá uma poção brilhante lá dentro! Digite 1 para bebê-la...") # O jogador encontra uma poção brilhante dentro do baú e deve bebê-la
                                                    beber_pocao_brilhante = input(">>>")
                                                    if beber_pocao_brilhante == "1":
                                                        e += 1
                                                        jogador["hp"] += 20
                                                        objetos_coletados.append("poção brilhante")
                                                        print(
                                                            f'\nVocê ganhou 20 HPs após beber a poção! Seus HPs: {jogador["hp"]}') 
                                                            # O jogador ganha 20 HPs após beber a poção
                                                    else:
                                                        print(f'Comando não conhecido, tente novamente.')
                                                print("\nTambém há uma nota dentro do baú... leia!")
                                                bt.enter()
                                                bt.delete_last_lines(1)
                                                print("\nNa nota está escrito 'URSO'..")
                                                print("\nHmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
                                                missao_cumprida = True
                                            else:
                                                print(
                                                    "\nOops! Você ainda não tem a chave para abrir o baú! Continue sua exploração pelo deserto e colete-a!") # Se o jogador não tiver a chave para abrir o baú, ele recebe um aviso
                                        else:
                                            print('\nComando não conhecido, tente novamente!') # Verifica se o jogador informou um comando válido 
                                elif escolha_1 == "2":
                                    c += 1
                                    print('\nVocê sai do lago, sentando-se à sua beira...')
                                    bt.enter()
                                    print('\nParece que não há mais nada para fazer aqui...') # Se o jogador não coletar o baú e sair do lago, recebe um aviso de que não há mais nada para fazer naquele/// local...
                                else:
                                    print('\nComando não reconhecido, tente novamente.')

                                while f < 1:
                                    print("\n\u001b[37;1mVocê encontrou um chicote no caminho! Digite 1 para obtê-lo como arma!") # O jogador encontra uma nova arma, um chicote
                                    nova_arma = input(">>>")
                                    bt.delete_last_lines(1)
                                    print(f">>>{nova_arma}\u001b[0m\n")
                                    if nova_arma == "1":
                                        f += 1
                                        chicote = {"nome": "chicote", "atributo": "DES", "dano": "2-4", "min": 2, "max": 4}
                                        jogador["arma"] = chicote # A arma que o jogador tinha anteriormente é substituída por um chicote
                                        print(f'\nSua nova arma: {jogador["arma"]["nome"]}')
                                    else:
                                        print("\nComando não conhecido, tente novamente.")

    if desbloqueio == False:
        return (f'\nCombinação incorreta! Você não conseguiu advinhar a sequência e obter acesso ao oásis! Tente novamente!')
    if missao_cumprida == False:
        return (f'\nVocê não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...')
    elif missao_cumprida == True:
        return (f'\nParabéns! Você cumpriu esta etapa, obtendo uma dica para seguir em sua jornada!')


def retornar(local, jogador, objetos_coletados):
    # Função utilizada para que o jogador possa retornar a locais que ele já explorou anteriormente
    i = 0
    j = 0

    if local == "Topo da montanha":
        print("\nVocê voltou ao topo da montanha...")
        bt.delete_last_lines(1)
        print(topo_da_montanha(objetos_coletados))
        if "chave" not in objetos_coletados:
            while i < 1:
                print("\n\u001b[37;1mVocê encontrou uma chave! Deseja coletá-la?\n (1) sim\n (2) não")
                coleta_de_objetos = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{coleta_de_objetos}\u001b[0m\n")
                if coleta_de_objetos == "1":
                    i += 1
                    objetos_coletados.append("chave")
                    print("\nChave coletada!")
                    print("\nSeu novo item é chave!")
                elif coleta_de_objetos == "2":
                    i += 1
                    print("OK!")
        print("\nAgora você pode visitar as dunas novamente...")
        bt.enter()
        print("\nVocê faz o caminho de descida da montanha rapidamente e segue às dunas do deserto novamente...")
        bt.delete_last_lines(1)
        
        print(dunas(jogador, objetos_coletados))
        
        print("\nSó resta explorar o oásis novamente...")
        print("\nVocê retornou ao oásis...")
        bt.enter()
        
        print(oasis(jogador, objetos_coletados))
        
        if "poção brilhante" not in objetos_coletados:
            return (f' ')
        else:
            return (f'\nDessa vez você conseguiu!')

    elif local == "Dunas":
        print("\nVocê voltou às dunas...")
        bt.delete_last_lines(1)
        
        print(dunas(jogador, objetos_coletados))
        print("\nVocê pode seguir ao topo da montanha novamente agora...")
        bt.enter()
        print("\nVocê faz o caminho já conhecido e chega até lá...")
        bt.delete_last_lines(1)
        
        print(topo_da_montanha(objetos_coletados))

        print("\Só resta um local para retornar agora...")
        bt.enter()
        
        if "runa" not in objetos_coletados:
            while j < 1:
                print("\u001b[37;1mVocê encontrou uma runa! Deseja coletá-la?\n (1) sim\n (2) não")
                coleta_de_objetos = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{coleta_de_objetos}\u001b[0m\n")
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

        print("\nVocê voltou ao oásis!")
        print("\nTente desbloquear a passagem novamente...")
        bt.enter()

        print(oasis(jogador, objetos_coletados))

        if "poção_brilhante" not in objetos_coletados:
            return (f' ')
        else:
            return (f'\nDessa vez você conseguiu!')


def Deserto(jogador):
    # Função principal que chama as demais funções (dunas(), topo_da_montanha() e oasis()), descrevendo toda a trajetória do jogador pela etapa do deserto.

    r = s = t = u = v = w = x = y = z = 0  # Variáveis de controle para o mecanismo de repetição (caso o jogador tenha digitado um comando inválido)
    Serpente = {"nome": "Serpente", 'hp': 30, 'defesa': 2, 'força': 2}

    meus_objetos_coletados = []
    print("\nVOCÊ CHEGOU AO DESERTO!") # Introdução ao jogador
    bt.enter()
    print("\nSua primeira visão é de uma planície interminável e você se sente perdido(a)...")
    bt.enter()
    bt.delete_last_lines(1)

    while r < 1: # O jogador escolhe qual caminho deseja seguir no deserto
        print(
            "\n\u001b[37;1mInicialmente, você tem três opções de caminhos para seguir. Escolha um deles:\n (1) Caminho 1 \n (2) Caminho 2 \n (3) Caminho 3")
        escolha_1 = input(">>>")
        bt.delete_last_lines(1)
        print(f">>>{escolha_1}\u001b[0m\n")
        if escolha_1 == "1": # Se o jogador escolher o caminho 1
            # CAMINHO 1: TOPO DA MONTANHA - OASIS - DUNAS
            r += 1
            print("\nVocê escolheu o caminho 1. Você segue para o leste, a caminho de uma grande montanha...")
            bt.enter()
            print("\nO caminho é relativamente longo, mas você caminha rapidamente e não demora muito a encontrar a montanha.")
            print("\nSeu destino é o topo da montanha. Ao chegar até ela, você encontra uma subida bastante íngreme.")
            bt.enter()
            print("\nApós uma longa caminhada, você finalmente chega...")
            print('\nVocê se encontra no topo da montanha. O vento é mais ainda mais forte e, pela altura, você tem uma visão ampla de grande\nparte do deserto...')
            bt.enter()
            bt.delete_last_lines(1)

            print(topo_da_montanha(meus_objetos_coletados)) # Chama a função 'topo_da_montanha(meus_objetos_coletados)' quando o jogador chegar ao topo da montanha

            print("\nVocê está descendo a montanha agora...")
            bt.delete_last_lines(1)
            bt.enter()
            bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados: # O jogador encontra uma runa no caminho e decide se quer coletá-la ou não
                while s < 1:
                    print("\n\u001b[37;1mVocê encontrou uma runa no caminho! Deseja coletá-la?\n (1) sim \n (2) não")
                    coleta_de_objetos = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{coleta_de_objetos}\u001b[0m\n")
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
            bt.enter()
            print("\nApós aproximadamente 1 hora de caminhada, você está quase chegando ao seu próximo destino...")
            print("\nHá um oásis está a alguns metros de distância e você deve seguir até lá!")
            bt.enter()
            bt.delete_last_lines(1)

            print('\nVocê chegou ao oásis, que se destaca muito em meio àquela paisagem remota... é quase surreal ver um imenso lago, a \nvegetação e alguns coqueiros em meio ao deserto.')
            bt.enter()
            print('\nPorém você não pode ir até ele, pois há um bloqueio na passagem...\nAo lado há um rochedo com inscrições, mais \nsimilares a um hieroglifo...')
            bt.enter()
            print('\n\nO primeiro entalhe parece ser um vaso, o segundo uma árvore,\no terceiro um escriba e o quarto entalhe está desgastado, não dando para ver o que representa.\n')
            bt.enter()
            print(f'\nPara desbloquear o caminho você deve apresentar 4 objetos dos quais você coletou, em uma determinada sequência...\nVocê tem disponiveis esses objetos:')

            print(oasis(jogador, meus_objetos_coletados)) # Chama a função 'oasis(meus_objetos_coletados) quando o jogador chega ao oásis

            print("\nSó resta um local para explorar agora...")
            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê segue em direção ao seu destino final no deserto...")
            print("\nVocê continua caminhando pela mesma estrada...")
            bt.enter()
            print("\nVocê entra em um estreito caminho, partindo da estrada, e segue para o leste...")

            print("\nVocê encontrou uma serpente no caminho!")
            bt.batalha(Serpente, jogador)  # chamada da função "batalha" do módulo "Batalha"
            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê então segue em sua caminhada...")
            bt.enter()
            print("\nVocê vê algo na areia, a poucos metros...")
            bt.enter()
            if "poção" not in meus_objetos_coletados: # O jogador encontra uma poção no caminho e decide se quer coletá-la ou não
                while t < 1:
                    print("\n\u001b[37;1mChegando mais perto, você vê que é uma poção! Deseja coletá-la?\n (1) sim \n (2) não")
                    coleta_de_objetos = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{coleta_de_objetos}\u001b[0m\n")
                    print("\nVocê pode guardar esta poção, mas não bebê-la!")
                    if coleta_de_objetos == "1":
                        t += 1
                        meus_objetos_coletados.append("poção")
                        print("\nPoção coletada!")
                        print("\nA poção foi adicionada aos seus itens!!")
                    elif coleta_de_objetos == "2":
                        t += 1
                        print("\nOK!")
                    else:
                        print("\nComando não conhecido, tente novamente.")

            print("\nFinalmente, após alguns minutos de caminhada, você chega ao destino.")
            bt.enter()
            print('\nVocê se encontra nas dunas do deserto, que parecem não ter fim. O vento é forte, fazendo com que elas se movimentem. \nNão há nada ao seu redor além de areia, e você não sabe para onde ir...')
            bt.enter()

            print(dunas(jogador, meus_objetos_coletados))

            if "poção brilhante" not in meus_objetos_coletados: # Verifica se o jogador cumpriu a missão do deserto. Se não cumpriu, ele tem mais duas chances para retornar a outros locais, coletar objetos e depois tentar cumprir a missão novamente
                print("\nParece que você ainda não conseguiu desbloquer o acesso ao oásis...")
                bt.enter()
                print("\nPor isso, você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nVocê pode começar explorando as dunas novamente...")
                bt.enter()
                print(retornar("Dunas", jogador, meus_objetos_coletados)) # Chama a função 'retornar' para que o jogador retorne às dunas do deserto

                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance agora!")
                    bt.enter()
                    print("Você tem uma chance de explorar o topo da montanha novamente... você segue até lá.")
                    bt.enter()
                    print("O caminho da subida é cansativo, mas você finalmente chega ao destino...")
                    print(retornar("Topo da montanha", jogador, meus_objetos_coletados)) # Chama a função 'retornar' para que o jogador retorne ao topo da montanha
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram... você não pode mais explorar nenhum local no deserto.")
                        return (
                            f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada.')
                    else:
                        return (
                            f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')
                else:
                    return (
                        f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')
            else:
                return (
                    f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')

        elif escolha_1 == "2": # Se o jogador escolher o caminho 2
            # CAMINHO 2: DUNAS - TOPO DA MONTANHA - OASIS
            r += 1
            print("\nVocê escolheu o caminho 2. Você segue por um caminho estreito..")
            bt.enter()
            print("\nApós uma curta caminhada, você chega às dunas do deserto...")
            print(
                '\nAs dunas parecem não ter fim. O vento é forte, fazendo com que elas se movimentem. Não há nada ao seu redor além de \nareia, e você não sabe para onde ir...')
            bt.enter()
            bt.delete_last_lines(1)

            print(dunas(jogador, meus_objetos_coletados)) # Chama a função 'dunas' quando o jogador chega às dunas do deserto

            print("\nVocê continua seu caminho...")
            bt.enter()
            print(
                "\nVocê segue por uma longa estrada. A temperatura está bastante elevada, fazendo com que o caminho pareça ainda mais longo.")

            if "chave" not in meus_objetos_coletados: # O jogador encontra uma chave no caminho e decide se quer coletá-la ou não
                while u < 1:
                    print("\n\u001b[37;1mVocê encontrou uma chave! Deseja coletá-la?\n (1) sim\n (2) não")
                    coleta_de_objetos = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{coleta_de_objetos}\u001b[0m\n")
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
            print(
                "\nMesmo assim, você não pode desistir. Você começa a subir a montanha, percebendo um caminho muito íngreme.")
            bt.enter()
            print("\nApós a difícil caminhada, você finalmente chega ao desino...")
            print(
                '\nVocê se encontra no topo da montanha. O vento é mais ainda mais forte e, pela altura, você tem uma visão ampla de grande\n parte do deserto...')
            bt.enter()
            bt.delete_last_lines(1)

            print(topo_da_montanha(meus_objetos_coletados)) # chama a função 'topo_da_montanha' quando o jogador chega ao topo da montanha

            print("\nVocê está descendo a montanha agora...")
            print("\nSó resta um local para explorar agora...")
            bt.enter()
            print("Um oásis está há alguns metros... siga até lá!")
            bt.enter()
            bt.delete_last_lines(1)

            if "runa" not in meus_objetos_coletados: # O jogador encontra uma runa no caminho e decide se deseja coletá-la ou não
                while v < 1:
                    print("\n\u001b[37;1mVocê encontrou uma runa! Deseja coletá-la?\n (1) sim\n (2) não")
                    coleta_de_objetos = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{coleta_de_objetos}\u001b[0m\n")
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
            print('\nVocê chegou ao oásis, que se destaca muito em meio àquela paisagem remota, e achou surreal ver um imenso lago, a \nvegetação e alguns coqueiros em meio ao deserto.')
            bt.enter()
            print('\nPorém, você não pode ir até ele, pois há um bloqueio na passagem...\nAo lado há um rochedo com inscrições, mais \nsimilares a um hieroglifo...')
            bt.enter()
            print('\n\nO primeiro entalhe parece ser um vaso, o segundo uma árvore,\no terceiro um escriba e o quarto entalhe está desgastado, não dando para ver o que representa.\n')
            bt.enter()
            print(f'\nPara desbloquear o caminho você deve apresentar 4 objetos dos quais você coletou, em uma determinada sequência...\nVocê tem disponiveis esses objetos:')

            print(oasis(jogador, meus_objetos_coletados)) # chama a função 'oasis' quando o jogador chega ao oásis

            if "poção brilhante" not in meus_objetos_coletados: # Verifica se o jogador cumpriu a missão do deserto
                print("\nParece que você não conseguiu desbloquear o caminho ao oásis...")
                bt.enter()
                print("\nPor isso, você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nVocê pode começar explorando o topo da montanha novamente...")
                bt.enter()
                print(retornar("Topo da montanha", jogador, meus_objetos_coletados)) # Chamada da função 'retornar' para que o jogador volte à outros locais os quais já explorou e tente completar a missão
                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance agora!")
                    bt.enter()
                    print("Você tem uma chance para explorar as dunas do deserto novamente ... você segue até lá.")
                    bt.enter()
                    print(retornar("Dunas", jogador, meus_objetos_coletados)) # Chamada da função 'retornar' para que o jogador volte à outros locais os quais já explorou e tente completar a missão
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram... você não pode mais explorar nenhum local no deserto.")
                        return (f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada.')
                    else:
                        return (
                            f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')
                else:
                    return (f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')
            else:
                return (f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')

        elif escolha_1 == "3": # Se o jogador escolhe o caminho 3
            # CAMINHO 3: OASIS - DUNAS - TOPO DA MONTANHA
            r += 1
            print(
                "\nVocê segue por um estreito caminho. Não há praticamente nada ao seu redor além de alguns cactos ao redor.")
            bt.enter()
            print("\nVocê também avista um lagarto do deserto em certo ponto da caminhada...")
            bt.enter()
            print("\n1 hora depois, você finalmente tem uma bonita vista à sua frente: há um oásis a alguns metros!")
            bt.enter()
            bt.enter()
            bt.delete_last_lines(1)
            print('\nVocê chegou ao oásis, que se destaca muito em meio àquela paisagem remota, e achou surreal ver um imenso lago, a \nvegetação e alguns coqueiros em meio ao deserto.')
            bt.enter()
            print('\nPorém, você não pode ir até ele, pois há um bloqueio na passagem...\nAo lado há um rochedo com inscrições, mais \nsimilares a um hieroglifo...')
            bt.enter()
            print('\n\nO primeiro entalhe parece ser um vaso, o segundo uma árvore,\no terceiro um escriba e o quarto entalhe está desgastado, não dando para ver o que representa.\n')
            bt.enter()
            print(f'\nPara desbloquear o caminho você deve apresentar 4 objetos dos quais você coletou, em uma determinada sequência...\nVocê tem disponiveis esses objetos:')

            print(oasis(jogador, meus_objetos_coletados)) # Chamada da função 'oasis' quando o jogador chega ao oásis 

            print("\nVocê está prosseguindo sua caminhada...")
            bt.enter()
            bt.delete_last_lines(1)
            print("\nVocê segue em direção ao seu próximo destino...")
            print("\nVocê caminha por uma longa estrada...")
            bt.enter()
            print("\nVocê entra em um outra estreito caminho, partindo da estrada, e segue para leste...")

            print("\nVocê encontrou uma serpente!")
            bt.batalha(Serpente, jogador)  # Chamada da função "batalha" do módulo "Batalha"

            if "runa" not in meus_objetos_coletados:
                while w < 1:
                    print("\n\u001b[37;1mVocê encontrou uma runa! Deseja coletá-la?\n (1) sim\n (2) não")
                    coleta_de_objetos = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{coleta_de_objetos}\u001b[0m\n")
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

            print("\nFinalmente você vê as dunas do deserto, não muito distantes...")
            print("\nVocê segue até lá...")
            bt.enter()
            bt.delete_last_lines(1)
            
            print(dunas(jogador, meus_objetos_coletados)) # Chamada da função 'dunas' quando o jogador chega às dunas do deserto
            
            print("\nVocê está prosseguindo sua caminhada...")
            bt.delete_last_lines(1)
            print("\nSó resta um local para explorar agora...")
            print(
                "\nVocê segue por uma longa estrada. A temperatura está bastante elevada, fazendo com que o caminho pareça ainda mais longo")

            if "chave" not in meus_objetos_coletados:
                while x < 1:
                    print("\n\u001b[37;1mVocê encontrou uma chave! Deseja coletá-la?\n (1) sim\n (2) não")
                    coleta_de_objetos = input(">>>")
                    bt.delete_last_lines(1)
                    print(f">>>{coleta_de_objetos}\u001b[0m\n")
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
            print(
                "\nQuando você finalmente chega à montanha, percebe que o caminho para subi-la será longo e sinuoso...")
            print(
                "\nMesmo assim, você não pode desistir. Você começa a subir a montanha, percebendo um caminho muito íngreme.")
            bt.enter()
            print("\nApós a difícil caminhada, você finalmente chega ao topo da montanha...")
            bt.enter()
            bt.delete_last_lines(1)
            
            print(topo_da_montanha(meus_objetos_coletados))

            if "poção brilhante" not in meus_objetos_coletados:
                print("\nVocê não conseguiu acesso ao oásis para cumprir sua missão nesta etapa...")
                bt.enter()
                print("\nPor isso, você tem mais duas chances para retornar aos locais anteriores e tentar cumprir sua missão!")
                bt.enter()
                print("\nPrimeiramente siga às dunas...")
                bt.enter()
                print(retornar("Dunas", jogador, meus_objetos_coletados)) # Chamada da função 'retornar' para que o jogador volte às dunas do deserto e colete os objetos que faltam  

                if "poção brilhante" not in meus_objetos_coletados:
                    print("\nHmm... parece que você não conseguiu de novo. Aproveite sua última chance agora!")
                    bt.enter()
                    print("Você tem uma chance de explorar o topo da montanha novamente... você segue até lá.")
                    bt.enter()
                    print("O caminho da subida é cansativo, mas você finalmente chega ao destino...")
                    print(retornar("Topo da montanha", jogador, meus_objetos_coletados)) # Chamada da função 'retornar' para que o jogador volte ao topo da montanha e colete os objetos que faltam
                    if "poção brilhante" not in meus_objetos_coletados:
                        print("\nSuas chances acabaram... você não pode mais explorar nenhum local no deserto.")
                        return (f'\nVocê não cumpriu esta etapa, mas está livre para continuar sua jornada.')
                    else:
                        return (f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')
                else:
                    return (f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')
            else:
                return (f'\nVocê cumpriu a missão! Está pronto(a) para continuar sua jornada.')

