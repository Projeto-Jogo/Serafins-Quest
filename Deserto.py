# MÓDULO "DESERTO"

import Batalha as bt # Importa o módulo "Batalha"

def dunas(objetos_coletados): 
# Função utilizada para a trajetória do jogador nas dunas de areia do deserto 
    a = b = c = d = e = 0 # Variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    if "pedra" in objetos_coletados and "poção" in objetos_coletados: # Se o jogador já coletou a pedra e a poção, aparece um aviso de que não há mais objetos para coletar no local
        return(f'Você ja coletou os objetos que necessitava aqui!') 
    elif "pedra" in objetos_coletados and "poção" not in objetos_coletados: # Se o jogador já coletou a pedra, encontra apenas uma poção
        while a < 1:
            escolha_1 = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não")) # O jogador escolhe se quer coletar a poção ou não
            if escolha_1 == 1:
                a += 1
                objetos_coletados.append("poção")
                print("Poção coletada!")
                return(f'Seu novo item é poção')
                while b < 1:
                    escolha_2 = int(input("Beber poção? 1 - Sim / 2 - Não"))
                    if escolha_2 == 1:
                        b += 1
                        hp -= 1
                        print(f'Ah, não! Esta poção é perigosa! Você perdeu 1 HP!')
                        #if hp <= 0:
                         #   bt.game_over()
                    elif escolha_2 == 2:
                        b += 1
                        print("OK!")
                    else:
                        print("Escolha uma opção válida!")
            elif escolha_1 == 2:
                a += 1
                print("OK!")
                return(f'Você não coletou nenhum novo item!')
            else:
                print("Comando não conhecido, tente novamente.")
    elif "poção" in objetos_coletados and "pedra" not in objetos_coletados:
        while c < 1:
            c += 1
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("pedra")
                print("Pedra coletada!")
                return(f'Seu novo item é pedra!')
            elif escolha == 2:
                c += 1
                print("OK!")
                return(f'Você não coletou nenhum novo item!')
            else:
                print("Comando não conhecido, tente novamente.")
    else:
        while d < 1:
            escolha = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                d += 1
                objetos_coletados.append("poção")
                print("Poção coletada!")
            elif escolha == 2:
                d += 1
                print("OK!")
            else:
                print("Comando não conhecido, tente novamente.")
        print("ADICIONAR DESCRIÇÃO DE UM CAMINHO")
        enter()
        while e < 1:
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                e += 1
                objetos_coletados.append("pedra")
                print("Pedra coletada!")
            elif escolha == 2:
                e += 1
                print("OK!")
            else:
                print("Escolha uma opção válida!")
        if "poção" in objetos_coletados and "pedra" in objetos_coletados:
            return(f'Seus novos itens são poção e pedra!')
        elif "poção" in objetos_coletados and "pedra" not in objetos_coletados:
            return(f'Seu novo item é poção!')
        elif "pedra" in objetos_coletados and "poção" not in objetos_coletados:
            return(f'Seu novo item é pedra!')
        else:
            return(f'Você não coletou novos itens!')

def topo_da_montanha(objetos_coletados): 
# Funçao autilizada para a trajetória do jogador no topo de uma montanha no deserto
    a = 0
    if "flor" in objetos_coletados:
        print("Você ja coletou o objeto que necessitava aqui!")
    else:
        while a < 1:
            escolha = int(input("Você encontrou uma flor do deserto! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("flor")
                a += 1
                return(f'Seu novo item é uma flor do deserto!')
            elif escolha == 2:
                a += 1
                print("OK!")
                return(f'Você não coletou novos itens!')
            else:
                print("Comando não conhecido, tente novamente.")
		
def oasis(objetos_coletados, atributos): 
# Função utilizada para a trajetória do jogador em um oasis no deserto
    hp = atributos[5]
    a = b = c = d = e = 0 # 
    i = -1
    desbloqueio = False
    missao_cumprida = False
    combinacao_correta = ["poção", "flor", "runa", "pedra"]
    print("Apresente uma sequência de 4 objetos como código para desbloquear a passagem ao oasis!")
    objeto_1 = input("Qual é o primeiro objeto da sequência?")
    if objeto_1 not in objetos_coletados:
        return(f"Você não possui o objeto {objeto_1}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!")
    else:
        objeto_2 = input("Qual é o segundo objeto da sequência?")
        if objeto_2 not in objetos_coletados:
            return(f'Você não possui o objeto {objeto_2}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')
        else:
            objeto_3 = input("Qual é o terceiro objeto da sequência?")
            if objeto_3 not in objetos_coletados:
                return(f'Você não possui o objeto {objeto_3}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')
            else:
                objeto_4 = input("Qual é o quarto objeto da sequência?")
                if objeto_4 not in objetos_coletados:
                    return(f'Você não possui o objeto {objeto_4}! Continue sua caminhada pelo deserto e colete mais objetos. Em seguida, volte e tente conseguir a passagem ao oasis novamente!')
                else:
                    if(objeto_1 == combinacao_correta[0] and objeto_2 == combinacao_correta[1] and objeto_3 == combinacao_correta[2] and objeto_4 == combinacao_correta[3]):
                        desbloqueio = True
                        while i < len(atributos) - 1:
                            i += 1
                            if atributos[i] < 5:
                                atributos[i] += 1
                        print(f'Parabéns! Você desbloqueou o acesso ao oasis e seus atributos melhoraram! Força: {atributos[0]} - destreza: {atributos[1]} - intelig ência: {atributos[2]} - sorte: {atributos[3]} - carisma:  {atributos[4]}.')
                        print("ADICIONAR DESCRIÇÃO DO OASIS")
                        while a < 1:
                            escolha_1 = int(input("Qual local do oasis gostaria de explorar primeiro? 1 - Coqueiros / 2 - Lago "))
                            if escolha_1 == 1:
                                a += 1
                                print("ADICIONAR DESCRIÇÃO DOS COQUEIROS")
                                while b < 1:
                                    escolha_2 = int(input("Há uma (...) embaixo daquele coqueiro, há alguns metros! Deseja coletá-la? 1 - Sim / 2 - Não "))
                                    if escolha_2 == 1:
                                        b += 1
                                        # acontece alguma coisa
                                    elif escolha_2 == 2:                                   
                                        b += 1
                                        print("OK!")
                                    else:
                                        print("Escolha uma opção válida!")
                                print("Siga para o lago agora...")
                                enter()
                                print("Você mergulhou no lago!")
                                enter()
                                print("ADICIONAR DESCRIÇÃO DO LAGO")
                                print("Parece que há algo lá no fundo, há alguns metros...")
                                print("Nadando e chegando mais perto, você vê que é um báu!")
                                while c < 1:
                                    if escolha_3 == 1:
                                        c += 1
                                        print("Você coletou o baú!")
                                        print("Saia do lago agora e veja o que há dentro dele...")
                                        enter()
                                        if "chave" in objetos_coletados:
                                            while d < 1:
                                                abertura_do_bau = input("Você possui a chave! Digite 1 para utilizá-la: ")
                                                if abertura_do_bau == 1:
                                                    d += 1
                                                    print("Você conseguiu abrir o baú!")
                                                    i = 0
                                                    while i < len(atributos) - 1:
                                                        i += 1
                                                        if atributos[i] < 5:
                                                            atributos[i] += 1
                                                    hp += 2
                                                    print("Por conta disso, seus atributos aumetaram e você ganhou 2 HPs!")
                                                    print(f'força: atributos[0], destreza: atributos[1], inteligência: atributos[2], carisma: atributos[3], sorte: atributos[4]')
                                                    print("Também há uma nota dentro do baú... leia!")
                                                    enter()
                                                    print("Na nota está escrito 'URSO'..")
                                                    print("Hmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
                                                    missao_cumprida = True
                                                else:
                                                    print("Abra o baú!")
                                    else:
                                        print("Oops! Você ainda não tem a chave para abrir o baú! Continue sua exploração pelo deserto e colete-a!")                                                  
                            elif escolha_1 == 2:
                                a += 1
                                print("Você mergulhou no lago!")
                                enter()
                                print("ADICIONAR DESCRIÇÃO DO LAGO")
                                print("Parece que há algo lá no fundo, há alguns metros...")
                                print("Nadando e chegando mais perto, você vê que é um bau!")
                                while c < 1:
                                    escolha_3 = int(input("Deseja coletar o bau? 1 - Sim / 2 - Não"))
                                    if escolha_3 == 1:
                                        c += 1
                                        print("Você pegou o bau!")
                                        print("Agora saia do lago e veja o que há dentro dele...")
                                        enter()
                                        if "chave" in objetos_coletados:
                                            while d < 1:
                                                abertura_do_bau = int(input("Você possui a chave! Digite 1 para utilizá-la: "))
                                                if abertura_do_bau == 1:
                                                    d += 1
                                                    print("Você conseguiu abrir o baú!")
                                                    i = 0
                                                    while i < len(atributos) - 1:
                                                        i += 1
                                                        if atributos[i] < 5:
                                                            atributos[i] += 1
                                                    hp += 2
                                                    print("Por conta disso, seus atributos aumetaram e você ganhou 2 HPs!")
                                                    print(f'força: atributos[0], destreza: atributos[1], inteligência: atributos[2], carisma: atributos[3], sorte: atributos[4]')
                                                    print(f'HPs: atributos[5]')
                                                    print("Há uma nota lá dentro também... leia!")
                                                    enter()
                                                    print("Na nota está escrito: 'URSO'")
                                                    print("Hmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
                                                    missao_cumprida = True
						    return(f'Parabéns! Você cumpriu sua missão, melhorando seus atributos, ganhando HPs e obtendo uma dica para seguir em sua jornada!')
                                        else:
                                            print(f'Oops! Você ainda não tem a chave para abrir o baú! Continue sua exploração pelo deserto e colete-a!')
                                    else:
                                        print("Você saiu do lago. Parece que não há mais nada para fazer por aqui...")
                                        c += 1
    if desbloqueio == False:
        return(f'Combinação incorreta! Você não conseguiu acesso ao oasis! Tente novamente!')
    if missao_cumprida == False:
        return(f'Você não conseguiu cumprir sua missão no deserto! Continue sua exploração e tente novamente...')
    
def retornar(local, objetos_coletados, *atributos): 
# Funçao utilizada para que o jogador possa retornar a lugares por quais já passou anteriormente
if local == "Dunas":
    print("Bem vindo(a) de volta ao oasis!")
    return dunas(objetos_coletados)
elif local == "Topo da montanha":
    print("Bem vindo(a) de volta ao topo da montanha!")
    return topo_da_montanha(objetos_coletados)
elif local == "Oasis":
    print("Bem vindo(a) de volta ao oasis!")
    return oasis(objetos_coletados, atributos)

def Deserto(jogador):	
# Função principal do módulo, que chama as demais funções e define a trajetória do jogador pelo deserto						
    x = y = z = 0 # x, y e z são variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não informe uma escolha válida
    meus_objetos_coletados = [] # Lista para incluir os objetos que o jogador coleta ao logo da trajetória no deserto
    forca = jogador['forca']
    destreza = jogador['destreza']
    inteligencia = jogador['inteligência']
    sorte = jogador['sorte']
    carisma = jogador['carisma']
    meus_atributos = [forca, destreza, inteligencia, sorte, carisma]  # Atributos do jogador: força, destreza, inteligência, sorte e carisma, respectivamente 
    hp = jogador['hp'] 
    Serpente = bt.Serpente					  
# Introdução do ambiente (deserto) ao jogador
    print("Você chegou ao deserto!")
    print("ADICIONAR DESCRIÇÃO INTRODUTÓRIA DO DESERTO")
    bt.enter()
# O jogador escolhe para qual local deseja ir primeiro (dunas de areia, topo da montanha ou oasis)
    escolha_1 = int(input("Qual local deseja explorar primeiro? 1 - Dunas de areia / 2 - Topo da montanha / 3 - Oasis"))
# Se a escolha for dunas de areia:
    if escolha_1 == 1:
# CAMINHO 1
# O jogador escolhe seguir para as dunas de areia primeiro:
        print("Você está nas dunas!")
        print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA") # Descrição do ambiente ao jogador
        bt.enter()
        dunas(meus_objetos_coletados) # Chama função dunas()
        print("Você está prosseguindo sua caminhada...")
        escolha_2 == int(input("Qual é o seu próximo destino? 1 - Topo da montanha / 2 - Oasis")) # O jogador escolhe para onde ir em seguida
        if escolha_2 == 1:
# O jogador escolhe seguir das dunas para o topo da montanha:    
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
            if coleta_de_objetos == 1: # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
                bt.batalha(Serpente, jogador)#  chamada da função "batalha" do módulo "Batalha"
            else:
                bt.enter()
            if "chave" not in meus_objetos_coletados: # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
                coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
                if coleta_de_objetos == 1:  # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
                    meus_objetos_coletados.append("chave") # Se não, o jogador continua o caminho pelo deserto
                else:
                    bt.enter()
            else:
                bt.enter()
	    print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
            print("Você está chegando ao topo da montanha...")
            enter()
            print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
            topo_da_montanha(meus_objetos_coletados)
            print("Você está prosseguindo sua caminhada...")
            bt.enter()
            print("Só resta um local para explorar agora...")
# Finalmente, o jogador segue do topo da montanha a um oasis
	    print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA ATÉ O ENCONTRO DE UM OASIS NO DESERTO")		
            print("Há um oasis a alguns metros!")
            if "runa" not in meus_objetos_coletados:
                coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("runa")
                else:
                    bt.enter()
            else:
                bt.enter()
            oasis(meus_objetos_coletados, meus_atributos)   
	    missao = oasis(meus_objetos_coletados, meus_atributos) 
	    if missao != " ":
	        while x < 0:
	            escolha_1 = int(input("1 - Retornar a algum dos locais que já explorou / 2 - Seguir no caminho?")
	                if escolha_1 == 1:
	                    x += 1
	                    while y < 0:
	                        escolha_2 = int(input("Para qual local quer retornar? 1 - Dunas de areia / 2 - Topo da montanha / 3 - Oasis")
			            if escolha_2 == 1:
	                                retornar("Dunas", meus_objetos_coletados)
				        y += 1
			            elif escolha_2 == 2:
			                retornar("Topo da montanha")
				        y += 1
			            elif escolha_2 == 3:
		                        retornar("Oasis" meus_objetos_coletados, atributos)
				        y += 1
			            else:
			                print("Comando não reconhecido, tente novamente.")
            elif escolha_2 == 2:
# CAMINHO 2
# O jogador escolhe seguir das dunas de areia ao oasis:
            # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
                coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
            # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
                if coleta_de_objetos == 1:
                    bt.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
                else:
                    enter()
                print("Você chegou a um oasis!")
                oasis(meus_objetos_coletados, meus_atributos)
                print("Você está prosseguindo sua caminhada...")
                enter()
                print("Só resta um local para explorar agora...")
# Finalmente, o jogador segue do oasis ao topo da montanha
            # Descrição do caminho
                print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E O TOPO DA MONTANHA")
                if "runa" not in meus_objetos_coletados:
                coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                    if coleta_de_objetos == 1:
                        meus_objetos_coletados.append("runa")
                    else:
                        bt.enter()
                else:
                    bt.enter()
            
                print("Você chegou ao topo da montanha!")
                print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
                topo_da_montanha(meus_objetos_coletados)
                print("Você está prosseguindo sua caminhada...")
                bt.enter()
    elif escolha_1 == 2:	    
# CAMINHO 3:
# O jogador escolhe seguir para o topo da montanha primeiro	    
        print("Você está no topo da montanha!")
        print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
        bt.enter()
    #chama função topo_da_montanha()
        topo_da_montanha(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        escolha_2 == int(input("Qual é o seu próximo destino? 1 - Dunas / 2 - Oasis"))
        if escolha_2 == 1:
# O jogador segue do topo da montanha às dunas
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E AS DUNAS DE AREIA")
        # Descrição do caminho
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E AS DUNAS")
         # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
            if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
                coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
                else:
                    bt.enter()
            else:
                bt.enter()
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            bt.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
        else:
            bt.enter()
            print("Você chegou às dunas!")
	    print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
            enter()
    	#chama função "dunas"
	    dunas(meus_objetos_coletados)
	    print("Você está prosseguindo sua caminhada...")
	    print("Só resta um local para explorar agora...")
	    bt.enter()
# Finalmente, o jogador segue das dunas de areia ao oasis
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            if coleta_de_objetos == 1:
                bt.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
            else:
                bt.enter()
            print("Há um oasis a alguns metros!")
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS DE AREIA E O OASIS")
            oasis(meus_objetos_coletados, meus_atributos)
            elif escolha_2 == 2:
# CAMINHO 4
# O jogador segue do topo da montanha ao oasis
                print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E O OASIS")
                print("Há um oasis a alguns metros!")
                if "runa" not in meus_objetos_coletados:
                    coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                    if coleta_de_objetos == 1:
                        meus_objetos_coletados.append("runa")
                     else:
                        bt.enter()
                else:
                    bt.enter()
                print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA ATÉ O ENCONTRO DE UM OASIS NO DESERTO")
                oasis(meus_objetos_coletados, meus_atributos)     
                print("Você está prosseguindo sua caminhada...")
                bt.enter()
# Finalmente, o jogador segue do oasis às dunas de areia
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            if coleta_de_objetos == 1:
                bt.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
            else:
                bt.enter()
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS DE AREIA")
            if "runa" not in meus_objetos_coletados:
                coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("runa")
                else:
                    bt.enter()
            else:
                bt.enter()
                print("Você chegou às dunas de areia!")
                dunas(meus_objetos_coletados, meus_atributos)  
                print("Você está prosseguindo sua caminhada...")
            bt.enter()
    if escolha_1 == 3:
# CAMINHO 5: 
# O jogador escolhe seguir ao oasis primeiro 
        print("Você chegou a um oasis!")
        bt.enter()
    # chama função "oasis"
        oasis(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        escolha_2 == int(input("Qual é o seu próximo destino? 1 - Dunas / 2 - Topo da montanha ")
            if escolha_2 == 1:
# O jogador segue do oasis às dunas de areia
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS DE AREIA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            if coleta_de_objetos == 1:
                bt.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
            else:
                bt.enter()
            print("Você chegou às dunas de areia!")
            dunas(meus_objetos_coletados)  
            print("Você está prosseguindo sua caminhada...")
            print("Só resta um local para explorar agora...")
            bt.enter()
# Finalmente, o jogador segue das dunas de areia ao topo da montanha
        # Descrição do caminho entre as dunas de areia ao topo da montanha
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            if coleta_de_objetos == 1:
                Batalha.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
            else:
                bt.enter()
        # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
            if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
                coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
                else:
                    bt.enter()
            else:
                bt.enter()
            print("Você está chegando ao topo da montanha...")
            bt.enter()
            print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
            topo_da_montanha(meus_objetos_coletados)
            print("Você está prosseguindo sua caminhada...")
            bt.enter()
        elif escolha_2 == 2:
# CAMINHO 6:
# O jogador segue do oasis ao topo da montanha
            if "runa" not in meus_objetos_coletados:
                coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("runa")
                else:
                    bt.enter()
            else:
                bt.enter()
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E O TOPO DA MONTANHA")
            print("Você chegou ao topo da montanha!")
            enter()
            print("Descrição de ambiente - Topo da montanha")
            topo_da_montanha(meus_objetos_coletados)
            print("Você está prosseguindo sua caminhada...")
            print("Só resta um local para explorar agora...")
            bt.enter()
# O jogador segue do topo da montanha às dunas de areia
         # Descrição do caminho entre o topo da montanha e as dunas de areia
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            if coleta_de_objetos == 1:
                bt.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
            else:
                bt.enter()
        # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
            if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
                coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
                else:
                    bt.enter()
            else:
                bt.enter()
            print("Você está chegando às dunas de areia...")
            enter()
            print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
            dunas(meus_objetos_coletados)
            print("Você está prosseguindo sua caminhada...")
            bt.enter()	    
    missao_cumprida = oasis(meus_objetos_coletados, meus_atributos)
    while z < 1:
        if missao_cumprida == "Parabéns! Você cumpriu sua missão, aumentando seus atributos, ganhando HPs e obtendo uma dica para continuar!":
            print("Você está pronto para seguir em sua jornada...")
            z += 1
        else:
            print("Você ainda não completou essa etapa!")
    #return
