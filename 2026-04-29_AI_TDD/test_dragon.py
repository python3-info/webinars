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
