#!python

from permutation import permutation
import unittest


class PermutationTest(unittest.TestCase):
    def test_permutation_with_small_integers(self):
        # permutation should return the product n*(n-1)*...*(n-m+1) for n >= m > 0
        assert permutation(10, 0) == 1  # base case
        assert permutation(10, 1) == 10  # base case
        assert permutation(10, 2) == 10*9
        assert permutation(10, 3) == 10*9*8
        assert permutation(10, 4) == 10*9*8*7
        assert permutation(10, 5) == 10*9*8*7*6
        assert permutation(10, 6) == 10*9*8*7*6*5
        assert permutation(10, 7) == 10*9*8*7*6*5*4
        assert permutation(10, 8) == 10*9*8*7*6*5*4*3
        assert permutation(10, 9) == 10*9*8*7*6*5*4*3*2
        assert permutation(10, 10) == 10*9*8*7*6*5*4*3*2*1

    def test_permutation_with_large_integers(self):
        assert permutation(15, 13) == 653837184000
        assert permutation(20, 10) == 670442572800
        assert permutation(25, 17) == 384702630042931200000
        assert permutation(30, 25) == 2210440498434925488635904000000

    def test_permutation_with_negative_integers_n(self):
        # permutation should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            permutation(-1, 7)
            permutation(-5, 5)

    def test_permutation_with_negative_integers_m(self):
        # permutation should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for m < 0'):
            permutation(1, -1)
            permutation(5, -5)

    def test_permutation_with_integers_m_larger_than_integers_n(self):
        # permutation should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n <= m'):
            permutation(4, 5)
            permutation(3, 7)

    def test_permutation_with_floating_point_numbers(self):
        # permutation should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            permutation(2.0, 1)
            permutation(3.14159, 3)
            permutation(9, 3.14159)


if __name__ == '__main__':
    unittest.main()
