 
import os
 
os.system("cls")
 
import time
 
# A maior parte das funções utilizadas foram alocadas no módulo Batalha.py, por convenção
import Batalha as bt
 
import Introducao as intro
 
import Deserto as ds
 
import Floresta as fr
 
import Final as fn
 
# INTRODUÇÃO
 
print("JOGAR Serafin's Quest")
 
bt.enter()
 
intro.introducao()
 
bt.enter()
 
# GERAÇÃO INICIAL DOS ATRIBUTOS
def atriubutos_gen():
 
    loop = True
 
    while loop:
 
        print("\u001b[37;1mEscolha seu personagem:\n (1) Soldado\n (2) Mercenário\n (3) Ladrão")
        a = input(">>>")
        bt.delete_last_lines(1)
        print(f">>>{a}\u001b[0m\n")
 
        if a == "1" or a == "2" or a == "3":
 
 
            while loop:
 
                # Dicionário da arma inicial
                mao = {"nome": "mão", "atributo": "FOR", "dano": "0-1", "min": 0, "max": 1}
 
                # Dicionários para atributos do jogador                                                                                                                                    atributos de batalha                             atributos gerais
                Soldado =    {"nome": "Soldado",    'hp': 150, 'defesa': 5, 'força': 4, 'destreza': 3, 'inteligência': 2, 'sorte': 5, 'carisma': 3, "arma": mao}  #  Soldado      defesa média, força alta,  destreza baixa, | inteligência baixa, sorte alta,  carisma média
                                                                                                                                                                  #                                                          |
                Mercenario = {"nome": "Mercenário", 'hp': 150, 'defesa': 6, 'força': 2, 'destreza': 4, 'inteligência': 5, 'sorte': 3, 'carisma': 2, "arma": mao}  #  Mercenário   defesa alta,  força baixa, destreza média, | inteligência alta,  sorte media, carisma baixa
                                                                                                                                                                  #                                                          |
                Ladrao =     {"nome": "Ladrão",     'hp': 150, 'defesa': 4, 'força': 3, 'destreza': 5, 'inteligência': 3, 'sorte': 2, 'carisma': 5, "arma": mao}  #  Ladrao       defesa baixa, força média, destreza alta,  | inteligência média, sorte baixa, carisma alta
 
                # Os personagens tem atributos bases diferentes, a geração é feita escolhendo um número aleatório entre o atributo base +- 1 ponto, e todos começam com a mão como arma
 
                if a == "1":
 
                    Soldado['defesa'] = bt.dado(4, 6)  # Por exemplo, o atributo base e 5, então irá gerar um número de 4 a 6
                    Soldado['força'] = bt.dado(3, 5)
                    Soldado['destreza'] = bt.dado(2, 4)
                    Soldado['inteligência'] = bt.dado(1, 3)
                    Soldado['sorte'] = bt.dado(4, 6)
                    Soldado['carisma'] = bt.dado(2, 4)
                    personagem = Soldado
                    # Esse 'if' e um anti-azar, ele não permite progredir se a soma dos números gerados não for maior que 19
                    if Soldado['defesa'] + Soldado['força'] + Soldado['destreza'] + Soldado['inteligência'] + Soldado['sorte'] + Soldado['carisma'] >= 19:
                        return personagem
 
                elif a == "2":
 
                    Mercenario['defesa'] = bt.dado(5, 7)
                    Mercenario['força'] = bt.dado(1, 3)
                    Mercenario['destreza'] = bt.dado(3, 5)
                    Mercenario['inteligência'] = bt.dado(4, 6)
                    Mercenario['sorte'] = bt.dado(2, 4)
                    Mercenario['carisma'] = bt.dado(1, 3)
                    personagem = Mercenario
                    if Mercenario['defesa'] + Mercenario['força'] + Mercenario['destreza'] + Mercenario['inteligência'] + Mercenario['sorte'] + Mercenario['carisma'] >= 19:
                        return personagem
 
                elif a == "3":
 
                    Ladrao['defesa'] = bt.dado(3, 5)
                    Ladrao['força'] = bt.dado(2, 4)
                    Ladrao['destreza'] = bt.dado(4, 6)
                    Ladrao['inteligência'] = bt.dado(2, 4)
                    Ladrao['sorte'] = bt.dado(1, 3)
                    Ladrao['carisma'] = bt.dado(4, 6)
                    personagem = Ladrao
                    if Ladrao['defesa'] + Ladrao['força'] + Ladrao['destreza'] + Ladrao['inteligência'] + Ladrao['sorte'] + Ladrao['carisma'] >= 19:
                        return personagem
 
            break
 
        else:
            print("\nComando não reconhecido, tente novamente")
            time.sleep(2)
            bt.delete_last_lines(4)
 
 
personagem = atriubutos_gen()
 
# Apresentação dos atributos ao jogador
print(f'\nVocê é um: {personagem.get("nome")}\nSeus atributos:\n defesa = {personagem.get("defesa")}\n força = {personagem.get("força")}\n destreza = {personagem.get("destreza")}\n inteligência = {personagem.get("inteligência")}\n sorte = {personagem.get("sorte")}\n carisma = {personagem.get("carisma")}')
 
bt.enter()
 
intro.narracaocastelo()
 
loop = True
trigger_floresta = False
trigger_deserto = False
 
# O while vai ser diversamente usado para repetir o input caso o jogador de um comando invalido
while loop:
 
    escolha_1 = ""
    escolha_2 = ""
    escolha_3 = ""
    
    while escolha_1 != "4":
        
        escolha_1 = ""
        # ESCOLHA DO LOCAL DE BUSCA: TAVERNA; BIBLIOTECA; BECO
        print('\n\u001b[37;1mProcurar informações:\n (1) na Taverna\n (2) na Biblioteca\n (3) no Beco\n (4) continuar a jornada')
        escolha_1 = input(">>>")
        bt.delete_last_lines(1)
        print(f">>>{escolha_1}\u001b[0m\n")
 
        # TAVERNA
        if escolha_1 == '1':
 
            intro.narracaotaverna()
            bt.enter()
            escolha_2 = ""
 
            while escolha_2 != "4":
 
                # ESCOLHA DA CONVERSA: BÊBADO; MERETRIZ; BARMAN
                print('\n\u001b[37;1mConversar com:\n (1) Bêbado\n (2) Meretriz\n (3) Barman\n (4) voltar')
                escolha_2 = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{escolha_2}\u001b[0m\n")
 
                # BÊBADO
                if escolha_2 == '1':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.bebado1()
                    intro.bebado2()
                    intro.bebado3()
                    print(" (4) voltar")
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.bebadoresp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.bebadoresp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.bebadoresp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "4":
                            pass
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                # MERETRIZ
                elif escolha_2 == '2':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.meretriz1()
                    intro.meretriz2()
                    intro.meretriz3()
                    print(" (4) voltar")
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.meretriz1resp()
                            trigger_floresta = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.meretriz2resp()
                            trigger_floresta = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.meretriz3resp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "4":
                            pass
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                # BARMAN
                elif escolha_2 == '3':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.barman1()
                    intro.barman2()
                    intro.barman3()
                    print(" (4) voltar")
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.barman1resp()
                            trigger_deserto = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.barman2resp()
                            trigger_deserto = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.barman3resp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "4":
                            pass
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                elif escolha_2 == "4":
                    pass
 
                else:
                    print("\nComando não reconhecido, tente novamente")
                    time.sleep(2)
                    bt.delete_last_lines(4)
 
        # BIBLIOTECA
        elif escolha_1 == '2':
 
            intro.narracaobiblioteca()
            bt.enter()
            escolha_2 = ""
 
            while escolha_2 != "4":
 
                escolha_2 = ""
                # ESCOLHA DE PESQUISA: BIBLIOTECARIA; LIVROS; ESTUDANTE
                print('\n\u001b[37;1mPesquisar com:\n (1) Bibliotecária\n (2) Livros\n (3) Estudante\n (4) voltar')
                escolha_2 = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{escolha_2}\u001b[0m\n")
 
                # BIBLIOTECÁRIA
                if escolha_2 == '1':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.bibliotecaria1()
                    intro.bibliotecaria2()
                    intro.bibliotecaria3()
                    print(" (4) voltar")
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
 
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.bibliotecaria1resp()
                            trigger_deserto = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.bibliotecaria2resp()
                            trigger_deserto = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.bibliotecaria3resp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "4":
                            pass
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                # LIVROS
                elif escolha_2 == '2':
 
                    escolha_3 = ""
                    intro.livro()
 
                # ESTUDANTE
                elif escolha_2 == '3':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.estudante1()
                    intro.estudante2()
                    intro.estudante3()
                    print(" (4) voltar")
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
 
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.estudante1resp()
                            trigger_deserto = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.estudante2resp()
                            trigger_deserto = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.estudante3resp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "4":
                            pass
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                elif escolha_2 == "4":
                    pass
 
                else:
                    print("\nComando não reconhecido, tente novamente")
                    time.sleep(2)
                    bt.delete_last_lines(4)
 
        # BECO
        elif escolha_1 == '3':
 
            intro.narracaobeco()
            bt.enter()
            escolha_2 = ""
 
            while escolha_2 != "4":
 
                escolha_2 = ""
                # ESCOLHA DA CONVERSA: SÁBIO; MENDIGO; VIAJANTE
                print('\n\u001b[37;1mConversar com:\n (1) Sábio\n (2) Mendigo\n (3) Viajante\n (4) voltar')
                escolha_2 = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{escolha_2}\u001b[0m\n")
 
                # SABIO
                if escolha_2 == '1':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.sabio1()
                    intro.sabio2()
                    intro.sabio3()
                    print(" (4) voltar")
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
 
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.sabio1resp()
                            trigger_floresta = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.sabio2resp()
                            trigger_floresta = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.sabio3resp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "4":
                            pass
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                # MENDIGO
                elif escolha_2 == '2':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.mendigo1()
                    intro.mendigo2()
                    intro.mendigo3()
                    print(" (4) voltar")
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
 
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.mendigoresp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.mendigoresp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.mendigoresp()
                            bt.enter()
                            break
 
                        elif escolha_3 == "4":
                            pass
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                # VIAJANTE
                elif escolha_2 == '3':
 
                    print("\u001b[37;1m","")
                    escolha_3 = ""
                    intro.viajante1()
                    intro.viajante2()
                    intro.viajante3()
 
                    while escolha_3 != "4":
 
                        escolha_3 = ""
 
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")
 
                        if escolha_3 == "1":
                            intro.viajante1resp()
                            trigger_floresta = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "2":
                            intro.viajante2resp()
                            trigger_floresta = True
                            bt.enter()
                            break
 
                        elif escolha_3 == "3":
                            intro.viajante3resp()
                            bt.enter()
                            break
 
                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)
 
                elif escolha_2 == "4":
                    pass
 
                else:
                    print("\nComando não reconhecido, tente novamente")
                    time.sleep(2)
                    bt.delete_last_lines(4)
 
        elif escolha_1 == "4":
            print("Voce sai em direção a sua jornada")
 
        else:
            print("\nComando não reconhecido, tente novamente")
            time.sleep(2)
            bt.delete_last_lines(4)
 
    if trigger_deserto == True and trigger_floresta == True:
 
        while loop:
 
            print("\n\u001b[37;1m (1) Seguir pelo deserto\n (2) Seguir pela floresta")
            caminho = input(">>>")
            bt.delete_last_lines(1)
            print(f">>>{caminho}\u001b[0m\n")
 
            if caminho == "1":
 
                ds.Deserto(personagem)
                break
 
            elif caminho == "2":
 
                fr.floresta(personagem)
                break
 
            else:
                print("\nComando não reconhecido, tente novamente")
                time.sleep(2)
                bt.delete_last_lines(4)
 
        break
 
    elif trigger_deserto:
 
        #print(historinha)
        ds.Deserto(personagem)
        break
 
    elif trigger_floresta:
 
        #print(historinha)
        fr.floresta(personagem)
        break
 
    else:
        print("\nVocê não sabe aonde ir, então retorna à cidade para buscar mais informações")
 
fn.final(personagem)
 
 

