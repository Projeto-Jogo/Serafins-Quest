# contestualizaçao inicial

import time


def introducao():

    string = "Você acorda...\n""Esta cercado de prisioneiros, grades te separam do mundo externo, você é um prisioneiro que já não tinha esperanças de um dia sair da cadeia até que um dia o carrasco da prisão se dirige  aos detentos:\n""-Seus trastes, a esperança de vocês chegou, um de vocês será incumbido de realizar uma missão em nome do reino para conquistar a liberdade, mas a questão é, quem será?\n"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# historia em que se passa
def narracaocastelo():

    string = "-Acho que você deve ser o menos provável a fracassar, aproxime-se.\n""O guarda então lhe explica toda a situação\n""Há anos a situação entre o reino de Mitria no qual você se encontra e o reino de Nimide ao norte se mantem delicada, por receio do inicio de uma guerra ambos os reinos constantemente aumentam o seu poderio militar, aumentando cada vez mais as tensões entre os reinos.\n""Recentemente um espiao nosso que estava infiltrado no reino de Nimide descobriu recentes documentos adiquiridos pelos rivais indicando a localização de um artefato antigo conhecido como o cajado de serafim em uma caverna próxima na fronteira entre os reinos.\n"" Pouco se sabe sobre o objeto, embora lendas e historias rondeiem o artefato, poucos são os dados históricos sobre o seu uso, sabe-se apenas que tratasse de um imenso poder, mas o resto é envolto em mistérios.\n""Sabendo disso o reino não pode permitir que tal objeto cai perante as mãos rivais, entretanto o receio de dar inicio as conflitos armados entre os povos impede qualquer ação oficial do exercito mitriano.\n""Sendo assim você foi incumbido de rouba-lo e traze-lo antes que ele chegue aos cofres de Nimide.\n""Porém, para impedir qualquer traição de sua parte uma maldição foi jogada sobre você, e caso você não complete a missão dentro de 72 horas e retorne a Mitria, você morrerá\n""Você por não querer passar o resto de sua vida na prisão aceita a missão do guarda.\n""-Pois bem agora me acompanhe prisioneiro.\n""O guarda lhe escolta pela escura e sombria prisão, de volta ate o exterior quente e ensolarado depois de muitos anos entretanto não a tempo a perder, nenhum apoio do governo lhe sera oferecido e terras estranhas lhe aguardam a frente, será necessário adquirir mais informações para seguir em frente\n"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# TAVERNA

def narracaotaverna():

    string = "Você entre na taverna, o barulho de bárbaros e o cheiro de suas bebidas predominam sobre o lugar, e voce comeca a procuraar algum jeito de adiquirir informação"
    
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# BEBADO

def bebado1():
    
    string = " (1) Com licenca o senhor sabe como eu faco para chegar na fronteira com Dimitria?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bebado2():

    string = " (2) Meu companheiro, me fale com chegar a fronteira norte"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bebado3():

    string = " (3) Oh seu vagabundo, como que faz pra cruzar a fronteira de Dimitria?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bebadoresp():
    
    string = "O que voce falou? Tá querendo brigar? Vem resolver isso aqui seu fracote.\n(Voce se afasta do bebado para nap instigar uma briga)"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# BARMAN

def barman1():
   
    string = " (1) Meu camarada ,voce sabe me falar como eu faço para chegar na fronteira ao norte?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def barman2():

    string = " (2) Com a sua licença, o senhor sabe me dizer como eu faço para chegar até Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def barman3():

    string = " (3) Oh seuzinho, me fala como eu chego na fronteira norte"
   
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def barman1resp():

    string = "Mas é claro, com todos esses anos atendendo clientes eu descobri que o melhor jeito é cruzar o deserto, no caminho existem varios objetos que podem te ajudar no seu caminho, mas tome cuidado, nem tudo sao flores"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def barman2resp():

    string = "Mas que desnecessario esse seu jeito de falar, voce esta em uma taverna, é só voce pegar o caminho do deserto que voce chega."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def barman3resp():

    string = "Quem voce pensa q é pra falar comigo assim, saia da minha frente"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# MERETRIZ

def meretriz1():

    string = " (1) Madame, a senhora sabe me dizer como eu faco pra chegar na fronteira norte?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def meretriz2():

    string = " (2) Hey, voce ai, como que faz pra chegar em Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def meretriz3():

    string = " (3) Oh velha senhora, me conta como faz pra chegar na fronteira de Nimide."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def meretriz1resp():

    string = "Oh darling, minhas garotas recebm muitos viajantes e eles dizem que o melhor é ir pela floresta, e eles falam pra seguir as cores frias no caminha, seja lá o que isso for."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def meretriz2resp():

    string = "Mas respeito garoto, por favor. Vá pela floresta que voce conseguira chegar até a fronteira."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def meretriz3resp():

    string = "Quem voce é pensa que é garoto pr falar comigo assim? Saia da minha frente."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# BIBLIOTECA

def narracaobiblioteca():

    string = "O conhecimento presente entre os livros e as pessoas no lugar podem provar-se muito uteis para voce, mas onde seria o melhor lugar para descobrir essa informaçao"
   
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)
    
    return

# LIVRO

def livro():

    string = "Voce procura algum livro que possa te ajudar mas nao esta conseguindo achar, talvez alguem possa te ajudar"
    
    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# BIBLIOTECARIA

def bibliotecaria1():

    string = " (1) Com licenca, a senhora sabe me dizer como descobrir o caminho para Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bibliotecaria2():

    string = " (2) Hey, voce aí, como eu faco pra descobrir o caminho pra Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bibliotecaria3():

    string = " (3) Oh velha senhora atras do balcao, onde eu descubro como chegar em Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bibliotecaria1resp():

    string = "Mas é claro meu jovem rapaz, veja nesse livro aqui (a bibliotecar lhe dá um livro de viagens com anotacoes de outros viajantes mostrando que o melhor caminho é o deserto e que para ajudar na jornada existem alguns objetos no caminho mas que nem todos sao confiaveis."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bibliotecaria2resp():

    string = "Um pouco de respeito a mais seria bom meu jovem, veja nesse livro ( a bibliotecaria lhe da um livre de mapas indicando que é possivel chegar a fronteira de Nimide ao cruzar o deserto."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def bibliotecaria3resp():

    string = "Mas que desrespeito meu jovem, nao irei te ajudar em nada."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# ESTUDANTE

def estudante1():
    
    string = "Minha jovem, voce parece ser uma pessoa muito inteligente, a senhorita sabe me dizer como chegar a fronteira norte do reino?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def estudante2():
    
    string = "Oh garota, voce sabe me falar como chegar em Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def estudante3():
    string = "Oh sua jovenzinha ai, voce nao sabe como faz pra chegar em Nimide nao né?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def estudante1resp():
    string = "Sei sim meu senhor, eu li em algum livro que o melhor jeito é ir pelo deserto mas ele dizia que embora existam objetos no caminho que poderiam ser uteis, algos poderiam ser ruins."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def estudante2resp():
    string = "Nossa um pouco a mais de educaçao nao machuca, eu vi em algum livro que deviasse viajar pelo deserto."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def estudante3resp():
    string = "Mas que homem rude, eu até sei, mas nao irie te ajudar, agr saia daqui."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# BECO

def narracaobeco():
    string = "Essa parte da cidade parece meio obscura, mas talvez as pessoas que se reunem aqui tenham alguma informacao"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# SABIO

def sabio1():
    string = "O senhor parece ser muito esperto, saberia me dizer como chegar ate a fronteira de Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def sabio2():
    string = "Hey, o senhor ai, voce sabe me dizer como chegar a fronteira norte do reino?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def sabio3():
    string = "Oh seu velho, me fala ai, voce sabe como eu faço pra chegar até Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def sabio1resp():
    string = "De fato meu jovem eu sei te dizer, com todos os meus anos de vida eu sempre fui pela floresta, mas existe um truque para isso, siga as cores frias no caminho."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def sabio2resp():
    string = "Nossa, um pouco de delicadeza a mais viria a calhar, voce deve ir pela floresta, é o caminho que eu sempre uso."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def sabio3resp():
    string = "Quem voce pensa que é pra me chamar de velho desse jeito? Nao irie te ajudar, agora saia daqui."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# VIAJANTE

def viajante1():
    string = "Com liceça, o senhor me parece ser um viajante, por acaso voce conhece o melhor caminho para Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def viajante2():
    string = "Hey andarilho, voce sabe o melhor caminho para Nimide?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def viajante3():
    string = "Oh  seu nomadiznho, voce deve saber como chegar a Nimide, me conte"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def viajante1resp():
    string = "O senhor está certo e eu conheco o caminho, eu vou pela floresta, o segredo é seguir as cores frias."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def viajante2resp():
    string = "Que agressivo, o melhor caminho é a floresta meu senhor"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

def viajante3resp():
    string = "Mas que grosseiro, nao tenho nada pra te falar, segue o seu caminho"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return

# MENDIGO

def mendigo1():
   
    string = " (1) Pobre senhor, voce saberia me dizer o caminho para Nimide."

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return
    
def mendigo2():
   
    string = " (2) Oh mendigo, voce nao sabe o caminho para Nimide nao né?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return
      
def mendigo3():
   
    string = " (3) Hey voce ai largado na rua, se voce souber me conta, como eu chego na fronteira norte do país?"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return
  
def mendigoresp():
    string = "Oh meu senhor, eu lá tenho cara de quem viaja pra fora do reino? Eu nao sei nao"

    for ch in string:
        time.sleep(0.01)
        print(ch, end='', flush=True)

    return
