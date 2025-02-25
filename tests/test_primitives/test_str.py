import unittest

from keepdelta.types.primitives import DeltaStr


class TestDeltaStr(unittest.TestCase):

    def test_0(self):
        """
        Normal change
        """
        old = "hello"
        new = "world"
        delta = "world"
        self.assertEqual(DeltaStr.create(old, new), delta)
        self.assertEqual(DeltaStr.apply(old, delta), new)

    def test_1(self):
        """
        No changes
        """
        old = "hello"
        new = "hello"
        delta = "hello"
        self.assertEqual(DeltaStr.create(old, new), delta)
        self.assertEqual(DeltaStr.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
