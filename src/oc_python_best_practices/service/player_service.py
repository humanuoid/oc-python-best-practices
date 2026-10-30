"""Service des opérations sur les joueurs."""

from oc_python_best_practices.model.player import Player


class PlayerService:
    """Création, score et classement des joueurs."""

    @staticmethod
    def create(names: list[str]) -> list[Player]:
        """Crée les joueurs à partir d'une liste de noms.

        Args:
            names: Les noms des joueurs.

        Returns:
            La liste des joueurs créés.
        """
        players = []
        for name in names:
            players.append(Player(name=name))

        return players

    @staticmethod
    def elect(winner: Player) -> None:
        """Incrémente le score du vainqueur d'une manche.

        Args:
            winner: Le joueur qui remporte la manche.
        """
        winner.score += 1

    @staticmethod
    def rank(players: list[Player]) -> list[Player]:
        """Classe les joueurs par score décroissant.

        Args:
            players: Les joueurs à classer.

        Returns:
            La liste des joueurs triée du meilleur au moins bon score.
        """

        return sorted(players, key=lambda p: p.score, reverse=True)

    @staticmethod
    def final_winner(players: list[Player]) -> Player:
        """Retourne le vainqueur final (meilleur score).

        Args:
            players: Les joueurs en fin de partie.

        Returns:
            Le joueur avec le plus de points.
        """

        return PlayerService.rank(players)[0]
