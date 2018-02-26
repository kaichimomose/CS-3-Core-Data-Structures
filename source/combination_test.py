#!python

from combination import combination
import unittest


class CombinationTest(unittest.TestCase):
    def test_combination_with_small_integers(self):
        # combination should return the product (n*(n-1)*...*2*1)/() for n >= m >= 0
        assert combination(10, 0) == 1  # base case
        assert combination(10, 1) == 10  # base case
        assert combination(10, 2) == int((10*9)/(2*1))
        assert combination(10, 3) == int((10*9*8)/(3*2*1))
        assert combination(10, 4) == int((10*9*8*7)/(4*3*2*1))
        assert combination(10, 5) == int((10*9*8*7*6)//(5*4*3*2*1))
        assert combination(10, 6) == int((10*9*8*7*6*5)/(6*5*4*3*2*1))
        assert combination(10, 7) == int((10*9*8*7*6*5*4)/(7*6*5*4*3*2*1))
        assert combination(10, 8) == int((10*9*8*7*6*5*4*3)/(8*7*6*5*4*3*2*1))
        assert combination(10, 9) == int((10*9*8*7*6*5*4*3*2)/(9*8*7*6*5*4*3*2*1))
        assert combination(10, 10) == int((10*9*8*7*6*5*4*3*2*1)/(10*9*8*7*6*5*4*3*2*1))

    def test_combination_with_large_integers(self):
        assert combination(15, 13) == 105
        assert combination(20, 10) == 184756
        assert combination(25, 17) == 1081575
        assert combination(30, 25) == 142506
        assert combination(1500, 1499) == 1500

    def test_combination_with_negative_integers_n(self):
        # combination should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            combination(-1, 7)
            combination(-5, 5)

    def test_combination_with_negative_integers_m(self):
        # combination should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for m < 0'):
            combination(1, -1)
            combination(5, -5)

    def test_combination_with_integers_m_larger_than_integers_n(self):
        # combination should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n <= m'):
            combination(4, 5)
            combination(3, 7)

    def test_combination_with_floating_point_numbers(self):
        # combination should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            combination(2.0, 1)
            combination(3.14159, 3)
            combination(9, 3.14159)


if __name__ == '__main__':
    unittest.main()
