import os

os.system("cls")

import random as rd

import sys

import time


# Função para gerar números aleatórios
def dado(min, max):
    return rd.randint(min, max)


# Função para apagar linhas
def delete_last_lines(n):
    cursor_up_one = '\x1b[1A'
    erase_line = '\x1b[2K'
    for _ in range(n):
        sys.stdout.write(cursor_up_one)
        sys.stdout.write(erase_line)

# Função pra reiniciar o programa
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Essa função serve para a batalha não ocorrer toda de uma vez, ou seja, o jogador tera que avancar por conta propria
def enter():
    input('\n\u001b[37;1maperte enter para continuar\u001b[0m')
    delete_last_lines(1)
    return


# Função para dar a opcao do jogador tentar de novo ou sair do jogo
def game_over(jogador):

    if jogador["hp"] <= 0:
        print(f"\n   \u001b[37;1m\u001b[7mGAME OVER\u001b[0m\u001b[37;1m\n\nJogar novamente?\n\n(1)sim    (2)não")

        loop = True

        while loop == True:

            a = input("\n>>>\u001b[0m")

            # Reiniciar o programa
            if a == "1":
                restart_program()
                break

            # Interromper o programa, indicando a saida
            elif a == "2":
                sys.exit()

            # Repetir o input e indicar comando errado ou inexistente
            else:
                print("\nComando não reconhecido, tente novamente")
                time.sleep(2)
                delete_last_lines(4)


# Função para pausar a progressão da batalha, e dar opções para o jogador escolher
def acoes(inimigo, jogador, arma):

    loop = True

    global fugir

    global defende

    global forte

    global final

    # O while apenas serve para repetir o input caso o jogador ponha um comando não reconhecido
    while loop == True:

        print("\n\u001b[37;1mdigite 'comandos' para uma lista dos comandos")
        acao = input(">>>")
        delete_last_lines(2)
        print(f">>>{acao}\u001b[0m\n")  # Printar o comando do jogador que foi apagado

        # Checar se e possivel fugir da batalha
        if final == False:

            # Opcão do jogador fugir da batalha, encerrando-a imediatamente
            if acao == "fugir":
                fugir = True
                print(f"\n\u001b[33mVocê escapou do {inimigo.get('nome')}\u001b[0m")
                return

        # Opcão do jogador receber informações sobre si mesmo, e do oponente
        if acao == "info":
            print(f"\nVocê:\nHP {jogador['hp']}  DEF {jogador['defesa']}  FOR {jogador['força']}  DES {jogador['destreza']}  INT {jogador['inteligência']}\n\nArma:   {arma['nome']}\nAtr. {arma['atributo']}  Dano {arma['dano']}\n\n{inimigo['nome']}:\nHP {inimigo['hp']}  DEF {inimigo['defesa']}  FOR {inimigo['força']}  DES {inimigo['destreza']}  INT {inimigo['inteligência']}")

        # Se o jogador tiver escolhido fugir de uma batalha em que ele pode, nao vai chegar a esse ponto do codigo e nao vai repetir o input
        elif acao == "fugir":
            print("Você não pode fugir dessa batalha")

        # Opção do jogador usar um ataque forte, que aumenta sua força mas diminui sua defesa por um turno
        elif acao == "forte":
            forte = True
            print("\nVocê deu um ataque forte")
            return

        # Opção do jogador se defender do próximo ataque, aumentando sua defesa, mas não atacando naquela rodada
        elif acao == "defesa":
            defende = True
            print("\nVocê levanta a guarda")
            return

        # Igual a função enter()
        elif acao == "":
            return

        # Exibir os comandos possiveis
        elif acao == "comandos":
            if final == False:
                print("comandos\ninfo 'comando'\ninfo\nforte\ndefesa\nfugir\n")
            else:
                print("comandos\ninfo 'comando'\ninfo\nforte\ndefesa\n")

        # Mostrar a informacao do comando "info 'comando'"
        elif acao == "info info 'comando'":
            print("Esse comando exibe informações detalhadas sobre o comando especificado\n")

        # Mostrar a informacao do comando "comandos"
        elif acao == "info comandos":
            print("Esse comando exibe uma lista dos comandos disponíveis\n")

        # Mostrar a informacao do comando "info"
        elif acao == "info info":
            print("Esse comando exibe os atributos dos combatentes\n")

        # Mostrar a informacao do comando "forte"
        elif acao == "info forte":
            print("Esse comando determina que o próximo ataque do jogador sera um ataque forte\nO ataque forte aumenta sua força(FOR+2) mas baixa sua guarda(DEF-2)\n")

        # Mostrar a informacao do comando "defesa"
        elif acao == "info defesa":
            print("Esse comando determina que o jogador ira defender\nA defesa serve para levantar sua guarda(DEF+2) em troca de não atacar no turno\n")

        # Mostrar a informacao do comando "fugir"
        elif acao == "info fugir":
            print("Esse comando serve para escapar da batalha que o jogador se encontra no momento\n")

        # Repetir o input e indicar comando errado ou inexistente
        else:
            print("\nComando não reconhecido, tente novamente")
            time.sleep(2)
            delete_last_lines(4)


# Função para determinar a proxima acao do inimigo baseado em chance, 10% para defesa, 20% para ataque forte, 70% para ataque leve
def acao_inimigo():
    global inimigo_acao

    chance = dado(1, 10)

    if chance == 1 or chance == 2:
        inimigo_acao = 1

    elif chance == 3:
        inimigo_acao = 0


# Função para calcular o dano dado pelo jogador
def calculo_dano(d20,jogador,inimigo):

    # Checar o atributo da arma, que muda a forma que o dano e calculado
    if jogador["arma"]["atributo"] == "FOR":

        # Processo de redução da vida do inimigo
        if d20 == 1: # Caso o dado de 1, não sera somada a força e não haverá dano

            print("Seu dado deu 1")
            print('\nAtaque mal sucedido')
            enter()

        # Caso o dado de 20, procederá para um cálculo do acerto crítico
        elif d20 + jogador['força'] >= 20:

            print(f'\nSeu dado({d20}) mais sua força({jogador.get("força")}) deu {d20 + jogador["força"]}')
            print('\nVocê acertou um ataque crítico!')

            dano = int(((d20 + jogador['força'] + dado(jogador["arma"]["min"], jogador["arma"]["max"])) * 1.5) - inimigo['defesa']) # O acerto crítico ira adicionar 50% ao dado + força
            inimigo['hp'] -= dano

            # Manter a vida minima no zero, para que não mostre vida negativa
            if inimigo['hp'] < 0:
                inimigo['hp'] = 0

            print(f'\nVocê deu {dano} de dano ao inimigo!\nVida do inimigo: {inimigo.get("hp")}')
            enter()

        # Caso o dado não de vinte, mas for maior que a defesa do inimigo, procederá para o cálculo de dano comum
        elif d20 + jogador['força'] >= inimigo['defesa']:

            print(f'\nSeu dado({d20}) mais sua força({jogador.get("força")}) deu {d20 + jogador["força"]}')
            print('\nAtaque bem sucedido!')

            dano = ((d20 + jogador['força'] + dado(jogador["arma"]["min"], jogador["arma"]["max"])) - inimigo['defesa'])
            inimigo['hp'] -= dano

            # Manter a vida minima no zero, para que não mostre vida negativa
            if inimigo['hp'] < 0:
                inimigo['hp'] = 0

            print(f'\nVocê deu {dano} de dano ao inimigo!\nVida do inimigo: {inimigo.get("hp")}')
            enter()

        # Caso o dado de menor que a defesa do inimigo, não haverá dano
        else:

            print(f'\nSeu dado({d20}) mais sua força({jogador.get("força")}) deu {d20 + jogador["força"]}')
            print('\nAtaque mal sucedido')
            enter()

    elif jogador["arma"]["atributo"] == "DES":

        # Processo de redução da vida do inimigo
        # Caso o dado de 1, não sera somada a destreza e não haverá dano
        if d20 == 1:

            print("Seu dado deu 1")
            print('\nAtaque mal sucedido')
            enter()

        # Caso o dado de 20, procederá para um cálculo do acerto crítico
        elif d20 + jogador['destreza'] >= 20:

            print(f'\nSeu dado({d20}) mais sua destreza({jogador.get("destreza")}) deu {d20 + jogador["destreza"]}')
            print('\nVocê acertou um ataque crítico!')

            dano = int(((d20 + jogador['destreza'] + dado(jogador["arma"]["min"], jogador["arma"]["max"])) * 1.5) - inimigo['defesa']) # O acerto crítico ira adicionar 50% ao dado + destreza
            inimigo['hp'] -= dano

            # Manter a vida minima no zero, para que não mostre vida negativa
            if inimigo['hp'] < 0:
                inimigo['hp'] = 0

            print(f'\nVocê deu {dano} de dano ao inimigo!\nVida do inimigo: {inimigo.get("hp")}')
            enter()

        # Caso o dado não de vinte, mas for maior que a defesa do inimigo, procederá para o cálculo de dano comum
        elif d20 + jogador['destreza'] >= inimigo['defesa']:

            print(f'\nSeu dado({d20}) mais sua destreza({jogador.get("destreza")}) deu {d20 + jogador["destreza"]}')
            print('\nAtaque bem sucedido!')

            dano = ((d20 + jogador['destreza'] + dado(jogador["arma"]["min"], jogador["arma"]["max"])) - inimigo['defesa'])
            inimigo['hp'] -= dano

            # Manter a vida minima no zero, para que não mostre vida negativa
            if inimigo['hp'] < 0:
                inimigo['hp'] = 0

            print(f'\nVocê deu {dano} de dano ao inimigo!\nVida do inimigo: {inimigo.get("hp")}')
            enter()

        # Caso o dado de menor que a defesa do inimigo, não haverá dano
        else:
            print(f'\nSeu dado({d20}) mais sua destreza({jogador.get("destreza")}) deu {d20 + jogador["destreza"]}')
            print('\nAtaque mal sucedido')
            enter()


# Dicionários para as armas
mao = {"nome": "mão", "atributo": "FOR", "dano": "0-1", "min": 0, "max": 1}

adaga = {"nome": "adaga", "atributo": "DES", "dano": "1-3", "min": 1, "max": 3}


# Dicionários para atributos do jogador
Soldado = {"nome": "Soldado", 'hp': 100, 'defesa': 5, 'força': 5, 'destreza': 3, 'inteligência': 2, 'sorte': 5, 'carisma': 3, "arma": mao}       #Soldado tem     defesa media, força alta,  destreza baixa, inteligência baixa, sorte alta,  carisma media

Mercenario = {"nome": "Fernando", 'hp': 100, 'defesa': 6, 'força': 3, 'destreza': 4, 'inteligência': 5, 'sorte': 3, 'carisma': 2, "arma": mao}  #Mercenario tem  defesa alta,  força media, destreza media, inteligência alta,  sorte media, carisma baixa

Ladrao = {"nome": "Fernando", 'hp': 100, 'defesa': 4, 'força': 2, 'destreza': 5, 'inteligência': 3, 'sorte': 2, 'carisma': 5, "arma": mao}      #Ladrao tem      defesa baixa, força baixa, destreza alta,  inteligência media, sorte baixa, carisma alta


# Dicionários para atributos dos inimigos
Goblin = {"nome": "Goblin", 'hp': 85, 'defesa': 3, 'força': 1, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Esqueleto = {"nome": "Esqueleto", 'hp': 65, 'defesa': 5, 'força': 2, 'destreza': 2, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Serpente = {"nome": "Serpente", 'hp': 30, 'defesa': 2, 'força': 2, 'destreza': 5, 'inteligência': 1, 'sorte': 0, 'carisma': 0}

Urso = {"nome": "Urso", 'hp': 70, 'defesa': 2, 'força': 3, 'destreza': 1, 'inteligência': 1, 'sorte': 0, 'carisma': 0}


fugir = False

defende = False

forte = False

final = False

divisoria = '~'

divisoria2 = '/'


# Função para as batalha entre jogador e inimigo
def batalha(inimigo, jogador):
    global inimigo_acao

    global fugir

    global defende

    global forte

    if jogador["hp"] > 0:
        print(f"\n\u001b[33;1m{divisoria2 * 90}\n\nVocê entrou em uma batalha contra um {inimigo.get('nome')}!\u001b[0m")

    # O while serve para manter o ciclo dos turnos ate que alguém morra
    while (inimigo['hp'] > 0 and jogador['hp'] > 0 and fugir == False) == True:

        acao_inimigo()

        # Ver a acao do inimigo e preparar os atributos para o turno do jogador
        if inimigo_acao == 1:
            print(f'\nO {inimigo.get("nome")} prepara um ataque forte')
            inimigo["força"] += 2
            inimigo["defesa"] -= 2
            enter()

        elif inimigo_acao == 0:
            print(f'\nO {inimigo.get("nome")} levanta a guarda')
            inimigo["defesa"] += 2
            enter()

        print(f'\n\u001b[36m\n{divisoria * 90}\nSeu turno\u001b[0m')
        print("\nSua ação:\n")
        acoes(inimigo, jogador, jogador["arma"])

        # Checar se o jogador não escolheu fugir da batalha
        if fugir == False:

            # Caso o jogador tenha escolhido usar um ataque forte
            if forte == True:

                # Mudança temporária de atributos
                jogador["força"] += 2
                jogador["defesa"] -= 2

                dado_jogador = dado(1, 20)  # dado do jogador para determinar seu ataque

                calculo_dano(dado_jogador,jogador,inimigo)

                # Trazer a força do jogador de volta ao normal
                jogador["força"] -= 2

            # Caso o jogador decida se defender, não havendo cálculo de dano, apenas levando +2 de defesa para o turno do inimigo
            elif defende == True:

                jogador["defesa"] += 2

            # Caso o jogador decida apenas atacar normalmente
            else:
                print("\nVocê deu um ataque leve\n")
                dado_jogador = dado(1, 20)  # dado do jogador para determinar seu ataque

                calculo_dano(dado_jogador,jogador,inimigo)

        # Checar se o jogador decidiu fugir antes do turno do inimigo
        if fugir == False:

            # If para checar se o inimigo morreu durante o turno do jogador
            if inimigo['hp'] > 0:

                # Se o inimigo se defender pula o turno de dano dele
                if inimigo_acao == 0:
                    print(f'\n\u001b[31m\n{divisoria * 90}\nTurno do inimigo\u001b[0m')
                    print(f'\nO {inimigo.get("nome")} se defende')
                    inimigo["defesa"] -= 2

                # Caso ele nao se defenda, procede para o calculo de dano normal
                else:
                    print(f'\n\u001b[31m\n{divisoria * 90}\nTurno do inimigo\u001b[0m')
                    enter()
                    dado_inimigo = dado(1, 20)

                    # Processo de redução da vida do jogador
                    # Caso o dado de 1, não sera somada a força e não haverá dano
                    if dado_inimigo == 1:

                        print("O dado do inimigo deu 1")
                        print(f'\nO inimigo errou o ataque')
                        enter()

                    # Caso o dado de 20, procederá para um cálculo do acerto crítico
                    elif dado_inimigo + inimigo['força'] >= 20:

                        print(f'\nO dado({dado_inimigo}) mais força do inimigo({inimigo.get("força")}) deu {dado_inimigo + inimigo["força"]}')
                        print('\nVocê recebeu um ataque crítico!')

                        dano = int(((dado_inimigo + inimigo['força']) * 1.5) - jogador['defesa'])
                        jogador['hp'] -= dano

                        # Manter a vida minima no zero, para que não mostre vida negativa
                        if jogador['hp'] < 0:
                            jogador['hp'] = 0

                        print(f'\nVocê recebeu {dano} de dano!\nSua vida: {jogador.get("hp")}')
                        enter()

                    # Caso o dado não de vinte, mas for maior que a defesa do jogador, procederá para o cálculo de dano comum
                    elif dado_inimigo + inimigo['força'] >= jogador['defesa']:

                        print(f'\nO dado({dado_inimigo}) mais força do inimigo({inimigo.get("força")}) deu {dado_inimigo + inimigo["força"]}')
                        print('\nVocê recebeu um ataque!')

                        dano = ((dado_inimigo + inimigo['força']) - jogador['defesa'])
                        jogador['hp'] -= dano

                        # Manter a vida minima no zero, para que não mostre vida negativa
                        if jogador['hp'] < 0:
                            jogador['hp'] = 0

                        print(f'\nVocê recebeu {dano} de dano!\nSua vida: {jogador.get("hp")}')
                        enter()

                    else:

                        print(f'\nO dado({dado_inimigo}) mais força do inimigo({inimigo.get("força")}) deu {dado_inimigo + inimigo["força"]}')
                        print(f'\nO inimigo errou o ataque')
                        enter()

                if inimigo_acao == 1:
                    inimigo["força"] -= 2
                    inimigo["defesa"] += 2

            else:
                print(f'\nVocê derrotou  o inimigo!')

        # Trazer os atributos do jogador de volta ao normal
        if defende == True:
            jogador["defesa"] -= 2
            defende = False

        if forte == True:
            jogador["defesa"] += 2
            forte = False

        # Checar se o jogador morreu após o turno do inimigo
        if jogador['hp'] <= 0:
            print(f'\nVocê morreu')

    fugir = False


batalha(Goblin, Soldado)

game_over(Soldado)

Soldado["arma"] = adaga

game_over(Soldado)

batalha(Esqueleto, Soldado)

game_over(Soldado)

final = True

batalha(Esqueleto, Mercenario)

game_over(Mercenario)


"""
LEMBRETES:
-balanceamento dos valores
-cores para os comandos
"""
