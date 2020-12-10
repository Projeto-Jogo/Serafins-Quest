# contextualização inicial
 
import time
 
 
def introducao():
 
    string = "Você acorda...\n""Está cercado de prisioneiros, grades te separam do mundo externo, você é um prisioneiro que já não tinha esperanças de \nsair da cadeia. Até que um dia o carrasco da prisão se dirige aos detentos:\n""- Seus trastes, a esperança de vocês chegou. Um de vocês será incumbido de realizar uma missão em nome do reino para \nconquistar a liberdade. Mas a questão é, quem será?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# história em que se passa
def narracaocastelo():
 
    string = "- Acho que você deve ser o menos provável a fracassar, aproxime-se.\n""O guarda então lhe explica toda a situação:\n""- Há anos, a situação entre o reino de Mitria, no qual você se encontra, e o reino de Nimidia ao norte se mantém delicada.\nPor receio do início de uma guerra ambos os reinos constantemente aumentam o seu poderio militar, aumentando cada vez \nmais as tensões entre os reinos.\n""Recentemente um espião nosso infiltrado no reino de Nimidia descobriu novos documentos adquiridos pelos \nrivais, indicando a localização de um artefato antigo conhecido como Cajado de Serafin em uma casa misteriosa próxima à \nfronteira entre os reinos.\n""Pouco se sabe sobre o objeto. Embora lendas e histórias rodeiem o artefato, poucos são os dados históricos sobre o seu \nuso. Sabe-se apenas que possui um imenso poder, mas o restante é envolto em mistérios.\n""Sabendo disso, o reino não pode permitir que tal objeto caia em mãos rivais. Entretanto, o receio de dar início \naos conflitos armados entre os povos impede qualquer ação oficial do exército mitriano.\n""Sendo assim você foi incumbido de roubá-lo e trazê-lo antes que ele chegue aos cofres de Nimidia.\n""Porém, para impedir qualquer traição de sua parte, uma maldição foi jogada sobre você e caso você não complete a missão \ndentro de 72 horas e retorne a Mitria, você morrerá.\n\n""Por não querer passar o resto de sua vida na prisão, você aceita a missão do guarda.\n""- Pois bem, agora me acompanhe, prisioneiro.\n""O guarda lhe escolta pela escura e sombria prisão, de volta ao exterior quente e ensolarado depois de muitos anos.\nEntretanto, não tem tempo a perder, nenhum apoio do governo lhe será oferecido e terras estranhas lhe aguardam à \nfrente. Será necessário adquirir mais informações para continuar a jornada.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# TAVERNA
 
def narracaotaverna():
 
    string = "Você entra na taverna. O barulho de bárbaros e o cheiro de suas bebidas predominam sobre o lugar e você começa a \nprocurar algum jeito de adquirir informações.\n"
    
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BÊBADO
 
def bebado1():
    
    string = " (1) Com licença, o senhor sabe como eu faço para chegar na fronteira com Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bebado2():
 
    string = " (2) Meu companheiro, me fale como chegar à fronteira norte.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bebado3():
 
    string = " (3) Oh seu vagabundo, como que faz para cruzar a fronteira de Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bebadoresp():
    
    string = "O que você falou? Tá querendo brigar? Vem resolver isso aqui, seu fracote.\n(Você se afasta do bêbado para não instigar uma briga)\n"
 
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
 
    string = " (2) Com a sua licença, o senhor sabe me dizer como eu faço para chegar até Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman3():
 
    string = " (3) Oh seuzinho, me fala como eu chego na fronteira norte!\n"
   
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman1resp():
 
    string = "Mas é claro, com todos esses anos atendendo clientes eu descobri que o melhor jeito é cruzar o deserto. No caminho \nexistem vários objetos que podem ajudar na sua jornada.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman2resp():
 
    string = "Mas que desnecessário esse seu jeito de falar, você está em uma taverna. É só pegar o caminho do deserto que você \nchega.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def barman3resp():
 
    string = "Quem você pensa que é para falar comigo assim? Saia da minha frente!\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# MERETRIZ
 
def meretriz1():
 
    string = " (1) Madame, a senhora sabe me dizer como eu faço para chegar na fronteira norte?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz2():
 
    string = " (2) Hey, você aí, como que faz para chegar em Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz3():
 
    string = " (3) Oh velha senhora, me conta como faz para chegar na fronteira de Nimidia.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz1resp():
 
    string = "Oh darling, minhas garotas recebem muitos viajantes e eles dizem que o melhor é ir pela floresta. E eles falam para\nseguir as cores frias no caminhar, seja lá o que isso for.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz2resp():
 
    string = "Mais respeito garoto, por favor. Vá pela floresta que você conseguirá chegar até a fronteira.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def meretriz3resp():
 
    string = "Quem você pensa que é, garoto, para falar comigo assim? Saia da minha frente.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BIBLIOTECA
 
def narracaobiblioteca():
 
    string = "O conhecimento presente entre os livros e as pessoas no lugar podem provar-se muito úteis para você, mas onde seria o \nmelhor lugar para descobrir essa informação?\n"
   
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
    
    return
 
# LIVRO
 
def livro():
 
    string = "Você procura algum livro que seja útil, mas não está conseguindo achar. Talvez alguém possa te ajudar.\n"
    
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# BIBLIOTECARIA
 
def bibliotecaria1():
 
    string = " (1) Com licença, a senhora sabe me dizer como descobrir o caminho para Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria2():
 
    string = " (2) Hey, você aí, como eu faço para descobrir o caminho para Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria3():
 
    string = " (3) Oh velha senhora atrás do balcão, onde eu descubro como chegar em Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria1resp():
 
    string = "Mas é claro, meu jovem rapaz, veja nesse livro aqui. \n(A bibliotecária lhe dá um livro de viagens com anotações de outros \nviajantes mostrando que o melhor caminho é o deserto, que para ajudar na jornada existem alguns objetos no caminho e \nque nem todos são confiáveis.)\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria2resp():
 
    string = "Um pouco de respeito a mais seria bom, meu jovem. Veja nesse livro. \n(A bibliotecária lhe dá um livro de mapas indicando que é possível chegar à fronteira de Nimida ao cruzar o deserto.)\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def bibliotecaria3resp():
 
    string = "Mas que desrespeito, meu jovem! Não irei te ajudar em nada.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# ESTUDANTE
 
def estudante1():
    
    string = " (1) Minha jovem, você parece ser uma pessoa muito inteligente. A senhorita sabe me dizer como chegar à fronteira norte \ndo reino?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante2():
    
    string = " (2) Oh garota, você sabe me falar como chegar em Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante3():
    string = " (3) Oh sua jovenzinha aí, você não sabe como faz para chegar em Nimidia não né?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante1resp():
    string = "Sei sim, meu senhor, eu li em algum livro que o melhor jeito é ir pelo deserto e que existem objetos \nno caminho que podem ser úteis.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante2resp():
    string = "Nossa, um pouco mais de educação não machuca. Eu vi em algum livro que é melhor viajar pelo deserto.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def estudante3resp():
    string = "Mas que homem rude! Eu até sei, mas não irei te ajudar. Agora saia daqui!\n"
 
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
    string = " (1) O senhor parece ser muito esperto, saberia me dizer como chegar até a fronteira de Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio2():
    string = " (2) Hey, o senhor aí, você sabe me dizer como chegar à fronteira norte do reino?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio3():
    string = " (3) Oh seu velho, me fala aí, você sabe como eu faço para chegar até Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio1resp():
    string = "De fato, meu jovem, eu sei te dizer. Com todos os meus anos de vida, eu sempre fui pela floresta, mas existe um truque para\nisso: siga as cores frias no caminho.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio2resp():
    string = "Nossa, um pouco de delicadeza a mais viria a calhar! Você deve ir pela floresta, é o caminho que eu sempre uso.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def sabio3resp():
    string = "Quem você pensa que é pra me chamar de velho desse jeito? Não irei te ajudar, agora saia daqui!\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# VIAJANTE
 
def viajante1():
    string = " (1) Com licença, o senhor me parece ser um viajante, por acaso conhece o melhor caminho para Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante2():
    string = " (2) Hey, andarilho, você sabe o melhor caminho para Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante3():
    string = " (3) Oh seu nomadezinho, você deve saber como chegar a Nimidia, me conte.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante1resp():
    string = "O senhor está certo e eu conheço o caminho. Eu vou pela floresta, o segredo é seguir as cores frias.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante2resp():
    string = "Que agressivo! O melhor caminho é a floresta, senhor.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
def viajante3resp():
    string = "Mas que grosseiro, não tenho nada para te falar! Segue o seu caminho.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
# MENDIGO
 
def mendigo1():
   
    string = " (1) Pobre senhor, você saberia me dizer o caminho para Nimidia?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
    
def mendigo2():
   
    string = " (2) Oh mendigo, você não sabe o caminho para Nimidia não né?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
      
def mendigo3():
   
    string = " (3) Hey, você aí largado na rua, se você souber me conta, como eu chego na fronteira norte do reino?\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
  
def mendigoresp():
    string = "Oh meu senhor, eu lá tenho cara de quem viaja para fora do reino? Eu não sei não.\n"
 
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
 
    return
 
 

