"""Modèle représentant un jeu de 52 cartes."""

import random

from oc_python_best_practices.config.ranks import RANKS
from oc_python_best_practices.config.suits import SUITS
from oc_python_best_practices.model.card import Card


class Deck(list):
    """Un jeu de 52 cartes, généré puis mélangé aléatoirement."""

    def __init__(self) -> None:
        """Crée toutes les combinaisons rang/couleur et les mélange."""
        super().__init__()
        for rank in RANKS:
            for suit in SUITS:
                self.append(Card(rank=rank, suit=suit))
        random.shuffle(self)
