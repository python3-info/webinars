
from random import randint


class Dragon:
    """Simple game entity representing a dragon.

    Attributes:
        name: Dragon name set at initialization.
        health: Random health points in range 50..100.
        position: Current `(x, y)` position on screen/map.
    """

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
        """Create a dragon with a name, random health, and initial position.

        Args:
            name: Dragon name (positional-only).
            position_x: Initial horizontal coordinate (default: 0).
            position_y: Initial vertical coordinate (default: 0).
        """
        self.name = name
        self.health = randint(50, 100)
        self.position = (position_x, position_y)

    def get_position(self) -> tuple[int, int]:
        """Return current dragon position as `(x, y)`."""
        return self.position

    def set_position(self, x: int, y: int) -> None:
        """Set dragon position to exact coordinates.

        Args:
            x: New horizontal coordinate.
            y: New vertical coordinate.
        """
        self.position = (x, y)

    def move(
        self,
        *,
        left: int = 0,
        right: int = 0,
        up: int = 0,
        down: int = 0,
    ) -> None:
        """Move dragon by directional deltas.

        Horizontal movement:
            - `right` increases x
            - `left` decreases x

        Vertical movement (screen coordinates):
            - `down` increases y
            - `up` decreases y

        Args:
            left: Steps to move left.
            right: Steps to move right.
            up: Steps to move up.
            down: Steps to move down.
        """
        x, y = self.position
        x += right - left
        y += down - up
        self.position = (x, y)
