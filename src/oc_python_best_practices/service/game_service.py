"""Service de gestion du jeu (joueurs, distribution)."""

from oc_python_best_practices.model.deck import Deck
from oc_python_best_practices.model.player import Player

MAX_PLAYERS = 2


def create_players(names: list[str]) -> list[Player]:
    """Crée les joueurs à partir d'une liste de noms.

    Args:
        names: Les noms des joueurs.

    Returns:
        La liste des joueurs créés.
    """
    players = []
    for name in names:
        players.append(Player(name=name))

    return players


def distribute_cards(deck: Deck, players: list[Player]) -> None:
    """Distribue une carte face cachée à chaque joueur.

    Args:
        deck: Le jeu de cartes.
        players: Les joueurs recevant une carte.
    """
    for player in players:
        card = deck.pop()
        card.face_down = True
        player.hand.append(card)


def elect_winner(winner: Player) -> None:
    """Incrémente le score du vainqueur d'une manche.

    Args:
        winner: Le joueur qui remporte la manche.
    """
    winner.score += 1


def rank_players(players: list[Player]) -> list[Player]:
    """Classe les joueurs par score décroissant.

    Args:
        players: Les joueurs à classer.

    Returns:
        La liste des joueurs triée du meilleur au moins bon score.
    """

    return sorted(players, key=lambda p: p.score, reverse=True)


def get_final_winner(players: list[Player]) -> Player:
    """Retourne le vainqueur final (meilleur score).

    Args:
        players: Les joueurs en fin de partie.

    Returns:
        Le joueur avec le plus de points.
    """

    return rank_players(players)[0]


def reveal_cards(players: list[Player]) -> None:
    """Retourne les cartes des joueurs (face visible).

    Args:
        players: Les joueurs dont on retourne la carte.
    """
    for player in players:
        player.hand[0].face_down = False


def reset_game(deck: Deck, players: list[Player]) -> None:
    """Remet les cartes des mains dans le deck et vide les mains.

    Args:
        deck: Le jeu de cartes à reconstituer.
        players: Les joueurs dont la main est vidée.
    """
    for player in players:
        deck.extend(player.hand)
        player.hand.clear()
