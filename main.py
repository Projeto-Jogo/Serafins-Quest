
import os

os.system("cls")

import time

# A maior parte das funcoes utilizadas foram alocadas no modulo Batalha.py, por convencao
import Batalha as bt

import Introducao as intro

import Deserto as ds

import Floresta_1 as fr

import Final as fn

# INTRODUCAO

print('JOGAR (nome do jogo)')

bt.enter()

# HISTORIA DE INTRODUCAO AO JOGO
print('(historia de introducao)')

bt.enter()


# GERACAO INICIAL DOS ATRIBUTOS
def atriubutos_gen():

    loop = True

    while loop == True:

        print("\u001b[37;1mEscolha seu personagem:\n(1) Soldado\n(2) Mercenario\n(3) Ladrao")
        a = input(">>>")
        bt.delete_last_lines(1)
        print(f">>>{a}\u001b[0m\n")

        if a == "1" or a == "2" or a == "3":


            while loop == True:

                # Dicionários para atributos do jogador                                                                                                                                    atributos de batalha                             atributos gerais
                Soldado =    {"nome": "Soldado",    'hp': 100, 'defesa': 5, 'força': 4, 'destreza': 3, 'inteligência': 2, 'sorte': 5, 'carisma': 3,"arma": mao}  #  Soldado      defesa media, força alta,  destreza baixa, | inteligência baixa, sorte alta,  carisma media
                                                                                                                                                                 #                                                          |
                Mercenario = {"nome": "Mercenário", 'hp': 100, 'defesa': 6, 'força': 2, 'destreza': 4, 'inteligência': 5, 'sorte': 3, 'carisma': 2,"arma": mao}  #  Mercenario   defesa alta,  força baixa, destreza media, | inteligência alta,  sorte media, carisma baixa
                                                                                                                                                                 #                                                          |
                Ladrao =     {"nome": "Ladrão",     'hp': 100, 'defesa': 4, 'força': 3, 'destreza': 5, 'inteligência': 3, 'sorte': 2, 'carisma': 5,"arma": mao}  #  Ladrao       defesa baixa, força media, destreza alta,  | inteligência media, sorte baixa, carisma alta

                # Os personagens tem atributos bases diferentes, a geracao e feita escolhendo um numero aleatorio entre o atributo base +- 1 ponto, e todos comecam com a mao como arma

                if a == "1":

                    Soldado['defesa'] = bt.dado(4,6)  # Por exemplo, o atributo base e 5, entao ira gerar um numero de 4 a 6
                    Soldado['força'] = bt.dado(3,5)
                    Soldado['destreza'] = bt.dado(2,4)
                    Soldado['inteligência'] = bt.dado(1,3)
                    Soldado['sorte'] = bt.dado(4,6)
                    Soldado['carisma'] = bt.dado(2,4)
                    personagem = Soldado
                    # Esse 'if' e um anti-azar, ele nao permite progredir se a soma dos numeros gerados nao for maior que 19
                    if Soldado['defesa'] + Soldado['força'] + Soldado['destreza'] + Soldado['inteligência'] + Soldado['sorte'] + Soldado['carisma'] >= 19:
                        return personagem

                elif a == "2":

                    Mercenario['defesa'] = bt.dado(5,7)
                    Mercenario['força'] = bt.dado(1,3)
                    Mercenario['destreza'] = bt.dado(3,5)
                    Mercenario['inteligência'] = bt.dado(4,6)
                    Mercenario['sorte'] = bt.dado(2,4)
                    Mercenario['carisma'] = bt.dado(1,3)
                    personagem = Mercenario
                    if Mercenario['defesa'] + Mercenario['força'] + Mercenario['destreza'] + Mercenario['inteligência'] + Mercenario['sorte'] + Mercenario['carisma'] >= 19:
                        return personagem

                elif a == "3":

                    Ladrao['defesa'] = bt.dado(3,5)
                    Ladrao['força'] = bt.dado(2,4)
                    Ladrao['destreza'] = bt.dado(4,6)
                    Ladrao['inteligência'] = bt.dado(2,4)
                    Ladrao['sorte'] = bt.dado(1,3)
                    Ladrao['carisma'] = bt.dado(4,6)
                    personagem = Ladrao
                    if Ladrao['defesa'] + Ladrao['força'] + Ladrao['destreza'] + Ladrao['inteligência'] + Ladrao['sorte'] + Ladrao['carisma'] >= 19:
                        return personagem
            break

personagem = atriubutos_gen()


# Apresentacao dos atributos ao jogador
print(f'\nVoce vai jogar de {personagem.get("nome")}\nSeus atributos:\n defesa = {personagem.get("defesa")}\n força = {personagem.get("força")}\n destreza = {personagem.get("destreza")}\n inteligência = {personagem.get("inteligência")}\n sorte = {personagem.get("sorte")}\n carisma = {personagem.get("carisma")}')

bt.enter()


# PRIMEIRA PARTE: CASTELO

print('\n(narracao)')


loop = True
escolha_1 = ""
escolha_2 = ""
escolha_3 = ""

# O while vai ser diversamente usado para repetir o input caso o jogador de um comando invalido
while loop:

    while escolha_1 != "4":

        # ESCOLHA DO LOCAL DE BUSCA: TAVERNA; BIBLIOTECA; BECO
        print('\n\u001b[37;1mProcurar informacoes:\n (1) na Taverna\n (2) na Biblioteca\n (3) no Beco\n (4) continuar a jornada')
        escolha_1 = input(">>>")
        bt.delete_last_lines(1)
        print(f">>>{escolha_1}\u001b[0m\n")

        # TAVERNA
        if escolha_1 == '1':

            print('\n(narracao)')
            bt.enter()

            while escolha_2 != "4":

                # ESCOLHA DA CONVERSA: BEBADO; MERETRIZ; BARTENDER
                print('\n\u001b[37;1mConversar com:\n (1) Bebado\n (2) Meretriz\n (3) Bartender\n (4) voltar')
                escolha_2 = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{escolha_2}\u001b[0m\n")

                # BEBADO
                if escolha_2 == '1':

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.bebado_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.bebado_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.bebado_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                # MERETRIZ
                elif escolha_2 == '2':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.meretriz_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.meretriz_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.meretriz_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                # BARTENDER
                elif escolha_2 == '3':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.bartender_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.bartender_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.bartender_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                else:
                    print("\nComando não reconhecido, tente novamente")
                    time.sleep(2)
                    bt.delete_last_lines(4)

        # BIBLIOTECA
        elif escolha_1 == '2':

            print('\n(narracao)')
            bt.enter()

            while loop:

                # ESCOLHA DE PESQUISA: BIBLIOTECARIA; LIVROS; ESTUDANTE
                print('\n\u001b[37;1mPesquisar com:\n (1) Bibliotecaria\n (2) Livros\n (3) Estudante\n (4) voltar')
                escolha_2 = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{escolha_2}\u001b[0m\n")

                # BIBLIOTECARIA
                if escolha_2 == '1':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.bibliotecaria_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.bibliotecaria_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.bibliotecaria_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                # LIVROS
                elif escolha_2 == '2':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.livros_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.livros_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.livros_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                # PESSOA ESTUDANDO
                elif escolha_2 == '3':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.estudante_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.estudante_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.estudante_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                else:
                    print("\nComando não reconhecido, tente novamente")
                    time.sleep(2)
                    bt.delete_last_lines(4)

        # BECO
        elif escolha_1 == '3':

            print('\n(narracao)')
            bt.enter()

            while loop:

                # ESCOLHA DA CONVERSA: SABIO; MENDIGO; VIAJANTE
                print('\n\u001b[37;1mConversar com:\n (1) Sabio\n (2) Mendigo\n (3) Viajante\n (4) voltar')
                escolha_2 = input(">>>")
                bt.delete_last_lines(1)
                print(f">>>{escolha_2}\u001b[0m\n")

                # SABIO
                if escolha_2 == '1':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.sabio_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.sabio_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.sabio_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                # MENDIGO
                elif escolha_2 == '2':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.mendigo_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.mendigo_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.mendigo_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                # VIAJANTE
                elif escolha_2 == '3':

                    # print as opcoes de fala do jogador

                    while escolha_3 != "4":

                        #print ocpcoes de fala do jogador
                        escolha_3 = input(">>>")
                        bt.delete_last_lines(1)
                        print(f">>>{escolha_3}\u001b[0m\n")

                        if escolha_3 == "1":
                            intro.viajante_1
                            bt.enter()

                        elif escolha_3 == "2":
                            intro.viajente_2
                            bt.enter()

                        elif escolha_3 == "3":
                            intro.viajante_3
                            bt.enter()

                        else:
                            print("\nComando não reconhecido, tente novamente")
                            time.sleep(2)
                            bt.delete_last_lines(4)

                else:
                    print("\nComando não reconhecido, tente novamente")
                    time.sleep(2)
                    bt.delete_last_lines(4)

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
                ds.deserto()
                break

            elif caminho == "2":
                fr.floresta(personagem)
                break

            else:
                print("\nComando não reconhecido, tente novamente")
                time.sleep(2)
                bt.delete_last_lines(4)

        break

    elif trigger_deserto == True:

    #   print(historinha)
        ds.deserto()
        break

    elif trigger_floresta == True:

    #   print(historinha)
        fr.floresta(personagem)
        break

    else:
        print("voce nao sabe aonde ir, entao retorna a cidade para buscar informacoes")

fn.final(personagem)
