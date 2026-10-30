"""Contrôleur du jeu de cartes."""

from oc_python_best_practices.model.deck import Deck
from oc_python_best_practices.model.player import Player
from oc_python_best_practices.service.card_service import CardService
from oc_python_best_practices.service.deck_service import DeckService
from oc_python_best_practices.service.game_service import GameService
from oc_python_best_practices.service.player_service import PlayerService
from oc_python_best_practices.view.game_view import GameView


class GameController:
    """Orchestre le déroulement du jeu.

    Attributes:
        deck: Le jeu de cartes.
        view: La vue console.
        players: La liste des joueurs (créée au lancement).
    """

    def __init__(
        self,
        deck: Deck,
        view: GameView,
    ) -> None:
        self.deck = deck
        self.view = view
        self.players: list[Player] = []

    def run(self) -> None:
        """Crée les joueurs, lance et relance le jeu si demandé."""
        names = self.view.ask_player_names(GameService.MAX_PLAYERS)
        self.players = PlayerService.create(names)
        self.deck = DeckService.create()

        while True:
            DeckService.shuffle(self.deck)
            GameService.distribute(self.deck, self.players)
            for player in self.players:
                self.view.show_drawn_card(player.name, player.hand[-1])

            CardService.reveal(self.players)
            for player in self.players:
                self.view.show_revealed_card(player.name, player.hand[0])

            winner = self.resolve_round()
            self.view.show_round_winner(winner)

            answer = self.view.ask_replay()
            if answer.lower() in ("n", "non"):
                break

            GameService.reset(self.deck, self.players)

        self.view.show_scores(PlayerService.rank(self.players))

    def resolve_round(self) -> Player:
        """Compare les cartes des joueurs et élit le vainqueur.

        Returns:
            Le joueur gagnant la manche.
        """
        winner = self.players[0]
        best_card = winner.hand[0]
        for player in self.players[1:]:
            card = player.hand[0]
            if CardService.strongest(best_card, card) is card:
                winner = player
                best_card = card
        PlayerService.elect(winner)

        return winner
