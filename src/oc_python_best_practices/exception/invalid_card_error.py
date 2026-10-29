"""Exception levée quand on tente d'ajouter autre chose qu'une Card."""


class InvalidCardError(TypeError):
    """Levée quand l'objet ajouté à une Hand n'est pas une Card."""

    def __init__(self, obj: object) -> None:
        super().__init__(f"Attendu Card, reçu {type(obj).__name__}")
