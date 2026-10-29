"""Modèle représentant une main de cartes."""

from oc_python_best_practices.exception.invalid_card_error import (
    InvalidCardError,
)
from oc_python_best_practices.model.card import Card


class Hand(list):
    """Une main de cartes, n'acceptant que des Card."""

    def append(self, card: Card) -> None:
        """Ajoute une carte à la main.

        Args:
            card: La carte à ajouter.

        Raises:
            InvalidCardError: Si l'objet n'est pas une Card.
        """
        if not isinstance(card, Card):
            raise InvalidCardError(card)
        super().append(card)
