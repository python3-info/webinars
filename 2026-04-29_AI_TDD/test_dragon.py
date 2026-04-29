
"""Unit tests for the Dragon entity.

This test module verifies:
- naming rules during initialization,
- randomized health generation constraints,
- position initialization, retrieval, update, and movement mechanics.
"""

from dragon import Dragon
from unittest import TestCase
from unittest.mock import patch


class TestName(TestCase):
    """Tests related to dragon naming rules."""

    def test_name_default(self):
        """Creating a dragon without a name must raise TypeError."""
        with self.assertRaises(TypeError):
            Dragon()

    def test_name_positional(self):
        """Dragon accepts name as a positional argument."""
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_name_keyword(self):
        """Dragon rejects name passed as a keyword (positional-only API)."""
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa


class TestHealth(TestCase):
    """Tests related to dragon health points."""

    def setUp(self):
        """Create a reusable dragon instance for health assertions."""
        self.dragon = Dragon('Wawelski')

    def test_health_int(self):
        """Health value should be an integer."""
        self.assertIsInstance(self.dragon.health, int)

    def test_health_le_ge(self):
        """Health should be within inclusive bounds [50, 100]."""
        for _ in range(10_000):
            self.assertGreaterEqual(self.dragon.health, 50)
            self.assertLessEqual(self.dragon.health, 100)

    def test_health_in_range(self):
        """Health should belong to Python range representing [50, 100]."""
        self.assertIn(self.dragon.health, range(50, 101))

    def test_health_uses_random_randint(self):
        """Health initialization should rely on dragon.randint()."""
        with patch('dragon.randint', return_value=77) as randint:
            dragon = Dragon('Wawelski')
            self.assertEqual(dragon.health, 77)


class TestPosition(TestCase):
    """Tests related to dragon position handling and movement."""

    def setUp(self):
        """Create a reusable dragon instance at default position."""
        self.dragon = Dragon('Wawelski')

    def test_position_default(self):
        """Default position should be origin (0, 0)."""
        self.assertEqual(self.dragon.position, (0, 0))

    def test_position_positional(self):
        """Position should not be accepted as positional arguments."""
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 50, 100)  # noqa

    def test_position_keyword(self):
        """Position should be configurable via keyword-only arguments."""
        dragon = Dragon('Wawelski', position_x=50, position_y=100)
        self.assertEqual(dragon.position, (50, 100))

    def test_position_get(self):
        """get_position() should return current coordinates."""
        self.dragon.position = (1, 2)
        position = self.dragon.get_position()
        self.assertEqual(position, (1, 2))

    def test_position_set(self):
        """set_position() should update dragon coordinates."""
        self.dragon.set_position(10, 20)
        self.assertEqual(self.dragon.position, (10, 20))

    def test_position_move_right(self):
        """Moving right should increase x coordinate."""
        self.dragon.position = (10, 20)
        self.dragon.move(right=1)
        self.assertEqual(self.dragon.position, (11, 20))

    def test_position_move_left(self):
        """Moving left should decrease x coordinate."""
        self.dragon.position = (10, 20)
        self.dragon.move(left=1)
        self.assertEqual(self.dragon.position, (9, 20))

    def test_position_move_up(self):
        """Moving up should decrease y coordinate (screen coordinates)."""
        self.dragon.position = (10, 20)
        self.dragon.move(up=1)
        self.assertEqual(self.dragon.position, (10, 19))

    def test_position_move_down(self):
        """Moving down should increase y coordinate."""
        self.dragon.position = (10, 20)
        self.dragon.move(down=1)
        self.assertEqual(self.dragon.position, (10, 21))

    def test_position_move_vertical(self):
        """Combined vertical movement should apply both up and down deltas."""
        self.dragon.position = (10, 20)
        self.dragon.move(up=1, down=2)
        self.assertEqual(self.dragon.position, (10, 21))

    def test_position_move_horizontal(self):
        """Combined horizontal movement should apply both left and right deltas."""
        self.dragon.position = (10, 20)
        self.dragon.move(left=1, right=2)
        self.assertEqual(self.dragon.position, (11, 20))

    def test_position_move_omnidirectional(self):
        """Movement should support simultaneous horizontal and vertical deltas."""
        self.dragon.position = (10, 20)
        self.dragon.move(left=1, right=2, up=3, down=4)
        self.assertEqual(self.dragon.position, (11, 21))
