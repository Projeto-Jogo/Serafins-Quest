# MÓDULO "DESERTO"

###########################################################################################################

import Batalha # Importando o módulo "Batalha"

# Definição de funções

def enter(): # (OK) "Botão" para prosseguir
    return input('\naperte enter para continuar')
def dunas(objetos_coletados): # (OK) Função que representa a trajetória do jogador nas dunas de areia do deserto 
    # a, b, c e d são variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não tenha selecionado uma resposta válida
    a = b = c = d = e = 0
    if "pedra" in objetos_coletados and "poção" in objetos_coletados: # Se o jogador já coletou a pedra e a poção, aparece um aviso de que não há mais objetos para coletar no local
        return(f'Você ja coletou os objetos que necessitava aqui!') 
    elif "pedra" in objetos_coletados and "poção" not in objetos_coletados: # Se o jogador já coletou a pedra, encontra apenas uma poção
        while a < 1:
            escolha = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não")) # O jogador escolhe se quer coletar a poção ou não
            if escolha == 1:
                objetos_coletados.append("poção")
                print("Poção coletada!")
                return(f'Seu novo item é poção')
                while b < 1:
                    escolha_2 = int(input("Beber poção? 1 - Sim / 2 - Não"))
                    if escolha_2 == 1:
                        hp -= 1
                        print(f'Ah, não! Esta poção é perigosa! Você perdeu 1 HP!')
                        b += 1
                    elif escolha_2 == 2:
                        print("OK!")
                        b += 1
                    else:
                        print("Escolha uma opção válida!")
                a += 1
            elif escolha == 2:
                print("OK!")
                return(f'Você não coletou nenhum novo item!')
                a += 1
            else:
                print("Escolha uma opção válida!")
    elif "poção" in objetos_coletados and "pedra" not in objetos_coletados:
        while c < 1:
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("pedra")
                print("Pedra coletada!")
                return(f'Seu novo item é pedra!')
                c += 1
            elif escolha == 2:
                print("OK!")
                return(f'Você não coletou nenhum novo item!')
                c += 1
            else:
                print("Escolha uma opção válida!")
    else:
        while d < 1:
            escolha = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("poção")
                print("Poção coletada!")
                d += 1
            elif escolha == 2:
                print("OK!")
                d += 1
            else:
                print("Escolha uma opção válida!")
        print("ADICIONAR DESCRIÇÃO DE UM CAMINHO")
        enter()
        while e < 1:
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("pedra")
                print("Pedra coletada!")
                e += 1
            elif escolha == 2:
                print("OK!")
                e += 1
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
def topo_da_montanha(objetos_coletados): # (OK) Funçao para a trajetória do jogador no topo de uma montanha no deserto
    a = 0
    if "flor" in objetos_coletados:
        print("Você ja coletou o objeto que necessitava aqui!")
    else:
	while a < 1:
            escolha = int(input("Você encontrou uma flor do deserto! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("flor")
                return(f'Seu novo item é uma flor do deserto!')
		a += 1
            elif escolha == 2:
                print("OK!")
                return(f'Você não coletou novos itens!')
                a += 1
	    else:
		print("Escolha uma opção válida!")
		
def oasis(objetos_coletados, atributos):

# Função utilizada para a trajetória do jogador em um oasis no deserto
    hp = atributos[5]
    a = b = c = d = e = f = 0 #
    i = -1
    desbloqueio = False
    missao_cumprida = False
    combinacao_correta = ["poção", "flor", "runa", "pedra"]
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
                        print(f'Parabéns! Você conseguiu entrar no ao oasis!')
                        enter()

                        #bt.passar_nivel(jogador)
                        print("ADICIONAR DESCRIÇÃO DO OASIS")
                        enter()

                        print("Há uma serpente no caminho!")
                        #print(bt.batalha(Serpente, jogador))

                        print("Siga para o lago agora...")
                        enter()
                        #bt.delete_last_lines(1)
                        print("Você mergulhou no lago!")
                        enter()
                        #bt.delete_last_lines(1)
                        print("ADICIONAR DESCRIÇÃO DO LAGO")
                        print("Parece que há algo lá no fundo, a alguns metros...")
                        enter()
                        #bt.delete_last_lines(1)
                        print("Nadando e chegando mais perto, você vê que é um báu!")
                        while c < 1:
                            escolha_1 = int(input("O que deseja fazer? 1 - Coletar o baú / 2 - Sair do lago "))
                            if escolha_1 == 1:
                                c += 1
                         #       bt.delete_last_lines(1)
                                print("Você pegou o baú!")
                                print("Saia do lago agora e veja o que há dentro dele...")
                                enter()
                                print("ADICIONAR DESCRIÇÃO DO JOGADOR SAINDO DO LAGO")
                          #      bt.delete_last_lines(1)
                                abertura_do_bau = int(input("Digite 1 para abrir o baú! "))
                                if abertura_do_bau == 1:
                                    d += 1
                                    if "chave" in objetos_coletados:
                                        print("Você conseguiu!")
                                        #print(bt.passar_nivel(jogador))
                                        while e < 1:
                                            beber_pocao_brilhante = int(input("Há uma poção brilhante lá dentro! Digite 1 para bebê-la..."))
                                            if beber_pocao_brilhante == 1:
                                                e += 1
                                                hp += 20
                                                print(f'Você ganhou 20 HPs após beber a poção! Seus HPs: {hp}')

                                        print("Também há uma nota dentro do baú... leia!")
                                        enter()
                           #             bt.delete_last_lines(1)
                                        print("Na nota está escrito 'URSO'..")
                                        print("Hmm... o que será que isso quer dizer? Guarde esta palavra, ela pode ser útil mais tarde...")
                                        enter()
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

def retornar(local, objetos_coletados, *atributos): # (OK) Funçao utilizada para que o jogador possa retornar a lugares por quais já passou anteriormente
    if local == "Dunas":
        print("Bem vindo(a) de volta ao oasis!")
        return dunas(objetos_coletados)
    elif local == "Topo da montanha":
        print("Bem vindo(a) de volta ao topo da montanha!")
        return topo_da_montanha(objetos_coletados)
    elif local == "Oasis":
        print("Bem vindo(a) de volta ao oasis!")
        return oasis(objetos_coletados, atributos)

############################################################################################################################

x = y = z = 0 # x, y e z são variáveis utilizadas para o mecanismo de repetição de perguntas caso o jogador não informe uma escolha válida
meus_objetos_coletados = [] # Lista para incluir os objetos que o jogador coleta ao logo da trajetória no deserto
meus_atributos = [1, 2, -3, 4, 5]  # Valores dos atributos do jogador: força, destreza, inteligência, sorte e carisma, respectivamente 
#hp = 

# Introdução do ambiente (deserto) ao jogador
print("Você chegou ao deserto!")
print("ADICIONAR DESCRIÇÃO INTRODUTÓRIA DO DESERTO")
enter()

# O jogador escolhe para qual local deseja ir primeiro (dunas de areia, topo da montanha ou oasis)
escolha_1 = int(input("Qual local deseja explorar primeiro? 1 - Dunas de areia / 2 - Topo da montanha / 3 - Oasis"))

# Se a escolha for dunas de areia:
if escolha_1 == 1:

# CAMINHO 1
# O jogador escolhe seguir para as dunas de areia primeiro:
    print("Você está nas dunas!")
    print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA") # Descrição do ambiente ao jogador
    enter()
    dunas(meus_objetos_coletados) # Chama função dunas()
    print("Você está prosseguindo sua caminhada...")
    escolha_2 == int(input("Qual é o seu próximo destino? 1 - Topo da montanha / 2 - Oasis")) # O jogador escolhe para onde ir em seguida

    if escolha_2 == 1:
# O jogador escolhe seguir das dunas para o topo da montanha:    

        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        if coleta_de_objetos == 1: # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            Batalha.batalha(Serpente, jogador)#  chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        if "chave" not in meus_objetos_coletados: # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
            coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
            if coleta_de_objetos == 1:  # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
                meus_objetos_coletados.append("chave") # Se não, o jogador continua o caminho pelo deserto
            else:
                enter()
        else:
            enter()
	print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
        print("Você está chegando ao topo da montanha...")
        enter()
        print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
        topo_da_montanha(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        enter()
        print("Só resta um local para explorar agora...")
        
# Finalmente, o jogador segue do topo da montanha a um oasis

	print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA ATÉ O ENCONTRO DE UM OASIS NO DESERTO")		
        print("Há um oasis a alguns metros!")
        if "runa" not in meus_objetos_coletados:
            coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("runa")
            else:
                enter()
        else:
            enter()
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
			            print("Escolha uma opção válida!")
				    	
        elif escolha_2 == 2:
# CAMINHO 2
# O jogador escolhe seguir das dunas de areia ao oasis:

            # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
            # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            if coleta_de_objetos == 1:
                Batalha.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
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
                    enter()
            else:
                enter()
            
            print("Você chegou ao topo da montanha!")
            print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
            topo_da_montanha(meus_objetos_coletados)
            print("Você está prosseguindo sua caminhada...")
            enter()

elif escolha_1 == 2:
				    
# CAMINHO 3:
# O jogador escolhe seguir para o topo da montanha primeiro
				    
    print("Você está no topo da montanha!")
    print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
    enter()
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
                enter()
        else:
            enter()

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        print("Você chegou às dunas!")
	print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
        enter()
    	#chama função "dunas"
	dunas(meus_objetos_coletados)
	print("Você está prosseguindo sua caminhada...")
	print("Só resta um local para explorar agora...")
	enter()
        
# Finalmente, o jogador segue das dunas de areia ao oasis

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
         
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
                    enter()
            else:
                enter()
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA ATÉ O ENCONTRO DE UM OASIS NO DESERTO")
            oasis(meus_objetos_coletados, meus_atributos)     
            print("Você está prosseguindo sua caminhada...")
            enter()

# Finalmente, o jogador segue do oasis às dunas de areia

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS DE AREIA")
        if "runa" not in meus_objetos_coletados:
            coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("runa")
            else:
                enter()
        else:
            enter()
        print("Você chegou às dunas de areia!")
        dunas(meus_objetos_coletados, meus_atributos)  
        print("Você está prosseguindo sua caminhada...")
        enter()
    
if escolha_1 == 3:

# CAMINHO 5: 
# O jogador escolhe seguir ao oasis primeiro 

    print("Você chegou a um oasis!")
    enter()
    # chama função "oasis"
    oasis(meus_objetos_coletados)
    print("Você está prosseguindo sua caminhada...")
    escolha_2 == int(input("Qual é o seu próximo destino? 1 - Dunas / 2 - Topo da montanha"))
				    
        if escolha_2 == 1:
# O jogador segue do oasis às dunas de areia

        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS DE AREIA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        print("Você chegou às dunas de areia!")
        dunas(meus_objetos_coletados)  
        print("Você está prosseguindo sua caminhada...")
        print("Só resta um local para explorar agora...")
	enter()
    
# Finalmente, o jogador segue das dunas de areia ao topo da montanha
        # Descrição do caminho entre as dunas de areia ao topo da montanha
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
        if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
            coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
            else:
                enter()
        else:
            enter()
        print("Você está chegando ao topo da montanha...")
        enter()
        print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
        topo_da_montanha(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        enter()

    elif escolha_2 == 2:
# CAMINHO 6:
# O jogador segue do oasis ao topo da montanha
        if "runa" not in meus_objetos_coletados:
            coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("runa")
            else:
                enter()
        else:
            enter()
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E O TOPO DA MONTANHA")
        print("Você chegou ao topo da montanha!")
        enter()
        print("Descrição de ambiente - Topo da montanha")
        topo_da_montanha(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        print("Só resta um local para explorar agora...")
        enter()
        
# O jogador segue do topo da montanha às dunas de areia
         # Descrição do caminho entre o topo da montanha e as dunas de areia
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha(Serpente, jogador) # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
        if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
            coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
            else:
                enter()
        else:
            enter()
        print("Você está chegando às dunas de areia...")
        enter()
        print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
        dunas(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        enter()
				    
missao_cumprida = oasis(meus_objetos_coletados, meus_atributos)
while z < 1:
    if missao_cumprida == "Parabéns! Você cumpriu sua missão, aumentando seus atributos, ganhando HPs e obtendo uma dica para continuar!":
        print("Você está pronto para prosseguir em sua jornada...")
        z += 1
    else:
        print("Você ainda não completou essa etapa!")
