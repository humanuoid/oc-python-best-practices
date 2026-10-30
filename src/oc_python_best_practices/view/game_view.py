"""Vue console du jeu de cartes."""

from oc_python_best_practices.model.card import Card
from oc_python_best_practices.model.player import Player


class GameView:
    """Présente les informations et récolte les inputs (console)."""

    def show_drawn_card(self, player_name: str, card: Card) -> None:
        """Affiche la carte tirée par un joueur.

        Args:
            player_name: Le nom du joueur.
            card: La carte tirée (face cachée affichée si tel).
        """
        print(f"{player_name} a tiré : {card}")

    def show_revealed_card(self, player_name: str, card: Card) -> None:
        """Affiche la carte révélée d'un joueur.

        Args:
            player_name: Le nom du joueur.
            card: La carte révélée.
        """
        print(f"{player_name} révèle : {card}")

    def show_round_winner(self, winner: Player) -> None:
        """Affiche le gagnant de la manche.

        Args:
            winner: Le joueur qui remporte la manche.
        """
        print(f"{winner.name} remporte la manche !")

    def show_scores(self, players: list[Player]) -> None:
        """Affiche le score de chaque joueur.

        Args:
            players: Les joueurs dont on affiche le score.
        """
        for player in players:
            print(f"{player.name} : {player.score} point(s)")

    def ask_player_names(self, count: int) -> list[str]:
        """Demande les noms des joueurs, l'un après l'autre.

        Args:
            count: Le nombre de joueurs à saisir.

        Returns:
            La liste des noms saisis.
        """
        names = []
        for i in range(count):
            name = input(f"Nom du joueur {i + 1} : ")
            names.append(name)

        return names

    def ask_replay(self) -> bool:
        """Demande si les joueurs veulent rejouer (O par défaut).

        Returns:
            True si oui ou Entrée, False si non.
        """
        answer = input("Voulez-vous rejouer une partie ? (O/n) : ")

        return answer.lower() not in ("n", "non")
