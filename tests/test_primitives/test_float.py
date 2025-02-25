import unittest

from keepdelta.types.primitives import DeltaFloat


class TestDeltaFloat(unittest.TestCase):

    def test_0(self):
        old = 1.1
        new = 3.3
        delta = 2.2
        self.assertAlmostEqual(DeltaFloat.create(old, new), delta, places=5)
        self.assertAlmostEqual(DeltaFloat.apply(old, delta), new, places=5)

    def test_1(self):
        old = 3.3
        new = 1.1
        delta = -2.2
        self.assertAlmostEqual(DeltaFloat.create(old, new), delta, places=5)
        self.assertAlmostEqual(DeltaFloat.apply(old, delta), new, places=5)

    def test_2(self):
        old = 1.1
        new = 1.1
        delta = 0.0
        self.assertEqual(DeltaFloat.create(old, new), delta)
        self.assertEqual(DeltaFloat.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
