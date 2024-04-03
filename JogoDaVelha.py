# Jogo da Velha

# Tabuleiro
tabuleiro = [' '] * 9

# Jogador atual (X ou O)
jogador_atual = 'X'

# Função para exibir o tabuleiro


def exibir_tabuleiro():
    print('-------------')
    print('|', tabuleiro[0], '|', tabuleiro[1], '|', tabuleiro[2], '|')
    print('-------------')
    print('|', tabuleiro[3], '|', tabuleiro[4], '|', tabuleiro[5], '|')
    print('-------------')
    print('|', tabuleiro[6], '|', tabuleiro[7], '|', tabuleiro[8], '|')
    print('-------------')

# Função para verificar se há um vencedor


def verificar_vencedor(jogador):
    # Verificação das linhas
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == jogador) or \
       (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == jogador) or \
       (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == jogador):
        return True
    # Verificação das colunas
    elif (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == jogador) or \
         (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == jogador) or \
         (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == jogador):
        return True
    # Verificação das diagonais
    elif (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador) or \
         (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador):
        return True
    else:
        return False

# Loop principal do jogo


while True:
    exibir_tabuleiro()

    # Obter a jogada do jogador
    jogada = int(input("Digite a posição de 1 a 9 para fazer a sua jogada: ")) - 1

    # Verificar se a jogada é válida
    if tabuleiro[jogada] == ' ':
        tabuleiro[jogada] = jogador_atual
    else:
        print("Jogada inválida. Por favor, escolha uma posição vazia.")

    # Verificar se há um vencedor
    if verificar_vencedor(jogador_atual):
        exibir_tabuleiro()
        print("O jogador", jogador_atual, "venceu!")
        break

    # Verificar se houve um empate
    if ' ' not in tabuleiro:
        exibir_tabuleiro()
        print("O jogo terminou em empate!")
        break

    # Alternar para o próximo jogador
    if jogador_atual == 'X':
        jogador_atual = 'O'
    else:
        jogador_atual = 'X'
        