import unittest
from calculate import calculate
class TestCalculate(unittest.TestCase):
    def test_add_positive(self):
        c = calculate()
        r = c.add(4,3)
        self.assertEqual(r,7)
    def test_add_zeros(self):
        c = calculate()
        r = c.add(0, 0)
        self.assertEqual(r, 0)

if __name__ == '__main__':
    unittest.main()