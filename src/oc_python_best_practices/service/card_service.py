"""Service des opérations sur les cartes."""

from oc_python_best_practices.config.ranks import RANKS
from oc_python_best_practices.config.suits import SUITS
from oc_python_best_practices.model.card import Card
from oc_python_best_practices.model.player import Player


class CardService:
    """Comparaison, représentation et révélation des cartes."""

    @staticmethod
    def strongest(card_a: Card, card_b: Card) -> Card:
        """Retourne la carte la plus forte entre deux cartes.

        Compare d'abord les rangs, puis les couleurs en cas d'égalité
        de rang. L'égalité parfaite est impossible (52 cartes uniques).

        Args:
            card_a: Première carte à comparer.
            card_b: Deuxième carte à comparer.

        Returns:
            La carte gagnante.
        """
        ranks = list(RANKS)
        suits = list(SUITS)

        rank_a = ranks.index(card_a.rank)
        rank_b = ranks.index(card_b.rank)

        if rank_a != rank_b:

            return card_a if rank_a < rank_b else card_b

        suit_a = suits.index(card_a.suit)
        suit_b = suits.index(card_b.suit)

        return card_a if suit_a < suit_b else card_b

    @staticmethod
    def repr(card: Card) -> str:
        """Représentation développeur d'une carte.

        Args:
            card: La carte à représenter.

        Returns:
            La chaîne "Card(rank=..., suit=..., face_down=...)".
        """
        return (
            f"Card(rank={card.rank!r}, suit={card.suit!r}, "
            f"face_down={card.face_down!r})"
        )

    @staticmethod
    def reveal(players: list[Player]) -> None:
        """Retourne les cartes des joueurs (face visible).

        Args:
            players: Les joueurs dont on retourne la carte.
        """
        for player in players:
            player.hand[0].face_down = False
