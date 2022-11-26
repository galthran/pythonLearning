import unittest
from Fraction import Fraction


class FractionTestCase(unittest.TestCase):
    def test_fraction_add_3(self):
        f = Fraction(2, 3)
        result = f.add(3)
        self.assertEqual(result.nr, 11)
        self.assertEqual(result.dr, 3)

    def test_fraction_add_8(self):
        f = Fraction(2, 3)
        result = f.add(8)
        self.assertEqual(result.nr, 26)
        self.assertEqual(result.dr, 3)


if __name__ == '__main__':
    unittest.main()
