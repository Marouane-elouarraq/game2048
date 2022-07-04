from grid_2048 import *


def read_player_command():
    move = input(
        "Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move


def read_size_grid():
    size = input("choisissez une taille pour la grille:")
    return size


#if __name__ == '__main__':
#    game_play()
#    exit(1)
