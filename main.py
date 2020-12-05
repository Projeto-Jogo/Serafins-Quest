
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

adaga = {"nome": "adaga", "atributo": "DES", "dano": "1-3", "min": 1, "max": 3}


# Dicionários para atributos dos inimigos
Goblin = {"nome": "Goblin", 'hp': 85, 'defesa': 3, 'força': 1, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Esqueleto = {"nome": "Esqueleto", 'hp': 65, 'defesa': 5, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Serpente = {"nome": "Serpente", 'hp': 30, 'defesa': 2, 'força': 2, 'destreza': 5, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Urso = {"nome": "Urso", 'hp': 70, 'defesa': 2, 'força': 3, 'destreza': 1, 'inteligência': 1, 'sorte': 0, 'carisma': 0}


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
x = 0
y = 0
while x < 1:

    # ESCOLHA DO LOCAL DE BUSCA: TAVERNA; BIBLIOTECA; BECO
    escolha_1 = input('\nProcurar informacoes:\n(1) na Taverna\n(2) na Biblioteca\n(3) no Beco')

    # TAVERNA
    if escolha_1 == '1':
        print('\n(narracao)')
        bt.enter()
        x += 1
        while y < 1:
            # ESCOLHA DA CONVERSA: BEBADO; MERETRIZ; BARTENDER
            escolha_2 = input('\nConversar com:\n(1) Bebado\n(2) Meretriz\n(3) Bartender')

            # BEBADO
            if escolha_2 == '1':
                bt.enter()
                y += 1

            # MERETRIZ
            elif escolha_2 == '2':
                bt.enter()
                y += 1

            # BARTENDER
            elif escolha_2 == '3':
                bt.enter()
                y += 1

            else:
                print('\ndigite apenas o numero')


    # BIBLIOTECA
    elif escolha_1 == '2':

        print('\n(narracao)')
        bt.enter()
        x += 1

        while y < 1:
            # ESCOLHA DE PESQUISA: BIBLIOTECARIA; LIVROS; PESSOA ESTUDANDO
            escolha_2 = input('\nProcurar com:\n(1) Bibliotecaria\n(2) Livros\n(3) Pessoa estudando')

            # BIBLIOTECARIA
            if escolha_2 == '1':
                bt.enter()
                y += 1

            # LIVROS
            elif escolha_2 == '2':
                bt.enter()
                y += 1

            # PESSOA ESTUDANDO
            elif escolha_2 == '3':
                bt.enter()
                y += 1

            else:
                print('\ndigite apenas o numero')


    # BECO
    elif escolha_1 == '3':

        print('\n(narracao)')
        bt.enter()
        x += 1

        while y < 1:
            # ESCOLHA DA CONVERSA: SABIO; MENDIGO; VIAJANTE
            escolha_2 = input('\nConversar com:\n(1) Sabio\n(2) Mendigo\n(3) Viajante')

            # SABIO
            if escolha_2 == '1':
                bt.enter()
                y += 1

            # MENDIGO
            elif escolha_2 == '2':
                bt.enter()
                y += 1

            # VIAJANTE
            elif escolha_2 == '3':
                bt.enter()
                y += 1

            else:
                print('\ndigite apenas o numero')


    else:
        print('\ndigite apenas o numero')




