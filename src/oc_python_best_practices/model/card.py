"""Modèle représentant une carte à jouer."""

from dataclasses import dataclass

from oc_python_best_practices.config.ranks import RANKS
from oc_python_best_practices.config.suits import SUITS


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

    def __str__(self) -> str:
        """Affiche la carte (libellé + pictogramme) ou un dos si cachée."""
        if self.face_down:
            return "🂠"
        return f"{RANKS[self.rank]} {SUITS[self.suit]}"

    def __repr__(self) -> str:
        """Représentation développeur de la carte."""
        return (
            f"Card(rank={self.rank!r}, suit={self.suit!r}, "
            f"face_down={self.face_down!r})"
        )
