# contextualização inicial
 
import time
 
 
def introducao():
 
    string = "Você acorda...\n""Está cercado de prisioneiros, grades te separam do mundo externo, você é um prisioneiro que já não tinha esperanças de \num dia sair da cadeia até que um dia o carrasco da prisão se dirige  aos detentos:\n""-Seus trastes, a esperança de vocês chegou, um de vocês será incumbido de realizar uma missão em nome do reino para \nconquistar a liberdade, mas a questão é, quem será?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# história em que se passa
def narracaocastelo():
 
    string = "-Acho que você deve ser o menos provável a fracassar, aproxime-se.\n""O guarda então lhe explica toda a situação\n""Há anos a situação entre o reino de Mitria no qual você se encontra e o reino de Nimide ao norte se mantém delicada, \npor receio do início de uma guerra ambos os reinos constantemente aumentam o seu poderio militar, aumentando cada vez \nmais as tensões entre os reinos.\n""Recentemente um espião nosso que estava infiltrado no reino de Nimide descobriu recentes documentos adquiridos pelos \nrivais indicando a localização de um artefato antigo conhecido como o cajado de serafim em uma caverna próxima na \nfronteira entre os reinos.\n"" Pouco se sabe sobre o objeto, embora lendas e histórias rodeiam o artefato, poucos são os dados históricos sobre o seu \nuso, sabe-se apenas que tratasse de um imenso poder, mas o resto é envolto em mistérios.\n""Sabendo disso o reino não pode permitir que tal objeto caia perante as mãos rivais, entretanto o receio de dar início \naos conflitos armados entre os povos impede qualquer ação oficial do exército mitriano.\n""Sendo assim você foi incumbido de roubá-lo e trazê-lo antes que ele chegue aos cofres de Nimide.\n""Porém, para impedir qualquer traição de sua parte uma maldição foi jogada sobre você, e caso você não complete a missão \ndentro de 72 horas e retorne a Mitria, você morrerá\n""Você por não querer passar o resto de sua vida na prisão aceita a missão do guarda.\n""-Pois bem agora me acompanhe prisioneiro.\n""O guarda lhe escolta pela escura e sombria prisão, de volta até o exterior quente e ensolarado depois de muitos anos \nentretanto não temos tempo a perder, nenhum apoio do governo lhe será oferecido e terras estranhas lhe aguardam a \nfrente, será necessário adquirir mais informações para seguir em frente\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# TAVERNA
 
def narracaotaverna():
 
    string = "Você entre na taverna, o barulho de bárbaros e o cheiro de suas bebidas predominam sobre o lugar, e você começa a \nprocurar algum jeito de adquirir informação\n"
    
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BÊBADO
 
def bebado1():
    
    string = " (1) Com licença o senhor sabe como eu faço para chegar na fronteira com Dimitria?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bebado2():
 
    string = " (2) Meu companheiro, me fale com chegar a fronteira norte.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bebado3():
 
    string = " (3) Oh seu vagabundo, como que faz pra cruzar a fronteira de Dimitria?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bebadoresp():
    
    string = "O que você falou? Tá querendo brigar? Vem resolver isso aqui seu fracote.\n(Você se afasta do bêbado para não instigar uma briga)\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BARMAN
 
def barman1():
   
    string = " (1) Meu camarada, você sabe me falar como eu faço para chegar na fronteira ao norte?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman2():
 
    string = " (2) Com a sua licença, o senhor sabe me dizer como eu faço para chegar até Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman3():
 
    string = " (3) Oh seuzinho, me fala como eu chego na fronteira norte.\n"
   
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman1resp():
 
    string = "Mas é claro, com todos esses anos atendendo clientes eu descobri que o melhor jeito é cruzar o deserto, no caminho \nexistem vários objetos que podem te ajudar na sua jornada\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman2resp():
 
    string = "Mas que desnecessário esse seu jeito de falar, você está em uma taverna, é só você pegar o caminho do deserto que você \nchega.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman3resp():
 
    string = "Quem você pensa que é pra falar comigo assim, saia da minha frente\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# MERETRIZ
 
def meretriz1():
 
    string = " (1) Madame, a senhora sabe me dizer como eu faço pra chegar na fronteira norte?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz2():
 
    string = " (2) Hey, você ai, como que faz pra chegar em Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz3():
 
    string = " (3) Oh velha senhora, me conta como faz pra chegar na fronteira de Nimide.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz1resp():
 
    string = "Oh darling, minhas garotas recebem muitos viajantes e eles dizem que o melhor é ir pela floresta, e eles falam pra \nseguir as cores frias no caminhar, seja lá o que isso for.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz2resp():
 
    string = "Mas respeito garoto, por favor. Vá pela floresta que você conseguirá chegar até a fronteira.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz3resp():
 
    string = "Quem você é pensa que é garoto pra falar comigo assim? Saia da minha frente.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BIBLIOTECA
 
def narracaobiblioteca():
 
    string = "O conhecimento presente entre os livros e as pessoas no lugar podem provar-se muito uteis para voce, mas onde seria o \nmelhor lugar para descobrir essa informação.\n"
   
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
    
    return
 
# LIVRO
 
def livro():
 
    string = "Você procura algum livro que possa te ajudar mas nao esta conseguindo achar, talvez alguém possa te ajudar\n"
    
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BIBLIOTECARIA
 
def bibliotecaria1():
 
    string = " (1) Com licença, a senhora sabe me dizer como descobrir o caminho para Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria2():
 
    string = " (2) Hey, você aí, como eu faço pra descobrir o caminho para Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria3():
 
    string = " (3) Oh velha senhora atrás do balcão, onde eu descubro como chegar em Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria1resp():
 
    string = "Mas é claro meu jovem rapaz, veja nesse livro aqui (a bibliotecária lhe dá um livro de viagens com anotações de outros \nviajantes mostrando que o melhor caminho é o deserto e que para ajudar na jornada existem alguns objetos no caminho, mas \nque nem todos são confiáveis.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria2resp():
 
    string = "Um pouco de respeito a mais seria bom meu jovem, veja nesse livro \n(a bibliotecária lhe dá um livro de mapas indicando que é possível chegar a fronteira de Nimide ao cruzar o deserto).\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria3resp():
 
    string = "Mas que desrespeito meu jovem, não irei te ajudar em nada.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# ESTUDANTE
 
def estudante1():
    
    string = " (1) Minha jovem, você parece ser uma pessoa muito inteligente, a senhorita sabe me dizer como chegar a fronteira norte \ndo reino?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante2():
    
    string = " (2) Oh garota, você sabe me falar como chegar em Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante3():
    string = " (3) Oh sua jovenzinha aí, você não sabe como faz pra chegar em Nimide não né?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante1resp():
    string = "Sei sim meu senhor, eu li em algum livro que o melhor jeito é ir pelo deserto mas ele dizia que embora existam objetos \nno caminho que poderiam ser úteis.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante2resp():
    string = "Nossa um pouco a mais de educação não machuca, eu vi em algum livro que é melhor viajar pelo deserto.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante3resp():
    string = "Mas que homem rude, eu até sei, mas não irei te ajudar, agora saia daqui.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BECO
 
def narracaobeco():
    string = "Essa parte da cidade parece meio obscura, mas talvez as pessoas que se reúnem aqui tenham alguma informação.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# SÁBIO
 
def sabio1():
    string = " (1) O senhor parece ser muito esperto, saberia me dizer como chegar até a fronteira de Nimide\n?"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio2():
    string = " (2) Hey, o senhor aí, você sabe me dizer como chegar a fronteira norte do reino?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio3():
    string = " (3) Oh seu velho, me fala ai, você sabe como eu faço pra chegar até Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio1resp():
    string = "De fato meu jovem eu sei te dizer, com todos os meus anos de vida eu sempre fui pela floresta, mas existe um truque para\n isso, siga as cores frias no caminho.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio2resp():
    string = "Nossa, um pouco de delicadeza a mais viria a calhar, você deve ir pela floresta, é o caminho que eu sempre uso.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio3resp():
    string = "Quem você pensa que é pra me chamar de velho desse jeito? Não irei te ajudar, agora saia daqui.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# VIAJANTE
 
def viajante1():
    string = " (1) Com licença, o senhor me parece ser um viajante, por acaso você conhece o melhor caminho para Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante2():
    string = " (2) Hey andarilho, você sabe o melhor caminho para Nimide?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante3():
    string = " (3) Oh  seu nomadezinho, você deve saber como chegar a Nimide, me conte.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante1resp():
    string = "O senhor está certo e eu conheço o caminho, eu vou pela floresta, o segredo é seguir as cores frias.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante2resp():
    string = "Que agressivo, o melhor caminho é a floresta meu senhor.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante3resp():
    string = "Mas que grosseiro, nao tenho nada pra te falar, segue o seu caminho\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# MENDIGO
 
def mendigo1():
   
    string = " (1) Pobre senhor, você saberia me dizer o caminho para Nimide.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
    
def mendigo2():
   
    string = " (2) Oh mendigo, você não sabe o caminho para Nimide não né?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
      
def mendigo3():
   
    string = " (3) Hey você aí largado na rua, se você souber me conta, como eu chego na fronteira norte do país?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
  
def mendigoresp():
    string = "Oh meu senhor, eu lá tenho cara de quem viaja pra fora do reino? Eu não sei não\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
 

