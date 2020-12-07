# MÓDULO "DESERTO"

import Batalha as bt # Importa o módulo "Batalha"


def dunas(objetos_coletados): 
	
# Função utilizada para a trajetória do jogador nas dunas de areia do deserto 

    print("ADICIONAR DESCRIÇÃO DAS DUNAS DO DESERTO")
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
                        print(f'Ah, não! Esta poção é perigosa! Você perdeu 10 HPs!')
                        # ADICIONAR FUNÇÃO PARA PASSAR DE NÍVEL
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
		while b < 1:
                    escolha_2 = int(input("Beber poção? 1 - Sim / 2 - Não"))
                    if escolha_2 == 1:
                        b += 1
                        # ADICIONAR FUNÇÃO PARA PASSAR DE NÍVEL
                    elif escolha_2 == 2:
                        b += 1
                        print("OK!")
                    else:
                        print("Escolha uma opção válida!")
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
                        print("Há uma serpente no caminho!")
                        print(bt.batalha(Serpente, jogador))
                        print("Siga para o lago agora...")
                        bt.enter()
                        print("Você mergulhou no lago!")
                        bt.enter()
                        print("ADICIONAR DESCRIÇÃO DO LAGO")
                        print("Parece que há algo lá no fundo, há alguns metros...")
                        print("Nadando e chegando mais perto, você vê que é um báu!")
                        while c < 1:
                            escolha_1 = int(input("O que deseja fazer? 1 - Coletar o baú / 2 - Sair do lago "))
                            if escolha_1 == 1:
                                c += 1
                                print("Você coletou o baú!")
                                print("Saia do lago agora e veja o que há dentro dele...")
                                bt.enter()
                                if "chave" in objetos_coletados:
                                    while d < 1:
                                        abertura_do_bau = int(input("Você possui a chave! Digite 1 para utilizá-la: "))
                                        if abertura_do_bau == 1:
                                            d += 1
                                            print("Você conseguiu abrir o baú!")
                                            i = 0
					    while d < 1:
					        aumento_de_atributos = int(input("Você pode ter aumento em um dos seus atributos! Qual atributo você escolhe? 1 - Força / 2 - Destreza / 3 - Inteligência / 4 - Sorte / 5 - Carisma "))
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
                                            #ADICIONAR FUNÇÃO PARA PASSAR DE NÍVEL
					    while e < 1:
						melhora_atributo = int(input("Você conseguiu uma melhora de atributo! Escolha um dos atributos para ganhar 1 ponto: 1 - força / 2 - destreza / 3 - inteligência / 4 - sorte / 5 - carisma "))
						if melhora_atributo == 1:
							e += 1
							atributos[0] += 1
							print(f'Sua força aumentou! Força: atributos[0]')
						elif melhora_atributo == 2:
							e += 1
							atributos[1] += 1
							print(f'Sua destreza aumentou! Destreza: atributos[1]')
						elif melhora_atributo == 3:
							e += 1
							atributos[2] += 1
							print(f'Sua inteligência aumentou! Inteligência: atributos[2]')
						elif melhora_atributo == 4:
							e += 1
							atributos[3] += 1
							print(f'Sua sorte aumentou! Sorte: atributos[3]')
						elif melhora_atributo == 5:
							e += 1
							atributos[4] += 1
							print(f'Seu carisma aumentou! Carisma: atributos[4]')
					        
                                            print("Também há uma nota dentro do baú... leia!")
                                            bt.enter()
                                            print("Na nota está escrito 'URSO'..")
                                            print("Hmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
					    bt.enter()
					    while f < 1:
					    	carregar_arma = int(input("Você encontrou um chicote no caminho! Digite 1 para obtê-lo como arma!))
						if carregar_arma == 1:
							f += 1
							arma = "chicote"
						else:
							print("Comando não conhecido, tente novamente.")
									  
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

def retornar(local, objetos_coletados, atributos):
	
	if local == "Topo da montanha":
	    print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ O TOPO DA MONTANHA")
	    print("Você voltou ao topo da montanha!")
	    print(topo_da_montanha(objetos_coletados))
	    print("Siga às dunas agora...")
	    bt.enter()
	    print(dunas(objetos_coletados))
	    print("Agora só resta explorar o oasis novamente...")
	    resultado = oasis(objetos_coletados, atributos)
	    print(resultado)							  
	    if resultado == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
	        return retornar("Topo da montanha", objetos_coletados, atributos)
	    else:
		return(f'Dessa vez você conseguiu!')
	    
        elif local == "Dunas:
	    print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ AS DUNAS")
	    print("Você voltou às dunas")
	    print(dunas(objetos_coletados))
	    print("Siga ao topo da montanha agora...")
	    bt.enter()
	    print(topo_da_montanha(objetos_coletados))
	    print("Agora só resta explorar o oasis novamente...")
	    resultado = oasis(objetos_coletados, atributos)
	    print(resultado)							  
	    if resultado == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
	        return retornar("Dunas", objetos_coletados, atributos)
	    else:
		return(f'Dessa vez você conseguiu!')

def Deserto(jogador):

	# Função principal que chama as demais funções (dunas(), topo_da_montanha() e oasis()), descrevendo toda a trajetória do jogador pela etapa do deserto.
	#
	#
	
	s = t = u = v = w = x = y = z = 0 # Variáveis de controle para o mecanismo de repetição (caso o jogador tenha digitado um comando inválido)
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
	print("ADICIONAR DESCRIÇÃO INTRODUTÓRIA DO DESERTO")
	print(bt.enter())
	
	while s < 1:
		escolha_1 = int(input("Escolha um dos caminhos para seguir: 1 - Caminho 1 / 2 - Caminho 2 / 3 - Caminho 3"))
		if escolha_1 == 1:
			# CAMINHO 1: TOPO DA MONTANHA - OASIS - DUNAS
			s += 1
			print("ADICIONAR DESCRIÇÃO DO CAMINHO ATÉ O TOPO DA MONTANHA")
			print("Você está no topo da montanha!")
			print(bt.enter())
			print(topo_da_montanha(meus_objetos_coletados))
			print("Você está prosseguindo sua caminhada...")
			print(bt.enter())
			if "runa" not in meus_objetos_coletados:
				while t < 1:
					coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
					if coleta_de_objetos == 1:
						t += 1
						meus_objetos_coletados.append("runa")
						print("Runa coletada!")
						print("Seu novo item é runa!")
					elif coleta_de_objetos == 2:
						t += 1
						print("OK!")
					else:
						print("Comando não conhecido, tente novamente.")
			print(bt.enter())
			print("O oasis está a alguns metros... siga até lá!")
			print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E O OASIS")
			print("Você chegou ao oásis...")
			print(oasis(meus_objetos_coletados, meus_atributos))
			print("Só resta um local para explorar agora...")
			print(bt.enter())
			print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS")
		        print("Você encontrou uma serpente no caminho!")
			bt.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
			print(bt.enter())
			print("Você chegou às dunas de areia...")
			print(dunas(meus_objetos_coletados))
			resultado_etapa = oasis(meus_objetos_coletados, meus_atributos)
	                if resultado_etapa == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
			    i = 0
		            j = 0
			    print("Você tem duas chances para retornar aos locais anteriores e tentar cumprir esta etapa!")
			    while i < 2:
			        retorno = int(input("Para onde deseja retornar? 1 - Dunas / 2 - Topo da montanha "))
				while j < 1:	
				    if retorno == 1:
					j += 1
				        resultado_etapa = retornar("Dunas")
					print(resultado_etapa)
				    if retorno == 2:
					j += 1
					resultado_etapa = retornar("Topo da montanha")
					print(resultado_etapa)
				i += 1
			    if resultado_etapa == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
			        return(f'Você não conseguiu cumprir sua missão nesta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você d           ecide parar e descansar por uma noite...')
			    else:
				return(f'Parabéns! Você conseguiu cumprir esta etapa e está pronto(a) para continuar sua jornada! Você conta agora com atributo_melhorado = , hp = e obteve uma nova arma! Antes de prosseguir, você decide parar e descansar por uma noite...')
			else:
			    return(f'Parabéns! Você conseguiu cumprir esta etapa e está pronto(a) para continuar sua jornada! Você conta agora com atributo_melhorado = , hp = e obteve uma nova arma! Antes de prosseguir, você decide parar e descansar por uma noite...')
						  
  		elif escolha_1 == 2:
			# CAMINHO 2: DUNAS - TOPO DA MONTANHA - OASIS
			s += 1
			print("Você está nas dunas do deserto...")
			print("ADICIONAR DESCRIÇÃO DAS DUNAS")
			print(bt.enter())
			print(dunas(meus_objetos_coletados))
			print("Você está prosseguindo sua caminhada...")
			print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
									  
			if "chave" not in meus_objetos_coletados:
				while v < 1:
					coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
					if coleta_de_objetos == 1:
						v += 1
						meus_objetos_coletados.append("chave")
						print("Chave coletada!")
						print("Seu novo item é chave!")
					elif coleta_de_objetos == 2:
						v += 1
						print("OK!")
									  
			print(bt.enter())
			print("Você chegou ao topo da montanha...")
			print(topo_da_montanha(meus_objetos_coletados))
			print("Só resta um local para explorar agora...")
			print("Um oasis está há alguns metros... siga até lá!")
			print(bt.enter())
									  
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
			print(bt.enter())
			print("Você chegou ao oásis...")
			print(oasis(meus_objetos_coletados, meus_atributos))
			resultado_etapa = oasis(meus_objetos_coletados, meus_atributos)
	                if resultado_etapa == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
			    i = 0
		            j = 0
			    print("Você tem duas chances para retornar aos locais anteriores e tentar cumprir esta etapa!")
			    while i < 2:
			        retorno = int(input("Para onde deseja retornar? 1 - Dunas / 2 - Topo da montanha "))
				while j < 1:	
				    if retorno == 1:
					j += 1
				        resultado_etapa = retornar("Dunas")
					print(resultado_etapa)
				    if retorno == 2:
					j += 1
					resultado_etapa = retornar("Topo da montanha")
					print(resultado_etapa)
				i += 1
			    if resultado_etapa == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
			        return(f'Você não conseguiu cumprir sua missão nesta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')				  
			    else:
				return(f'Parabéns! Você conseguiu cumprir esta etapa e está pronto(a) para continuar sua jornada! Você conta agora com atributo_melhorado = , hp = e obteve uma nova arma! Antes de prosseguir, você decide parar e descansar por uma noite...')
			else:
			    return(f'Parabéns! Você conseguiu cumprir esta etapa e está pronto(a) para continuar sua jornada! Você conta agora com atributo_melhorado = , hp = e obteve uma nova arma! Antes de prosseguir, você decide parar e descansar por uma noite...')
					  
		elif escolha_1 == 3:
			# CAMINHO 3: OASIS - DUNAS - TOPO DA MONTANHA
			t += 1
			print("Você está no oásis!")
			print(oasis(meus_objetos_coletados, meus_atributos))
			print("Você está prosseguindo sua caminhada...")
			print(bt.enter())
			print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS")
			print("Você encontrou uma serpente no caminho!")
			bt.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
			print("ADICIONAR MAIS DESCRIÇÃO DE CAMINHO")
			if "runa" not in meus_objetos_coletados:
				while y < 1:
					coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não"))
					if coleta_de_objetos == 1:
						y += 1
						meus_objetos_coletados.append("runa")
						print("Runa coletada!")
						print("Seu novo item é runa!")
					elif coleta_de_objetos == 2:
						y += 1
						print("OK!")
					else:
						print("Comando não conhecido, tente novamente.")
			print("Você chegou às dunas do deserto...")
			print(bt.enter())
			print(dunas(meus_objetos_coletados))
			print("Você está prosseguindo sua caminhada...")
			#print(delete_last_lines())
			print("Só resta um local para explorar agora...")
			print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
			if "chave" not in meus_objetos_coletados:
				while z < 1:
					coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
					if coleta_de_objetos == 1:
						z += 1
						meus_objetos_coletados.append("chave")
						print("Chave coletada!")
						print("Seu novo item é chave!")
					elif coleta_de_objetos == 2:
						z += 1
						print("OK!")
					else:
						print("Comando não conhecido, tente novamente.")
			print("Você chegou ao topo da montanha...")
			print(bt.enter())
			print(topo_da_montanha(meus_objetos_coletados))
			resultado_etapa = oasis(meus_objetos_coletados, meus_atributos)
			if resultado_etapa == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
			    i = 0
		            j = 0
			    k = 0
			    print("Você tem duas chances para retornar aos locais anteriores e tentar cumprir esta etapa!")
			    retorno = int(input("Para onde deseja retornar? 1 - Dunas / 2 - Topo da montanha "))
			    while i < 1:	
			        if retorno == 1:
			            i += 1
				    resultado_etapa = retornar("Dunas")
			            print(resultado_etapa)
			            if resultado_etapa == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
			                resultado_etapa = retornar("Dunas")
				        print(resultado_etapa)
				        
				    if retorno == 2:
					j += 1
					while k < 1:
					    resultado_etapa = retornar("Topo da montanha")
					    print(resultado_etapa)
					    if resultado_etapa =! 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
					        k += 1
				i += 1
			    if resultado_etapa == 'Você não conseguiu cumprir esta etapa! Continue sua exploração pelo deserto e tente novamente...':
			        return(f'Você não conseguiu cumprir sua missão nesta etapa, mas está livre para continuar sua jornada. Antes de prosseguir, você decide parar e descansar por uma noite...')				  
                            else:
				return(f'Parabéns! Você conseguiu cumprir esta etapa e está pronto(a) para continuar sua jornada! Você conta agora com atributo_melhorado = , hp = e obteve uma nova arma! Antes de prosseguir, você decide parar e descansar por uma noite...')
			else:
			    return(f'Parabéns! Você conseguiu cumprir esta etapa e está pronto(a) para continuar sua jornada! Você conta agora com atributo_melhorado = , hp = e obteve uma nova arma! Antes de prosseguir, você decide parar e descansar por uma noite...')					  
									  
