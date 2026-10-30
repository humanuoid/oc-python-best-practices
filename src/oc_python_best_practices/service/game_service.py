"""Service de gestion du jeu (distribution, remise à zéro)."""

from oc_python_best_practices.model.deck import Deck
from oc_python_best_practices.model.player import Player


class GameService:
    """Distribution des cartes et remise à zéro du jeu."""

    MAX_PLAYERS = 2

    @staticmethod
    def distribute(deck: Deck, players: list[Player]) -> None:
        """Distribue une carte face cachée à chaque joueur.

        Args:
            deck: Le jeu de cartes.
            players: Les joueurs recevant une carte.
        """
        for player in players:
            card = deck.pop()
            card.face_down = True
            player.hand.append(card)

    @staticmethod
    def reset(deck: Deck, players: list[Player]) -> None:
        """Remet les cartes des mains dans le deck et vide les mains.

        Args:
            deck: Le jeu de cartes à reconstituer.
            players: Les joueurs dont la main est vidée.
        """
        for player in players:
            deck.extend(player.hand.cards)
            player.hand.clear()
