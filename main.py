
import random as rd

import os

os.system("cls")

import sys

import time

import Batalha as bt

import Floresta as fl

import Deserto as ds



# Função para gerar números aleatórios
def dado(min, max):
    return rd.randint(min, max)


# BOTAO PARA PROGREDIR
def enter():
    input('\n\u001b[37;1maperte enter para continuar\u001b[0m')
    delete_last_lines(1)
    return

# Função para apagar linhas
def delete_last_lines(n):
    cursor_up_one = '\x1b[1A'
    erase_line = '\x1b[2K'
    for _ in range(n):
        sys.stdout.write(cursor_up_one)
        sys.stdout.write(erase_line)

# Dicionários para as armas
mao = {"nome": "mão", "atributo": "FOR", "dano": "0-1", "min": 0, "max": 1}

adaga = {"nome": "adaga", "atributo": "DES", "dano": "1-3", "min": 1, "max": 3}


# Dicionários para atributos do jogador
Soldado = {"nome": "Soldado", 'hp': 100, 'defesa': 5, 'força': 4, 'destreza': 3, 'inteligência': 2, 'sorte': 5, 'carisma': 3, "arma": mao}        #Soldado tem     defesa media, força alta,  destreza baixa, inteligência baixa, sorte alta,  carisma media

Mercenario = {"nome": "Mercenário", 'hp': 100, 'defesa': 6, 'força': 3, 'destreza': 4, 'inteligência': 5, 'sorte': 2, 'carisma': 2, "arma": mao}  #Mercenario tem  defesa alta,  força media, destreza media, inteligência alta,  sorte baixa, carisma baixa

Ladrao = {"nome": "Ladrão", 'hp': 100, 'defesa': 4, 'força': 2, 'destreza': 5, 'inteligência': 3, 'sorte': 3, 'carisma': 5, "arma": mao}          #Ladrao tem      defesa baixa, força baixa, destreza alta,  inteligência media, sorte media, carisma alta


# Dicionários para atributos dos inimigos
Goblin = {"nome": "Goblin", 'hp': 85, 'defesa': 3, 'força': 1, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Esqueleto = {"nome": "Esqueleto", 'hp': 65, 'defesa': 5, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Serpente = {"nome": "Serpente", 'hp': 30, 'defesa': 2, 'força': 2, 'destreza': 5, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Urso = {"nome": "Urso", 'hp': 70, 'defesa': 2, 'força': 3, 'destreza': 1, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

personagem = ""

# INTRODUCAO

print('JOGAR (nome do jogo)')

enter()

# HISTORIA DE INTRODUCAO AO JOGO
print('(historia de introducao)')

enter()

# GERACAO INICIAL DOS ATRIBUTOS
def atributos_gen():

    global personagem

    loop = True

    a = dado(1, 3)

    Soldado = {"nome": "Soldado", 'hp': 100, 'defesa': 5, 'força': 4, 'destreza': 3, 'inteligência': 2, 'sorte': 5, 'carisma': 3, "arma": mao}        #Soldado tem     defesa media, força alta,  destreza baixa, inteligência baixa, sorte alta,  carisma media

    Mercenario = {"nome": "Mercenário", 'hp': 100, 'defesa': 6, 'força': 3, 'destreza': 4, 'inteligência': 5, 'sorte': 2, 'carisma': 2, "arma": mao}  #Mercenario tem  defesa alta,  força media, destreza media, inteligência alta,  sorte baixa, carisma baixa

    Ladrao = {"nome": "Ladrão", 'hp': 100, 'defesa': 4, 'força': 2, 'destreza': 5, 'inteligência': 3, 'sorte': 3, 'carisma': 5, "arma": mao}          #Ladrao tem      defesa baixa, força baixa, destreza alta,  inteligência media, sorte media, carisma alta

        if a == 1:
            Soldado['defesa'] = dado(4,6)
            Soldado['força'] = dado(3,5)
            Soldado['destreza'] = dado(2,4)
            Soldado['inteligência'] = dado(1,3)
            Soldado['sorte'] = dado(4,6)
            Soldado['carisma'] = dado(2,4)
            if Soldado['defesa'] + Soldado['força'] + Soldado['destreza'] + Soldado['inteligência'] + Soldado['sorte'] + Soldado['carisma'] >= 19:
                break
            personagem = Soldado

        elif a == 2:
            Mercenario['defesa'] = dado(5,7)
            Mercenario['força'] = dado(2,4)
            Mercenario['destreza'] = dado(3,5)
            Mercenario['inteligência'] = dado(4,6)
            Mercenario['sorte'] = dado(1,3)
            Mercenario['carisma'] = dado(1,3)
            if Mercenario['defesa'] + Mercenario['força'] + Mercenario['destreza'] + Mercenario['inteligência'] + Mercenario['sorte'] + Mercenario['carisma'] >= 19:
                break
            personagem = Mercenario

        elif a == 3:
            Ladrao['defesa'] = dado(3,5)
            Ladrao['força'] = dado(1,3)
            Ladrao['destreza'] = dado(4,6)
            Ladrao['inteligência'] = dado(2,4)
            Ladrao['sorte'] = dado(2,4)
            Ladrao['carisma'] = dado(4,6)
            if Ladrao['defesa'] + Ladrao['força'] + Ladrao['destreza'] + Ladrao['inteligência'] + Ladrao['sorte'] + Ladrao['carisma'] >= 19:
                break
            personagem = Ladrao
        
    return personagem

#personagem = atriubutos_gen()


# APRESENTACAO DOS ATRIBUTOS AO JOGADOR
print(f'\nVoce vai jogar de {personagem["nome"]}\nSeus atributos:\n defesa = {personagem["defesa"]}\n força = {personagem["força"]}\n destreza = {personagem["destreza"]}\n inteligência = {personagem["inteligência"]}\n sorte = {personagem["sorte"]}\n carisma = {personagem["carisma"]}')

enter()

bt.batalha(Goblin, personagem)

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
        enter()
        x += 1
        while y < 1:
            # ESCOLHA DA CONVERSA: BEBADO; MERETRIZ; BARTENDER
            escolha_2 = input('\nConversar com:\n(1) Bebado\n(2) Meretriz\n(3) Bartender')

            # BEBADO
            if escolha_2 == '1':
                enter()
                y += 1

                # MERETRIZ
            elif escolha_2 == '2':
                enter()
                y += 1

            # BARTENDER
            elif escolha_2 == '3':
                enter()
                y += 1
            else:
                print('\ndigite apenas o numero')


    # BIBLIOTECA
    elif escolha_1 == '2':
        print('\n(narracao)')
        enter()
        x += 1
        while y < 1:
            # ESCOLHA DE PESQUISA: BIBLIOTECARIA; LIVROS; PESSOA ESTUDANDO
            escolha_2 = input('\nProcurar com:\n(1) Bibliotecaria\n(2) Livros\n(3) Pessoa estudando')

            # BIBLIOTECARIA
            if escolha_2 == '1':
                enter()
                y += 1

            # LIVROS
            elif escolha_2 == '2':
                enter()
                y += 1

            # PESSOA ESTUDANDO
            elif escolha_2 == '3':
                enter()
                y += 1
            else:
                print('\ndigite apenas o numero')


    # BECO
    elif escolha_1 == '3':
        print('\n(narracao)')
        enter()
        x += 1
        while y < 1:
            # ESCOLHA DA CONVERSA: SABIO; MENDIGO; VIAJANTE
            escolha_2 = input('\nConversar com:\n(1) Sabio\n(2) Mendigo\n(3) Viajante')

            # SABIO
            if escolha_2 == '1':
                enter()
                y += 1

            # MENDIGO
            elif escolha_2 == '2':
                enter()
                y += 1

            # VIAJANTE
            elif escolha_2 == '3':
                enter()
                y += 1
            else:
                print('\ndigite apenas o numero')


    else:
        print('\ndigite apenas o numero')







