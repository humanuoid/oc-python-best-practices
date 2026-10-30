"""Modèle représentant une carte à jouer."""

from dataclasses import dataclass


@dataclass
class Card:
    """Une carte à jouer avec un rang et une couleur.

    Attributes:
        rank: Le rang de la carte (clé de RANKS, ex: "A", "10", "V").
        suit: La couleur de la carte (clé de SUITS, ex: "Trèfle").
        face_down: True si la carte est face cachée, False sinon.
    """

    rank: str
    suit: str
    face_down: bool = False
