"""Service de comparaison des cartes."""

from oc_python_best_practices.config.ranks import RANKS
from oc_python_best_practices.config.suits import SUITS
from oc_python_best_practices.model.card import Card


def get_strongest_card(card_a: Card, card_b: Card) -> Card:
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
