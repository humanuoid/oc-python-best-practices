"""Service de création et de mélange du jeu de cartes."""

import random

from oc_python_best_practices.config.ranks import RANKS
from oc_python_best_practices.config.suits import SUITS
from oc_python_best_practices.model.card import Card
from oc_python_best_practices.model.deck import Deck


class DeckService:
    """Création et mélange du jeu de cartes."""

    @staticmethod
    def create() -> Deck:
        """Crée un jeu de 52 cartes (toutes les combinaisons rang/couleur).

        Returns:
            Le jeu de cartes créé (non mélangé).
        """
        deck = Deck()
        for rank in RANKS:
            for suit in SUITS:
                deck.append(Card(rank=rank, suit=suit))

        return deck

    @staticmethod
    def shuffle(deck: Deck) -> None:
        """Mélange le jeu de cartes aléatoirement.

        Args:
            deck: Le jeu de cartes à mélanger.
        """
        random.shuffle(deck)
