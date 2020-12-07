
import random as rd

import os

os.system("cls")

import sys

import time

import Batalha as bt

import Introducao as intro

import Deserto as ds

import Floresta as fr

import Final as fn




# Dicionários para as armas
mao = {"nome": "mão", "atributo": "FOR", "dano": "0-1", "min": 0, "max": 1}

adaga = {"nome": "adaga", "atributo": "DES", "dano": "2-4", "min": 2, "max": 4}

chicote = {"nome": "chicote", "atributo": "DES", "dano": "2-4", "min": 2, "max": 4}

espada_longa = {"nome": "espada longa", "atributo": "FOR", "dano": "3-5", "min": 3, "max": 5}


# Dicionários para atributos dos inimigos                                                Ordem de encontro
Serpente =         {"nome": "Serpente",              'hp': 30,  'defesa': 2, 'força': 2} # 1                       level up

Urso =             {"nome": "Urso",                  'hp': 45,  'defesa': 3, 'força': 3} # 1                       level up

Goblin =           {"nome": "Goblin",                'hp': 55,  'defesa': 4, 'força': 3} # 2

Seguranca =        {"nome": "Segurança",             'hp': 60,  'defesa': 5, 'força': 3} # 3

Esqueleto_1 =      {"nome": "Esqueleto",             'hp': 65,  'defesa': 4, 'força': 2} # 4

Esqueleto_2 =      {"nome": "Esqueleto",             'hp': 35,  'defesa': 6, 'força': 5} # 5

Troll =            {"nome": "Troll",                 'hp': 70,  'defesa': 5, 'força': 2} # 4

Escorpiao_enorme = {"nome": "Escorpião enorme",      'hp': 60,  'defesa': 4, 'força': 3} # 6

Morto_vivo =       {"nome": "Morto vivo",            'hp': 45,  'defesa': 2, 'força': 5} # 7                       level up

Javali =           {"nome": "Javali",                'hp': 65,  'defesa': 5, 'força': 3} # 5

Boss_1 =           {"nome": "Guardião do relicario", 'hp': 75,  'defesa': 5, 'força': 4} # 8

Boss_2 =           {"nome": "Guardião renascido",    'hp': 100, 'defesa': 6, 'força': 5} # 9


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

        a = input("Escolha seu personagem:\n(1) Soldado\n(2) Mercenario\n(3) Ladrao")

        if a == "1" or a == "2" or a == "3":


            while loop == True:

                # Dicionários para atributos do jogador                                                                                                                                    atributos de batalha                             atributos gerais
                Soldado =    {"nome": "Soldado",    'hp': 100, 'defesa': 5, 'força': 4, 'destreza': 3, 'inteligência': 2, 'sorte': 5, 'carisma': 3,"arma": mao}  #  Soldado      defesa media, força alta,  destreza baixa, | inteligência baixa, sorte alta,  carisma media
                                                                                                                                                                 #                                                          |
                Mercenario = {"nome": "Mercenário", 'hp': 100, 'defesa': 6, 'força': 2, 'destreza': 4, 'inteligência': 5, 'sorte': 3, 'carisma': 2,"arma": mao}  #  Mercenario   defesa alta,  força baixa, destreza media, | inteligência alta,  sorte media, carisma baixa
                                                                                                                                                                 #                                                          |
                Ladrao =     {"nome": "Ladrão",     'hp': 100, 'defesa': 4, 'força': 3, 'destreza': 5, 'inteligência': 3, 'sorte': 2, 'carisma': 5,"arma": mao}  #  Ladrao       defesa baixa, força media, destreza alta,  | inteligência media, sorte baixa, carisma alta

                if a == "1":

                    Soldado['defesa'] = bt.dado(4,6)
                    Soldado['força'] = bt.dado(3,5)
                    Soldado['destreza'] = bt.dado(2,4)
                    Soldado['inteligência'] = bt.dado(1,3)
                    Soldado['sorte'] = bt.dado(4,6)
                    Soldado['carisma'] = bt.dado(2,4)
                    personagem = Soldado
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


# APRESENTACAO DOS ATRIBUTOS AO JOGADOR
print(f'\nVoce vai jogar de {personagem.get("nome")}\nSeus atributos:\n defesa = {personagem.get("defesa")}\n força = {personagem.get("força")}\n destreza = {personagem.get("destreza")}\n inteligência = {personagem.get("inteligência")}\n sorte = {personagem.get("sorte")}\n carisma = {personagem.get("carisma")}')

bt.enter()


# PRIMEIRA PARTE: CASTELO

print('\n(narracao)')

# O WHILE SERVE PARA REPETIR A PERGUNTA AO JOGADOR CASO ELE NAO TENHA ESCOLHIDO DIREITO
loop = True
while loop:

    # ESCOLHA DO LOCAL DE BUSCA: TAVERNA; BIBLIOTECA; BECO
    escolha_1 = input('\nProcurar informacoes:\n(1) na Taverna\n(2) na Biblioteca\n(3) no Beco')

    # TAVERNA
    if escolha_1 == '1':

        print('\n(narracao)')
        bt.enter()

        while loop:

            # ESCOLHA DA CONVERSA: BEBADO; MERETRIZ; BARTENDER
            escolha_2 = input('\nConversar com:\n(1) Bebado\n(2) Meretriz\n(3) Bartender')

            # BEBADO
            if escolha_2 == '1':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.bebado_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.bebado_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.bebado_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            # MERETRIZ
            elif escolha_2 == '2':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.meretriz_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.meretriz_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.meretriz_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            # BARTENDER
            elif escolha_2 == '3':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.bartender_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.bartender_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.bartender_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            else:
                print("\nComando não reconhecido, tente novamente")
                time.sleep(2)
                bt.delete_last_lines(4)

        break

    # BIBLIOTECA
    elif escolha_1 == '2':

        print('\n(narracao)')
        bt.enter()

        while loop:

            # ESCOLHA DE PESQUISA: BIBLIOTECARIA; LIVROS; PESSOA ESTUDANDO
            escolha_2 = input('\nProcurar com:\n(1) Bibliotecaria\n(2) Livros\n(3) Pessoa estudando')

            # BIBLIOTECARIA
            if escolha_2 == '1':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.bibliotecaria_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.bibliotecaria_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.bibliotecaria_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            # LIVROS
            elif escolha_2 == '2':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.livros_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.livros_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.livros_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            # PESSOA ESTUDANDO
            elif escolha_2 == '3':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.estudante_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.estudante_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.estudante_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            else:
                print("\nComando não reconhecido, tente novamente")
                time.sleep(2)
                bt.delete_last_lines(4)
        break

    # BECO
    elif escolha_1 == '3':

        print('\n(narracao)')
        bt.enter()

        while loop:

            # ESCOLHA DA CONVERSA: SABIO; MENDIGO; VIAJANTE
            escolha_2 = input('\nConversar com:\n(1) Sabio\n(2) Mendigo\n(3) Viajante')

            # SABIO
            if escolha_2 == '1':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.sabio_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.sabio_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.sabio_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            # MENDIGO
            elif escolha_2 == '2':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.mendigo_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.mendigo_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.mendigo_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            # VIAJANTE
            elif escolha_2 == '3':

                # print as opcoes de fala do jogador

                while loop:

                    escolha_3 = input(">>>")

                    if escolha_3 == "1":
                        intro.viajante_1
                        bt.enter()
                        break

                    elif escolha_3 == "2":
                        intro.viajente_2
                        bt.enter()
                        break

                    elif escolha_3 == "3":
                        intro.viajante_3
                        bt.enter()
                        break

                    else:
                        print("\nComando não reconhecido, tente novamente")
                        time.sleep(2)
                        bt.delete_last_lines(4)

            else:
                print("\nComando não reconhecido, tente novamente")
                time.sleep(2)
                bt.delete_last_lines(4)
        break

    else:
        print("\nComando não reconhecido, tente novamente")
        time.sleep(2)
        bt.delete_last_lines(4)
