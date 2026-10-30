"""Modèle représentant un joueur."""

from dataclasses import dataclass, field

from oc_python_best_practices.model.hand import Hand


@dataclass
class Player:
    """Un joueur avec un nom, une main et un score.

    Attributes:
        name: Le nom du joueur.
        hand: La main du joueur (vide par défaut).
        score: Le nombre de manches remportées (0 par défaut).
    """

    name: str
    hand: Hand = field(default_factory=Hand)
    score: int = 0
