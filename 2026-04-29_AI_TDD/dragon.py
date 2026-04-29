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

    def get_position(self) -> tuple[int, int]:
        return self.position

    def set_position(self, x: int, y: int) -> None:
        self.position = (x, y)

    def move(
        self,
        *,
        left: int = 0,
        right: int = 0,
        up: int = 0,
        down: int = 0,
    ) -> None:
        x, y = self.position
        x += right - left
        y += down - up
        self.position = (x, y)
