import unittest

from keepdelta.types.primitives import DeltaComplex


class TestDeltaComplex(unittest.TestCase):

    def test_0(self):
        old = 1 + 1j
        new = 3 + 3j
        delta = 2 + 2j
        self.assertEqual(DeltaComplex.create(old, new), delta)
        self.assertEqual(DeltaComplex.apply(old, delta), new)

    def test_1(self):
        old = 3 + 3j
        new = 1 + 1j
        delta = -2 - 2j
        self.assertEqual(DeltaComplex.create(old, new), delta)
        self.assertEqual(DeltaComplex.apply(old, delta), new)

    def test_2(self):
        old = 1 + 1j
        new = 1 + 1j
        delta = 0
        self.assertEqual(DeltaComplex.create(old, new), delta)
        self.assertEqual(DeltaComplex.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()