from dragon import Dragon
from unittest import TestCase
from unittest.mock import patch


class TestName(TestCase):
    def test_name_default(self):
        with self.assertRaises(TypeError):
            Dragon()

    def test_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa


class TestHealth(TestCase):
    def setUp(self):
        self.dragon = Dragon('Wawelski')

    def test_health_int(self):
        self.assertIsInstance(self.dragon.health, int)

    def test_health_le_ge(self):
        for _ in range(10_000):
            self.assertGreaterEqual(self.dragon.health, 50)
            self.assertLessEqual(self.dragon.health, 100)

    def test_health_in_range(self):
        self.assertIn(self.dragon.health, range(50, 101))

    def test_health_uses_random_randint(self):
        with patch('dragon.randint', return_value=77) as randint:
            dragon = Dragon('Wawelski')
            self.assertEqual(dragon.health, 77)


class TestPosition(TestCase):
    def setUp(self):
        self.dragon = Dragon('Wawelski')

    def test_position_default(self):
        self.assertEqual(self.dragon.position, (0, 0))

    def test_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 50, 100)  # noqa

    def test_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=50, position_y=100)
        self.assertEqual(dragon.position, (50, 100))

    def test_position_get(self):
        self.dragon.position = (1, 2)
        position = self.dragon.get_position()
        self.assertEqual(position, (1, 2))

    def test_position_set(self):
        self.dragon.set_position(10, 20)
        self.assertEqual(self.dragon.position, (10, 20))

    def test_position_move_right(self):
        self.dragon.position = (10, 20)
        self.dragon.move(right=1)
        self.assertEqual(self.dragon.position, (11, 20))

    def test_position_move_left(self):
        self.dragon.position = (10, 20)
        self.dragon.move(left=1)
        self.assertEqual(self.dragon.position, (9, 20))

    def test_position_move_up(self):
        self.dragon.position = (10, 20)
        self.dragon.move(up=1)
        self.assertEqual(self.dragon.position, (10, 19))

    def test_position_move_down(self):
        self.dragon.position = (10, 20)
        self.dragon.move(down=1)
        self.assertEqual(self.dragon.position, (10, 21))

    def test_position_move_vertical(self):
        self.dragon.position = (10, 20)
        self.dragon.move(up=1, down=2)
        self.assertEqual(self.dragon.position, (10, 21))

    def test_position_move_horizontal(self):
        self.dragon.position = (10, 20)
        self.dragon.move(left=1, right=2)
        self.assertEqual(self.dragon.position, (11, 20))

    def test_position_move_omnidirectional(self):
        self.dragon.position = (10, 20)
        self.dragon.move(left=1, right=2, up=3, down=4)
        self.assertEqual(self.dragon.position, (11, 21))
