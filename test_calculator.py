import unittest
from calculator import add, subtract, multiply, divide, power, modulo, calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_calculate(self):
        self.assertEqual(calculate('add', 5, 5), 10)
        self.assertEqual(calculate('+', 5, 5), 10)
        self.assertEqual(calculate('subtract', 10, 4), 6)
        self.assertEqual(calculate('-', 10, 4), 6)
        self.assertEqual(calculate('multiply', 3, 3), 9)
        self.assertEqual(calculate('*', 3, 3), 9)
        self.assertEqual(calculate('divide', 8, 2), 4)
        self.assertEqual(calculate('/', 8, 2), 4)
        self.assertEqual(calculate('power', 2, 4), 16)
        self.assertEqual(calculate('**', 2, 4), 16)
        self.assertEqual(calculate('modulo', 7, 3), 1)
        self.assertEqual(calculate('%', 7, 3), 1)

        with self.assertRaises(ValueError):
            calculate('invalid_op', 1, 1)

if __name__ == '__main__':
    unittest.main()
