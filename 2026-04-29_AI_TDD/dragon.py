from random import randint


class Dragon:
    name: str
    health: int
    position: tuple[int, int]

    def __init__(
        self,
        name: str,
        /,
        *,
        position_x: int = 0,
        position_y: int = 0,
    ) -> None:
        self.name = name
        self.health = randint(50, 100)
        self.position = (position_x, position_y)
