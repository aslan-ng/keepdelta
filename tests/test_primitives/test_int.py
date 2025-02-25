import unittest

from keepdelta.types.primitives import DeltaInt


class TestDeltaInt(unittest.TestCase):

    def test_0(self):
        old = 1
        new = 3
        delta = 2
        self.assertEqual(DeltaInt.create(old, new), delta)
        self.assertEqual(DeltaInt.apply(old, delta), new)

    def test_1(self):
        old = 3
        new = 1
        delta = -2
        self.assertEqual(DeltaInt.create(old, new), delta)
        self.assertEqual(DeltaInt.apply(old, delta), new)

    def test_2(self):
        old = 1
        new = 1
        delta = 0
        self.assertEqual(DeltaInt.create(old, new), delta)
        self.assertEqual(DeltaInt.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
