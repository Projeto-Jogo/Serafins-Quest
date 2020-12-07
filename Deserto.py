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
                        hp -= 10
                        print(f'Ah, não! Esta poção é perigosa! Você perdeu 10 HPs!')
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
                        #coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim / 2 - Não"))
                        #if coleta_de_objetos == 1:
                         #   a += 1
                          #  bt.batalha(Serpente, jogador)
                        #else:
                         #   bt.enter()   
                        print("Siga para o lago agora...")
                        enter()
                        print("Você mergulhou no lago!")
                        enter()
                        print("ADICIONAR DESCRIÇÃO DO LAGO")
                        print("Parece que há algo lá no fundo, há alguns metros...")
                        print("Nadando e chegando mais perto, você vê que é um báu!")
                        while c < 1:
                            escolha_1 = int(input("O que desejaa fazer? 1 - Coletar o baú / 2 - Sair do lago "))
                            if escolha_1 == 1:
                                c += 1
                                print("Você coletou o baú!")
                                print("Saia do lago agora e veja o que há dentro dele...")
                                enter()
                                if "chave" in objetos_coletados:
                                    while d < 1:
                                        abertura_do_bau = int(input("Você possui a chave! Digite 1 para utilizá-la: "))
                                        if abertura_do_bau == 1:
                                            d += 1
                                            print("Você conseguiu abrir o baú!")
                                            i = 0
					    while d < 1:
					        aumento_de_atributos = int(input("Você pode ter aumento em um dos seus atributos! Qual você escolhe? 1 - Força / 2 - Destreza / 3 - Inteligência / 4 - Sorte / 5 - Carisma "))
                                                if aumento_de_atributos == 1:
						    d += 1
						    atributos[0] += 1
						    print(f'Voce tem atributos[0] de forca agora!')
					        elif aumento_de_atributos == 2:
						    d += 1
						    atributos[1] += 1
						    print(f'Voce tem atributos[1] de forca agora!')
					        eli f aumento_de_atributos == 3:
					            d += 1
						    atributos[2] += 1
						    print(f'Voce tem atributos[0] de forca agora!')
					        elif aumento_de_atributos == 4:
						    d += 1
						    atributos[3] += 1
						    print(f'Voce tem atributos[0] de forca agora!')
                                                elif aumento_de_atributos == 5:
						    d += 1
						    atributos[4] += 1
					            print(f'Voce tem atributos[0] de forca agora!')
					        else:
						    print("Comando não reconhecido, tente novamente")
                                            hp += 20
                                            print("Você também ganhou 20 HPs!")
                                            print(f'força: atributos[0], destreza: {atributos[1]}, inteligência: {atributos[2]}, carisma: {atributos[3]}, sorte: {atributos[5]}')
                                            print("Também há uma nota dentro do baú... leia!")
                                            bt.enter()
                                            print("Na nota está escrito 'URSO'..")
                                            print("Hmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
                                            missao_cumprida = True
                                        else:
                                            print("Abra o baú!")
                                else:
                                    print("Oops! Você ainda não tem a chave para abrir o baú! Continue sua exploração pelo deserto e colete-a!")                                                  
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

def retornar():
	pass

def Deserto(jogador):
	
	# Função principal utilizada para descrever toda a trajetória do jogador no deserto
	x = y = z = w = 0
	meus_objetos_coletados = []
	forca = jogador["forca"]
	destreza = jogador["destreza]
	inteligencia = jogador["inteligência"]
	sorte = jogador["sorte"]
	carisma = jogador["carisma"]
	hp = jogador["hp"]
	arma = jogador["arma"]
	print("Você está no deserto!")
	print("ADICIONAR DESCRIÇÃO INTRODUTÓRIA DO DESERTO")
	enter()
	escolha_1 = int(input("Qual caminho deseja seguir? 1 - Caminho 1 / 2 - Caminho 2 / 3 - Caminho 3"))
	if escolha_1 == 1:
        # CAMINHO 1: TOPO DA MONTANHA - OASIS - DUNAS
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ O TOPO DA MONTANHA")
            print("Você está no topo da montanha!")
            bt.enter()
	    topo_da_montanha(meus_objetos_coletados)
	    print("Você está prosseguindo sua caminhada...")
	    print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E O OASIS")
	    print("O oasis está a alguns metros... siga até lá!")
	    bt.enter()
	    if "runa" not in meus_objetos_coletados:
                coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("runa")
                else:
                    print("OK!")
            bt.enter()
            print("Há um oasis há alguns metros... siga até lá!")
            oasis(meus_objetos_coletados, atributos)
            print("Você está prosseguindo sua caminhada...")
            retornar()
            print("Só resta um local para explorar agora...")
            bt.nter()
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS")
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
            if coleta_de_objetos == 1:
                    bt.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
                else:
                    bt.enter()
            print("Você chegou às dunas de areia...")
            dunas(objetos_coletados)
            retornar()
			
	elif escolha_1 == 2:
        # CAMINHO 2: DUNAS - TOPO DA MONTANHA - OASIS
		print("Você está nas dunas!")
		print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
		bt.enter()
		dunas(meus_objetos_coletados)
		print("Você está prosseguindo sua caminhada...")
		print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
		if "chave" not in meus_objetos_coletados:
                    coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
                    if coleta_de_objetos == 1:
                        meus_objetos_coletados.append("chave")
			print("Chave coletada!")
		    else:
			bt.enter()
		else:
		    print("Você chegou ao topo da montanha...")
		    bt.nter()
		    print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
		    topo_da_montanha(meus_objetos_coletados)
		    print("Você está prosseguindo sua caminhada...")
		    print("Só resta um local para explorar agora...")
		    print("Um oasis está há alguns metros, siga até lá!")
		    bt.enter()
		    if "runa" not in meus_objetos_coletados:
			coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
			if coleta_de_objetos == 1:
			    meus_objetos_coletados.append("runa")
			else:
			    bt.enter()
		retornar()
	    elif escolha_1 == 3:
            # CAMINHO 3: OASIS - DUNAS - TOPO DA MONTANHA
                print("Você está no oasis!")
                oasis(objetos_coletados, atributos)
                print("Você está prosseguindo sua caminhada...")
                bt.enter()
                print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS DE AREIA")
                coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
              # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
                  # if coleta_de_objetos == 1:
                   #    bt.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
                   #else:
                 #      bt.enter()
                print("ADICIONAR MAIS DESCRIÇÃO")
                if "runa" not in meus_objetos_coletados:
                    coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                    if coleta_de_objetos == 1:
                        meus_objetos_coletados.append("runa")
                    else:
                        print("OK!")
                bt.enter()
                coleta_de_objetos = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim / 2 - Não"))
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("runa")
                elif coleta_de_dados == 2:
                    print("OK!")
                bt.enter()
                print("Você chegou às dunas de areia!")
                dunas(meus_objetos_coletados, meus_atributos)  
                retornar()
