import unittest
from main import next_power

class TestNextPower(unittest.TestCase):

    def test_two(self):
        self.assertEqual(next_power(2), 2)

    def test_three(self):
        self.assertEqual(next_power(3), 4)

    def test_large(self):
        self.assertEqual(next_power(2557), 4096)

    def test_zero(self):
    	self.assertEqual(next_power(0), 1)

if __name__ == '__main__':
    unittest.main()