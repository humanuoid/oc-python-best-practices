"""Modèle représentant une main de cartes."""

from dataclasses import dataclass, field

from oc_python_best_practices.exception.invalid_card_error import (
    InvalidCardError,
)
from oc_python_best_practices.model.card import Card


@dataclass
class Hand:
    """Une main de cartes.

    N'accepte que des Card, quelle que soit la voie d'écriture.

    Attributes:
        _cards: Les cartes de la main.
    """

    _cards: list[Card] = field(default_factory=list)

    @property
    def cards(self) -> tuple[Card, ...]:
        """Les cartes de la main, en lecture seule."""
        return tuple(self._cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int) -> Card:
        return self._cards[index]

    def __iter__(self):
        return iter(self._cards)

    def __setitem__(self, index: int, card: Card) -> None:
        """Remplace une carte, après validation du type.

        Raises:
            InvalidCardError: Si l'objet n'est pas une Card.
        """
        if not isinstance(card, Card):
            raise InvalidCardError(card)
        self._cards[index] = card

    def append(self, card: Card) -> None:
        """Ajoute une carte à la main, après validation du type.

        Raises:
            InvalidCardError: Si l'objet n'est pas une Card.
        """
        if not isinstance(card, Card):
            raise InvalidCardError(card)
        self._cards.append(card)

    def extend(self, cards: tuple[Card, ...]) -> None:
        """Ajoute plusieurs cartes à la main, chacune validée.

        Args:
            cards: Les cartes à ajouter.

        Raises:
            InvalidCardError: Si l'un des objets n'est pas une Card.
        """
        for card in cards:
            self.append(card)

    def pop(self) -> Card:
        """Retire et retourne la dernière carte de la main."""
        return self._cards.pop()

    def clear(self) -> None:
        """Vide la main."""
        self._cards.clear()
