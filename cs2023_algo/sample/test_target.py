import unittest
from target import gt100


class Test(unittest.TestCase):
    def test_target(self):
        actual = gt100(102)
        self.assertEqual(actual, 100)

    def test_target2(self):
        actual = gt100(99)
        self.assertEqual(actual, 99)
