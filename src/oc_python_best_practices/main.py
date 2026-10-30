"""Point d'entrée du jeu de cartes."""

from oc_python_best_practices.controller.game_controller import GameController
from oc_python_best_practices.model.deck import Deck
from oc_python_best_practices.view.game_view import GameView


def main() -> None:
    """Instancie la vue, le modèle et le contrôleur, puis lance le jeu."""
    view = GameView()
    deck = Deck()
    controller = GameController(deck, view)
    controller.run()


if __name__ == "__main__":
    main()
