"""Contrôleur du jeu de cartes."""

import random

from oc_python_best_practices.model.deck import Deck
from oc_python_best_practices.model.player import Player
from oc_python_best_practices.service.card_service import get_strongest_card
from oc_python_best_practices.service.game_service import (
    MAX_PLAYERS,
    create_players,
    distribute_cards,
    elect_winner,
    rank_players,
    reset_game,
    reveal_cards,
)
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
        names = self.view.ask_player_names(MAX_PLAYERS)
        self.players = create_players(names)

        while True:
            random.shuffle(self.deck)
            distribute_cards(self.deck, self.players)
            for player in self.players:
                self.view.show_drawn_card(player.name, player.hand[-1])

            reveal_cards(self.players)
            for player in self.players:
                self.view.show_revealed_card(player.name, player.hand[0])

            winner = self.resolve_round()
            self.view.show_round_winner(winner)

            if not self.view.ask_replay():
                break

            reset_game(self.deck, self.players)

        self.view.show_scores(rank_players(self.players))

    def resolve_round(self) -> Player:
        """Compare les cartes des joueurs et élit le vainqueur.

        Returns:
            Le joueur gagnant la manche.
        """
        winner = self.players[0]
        best_card = winner.hand[0]
        for player in self.players[1:]:
            card = player.hand[0]
            if get_strongest_card(best_card, card) is card:
                winner = player
                best_card = card
        elect_winner(winner)

        return winner
