"""
Tests for the integer type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

from keepdelta.types.primitives import DeltaInt


class TestDeltaInt(unittest.TestCase):

    def test_increase(self):
        """
        Integer variable increases.
        """
        old = 1
        new = 3
        delta = 2
        self.assertEqual(DeltaInt.create(old, new), delta)
        self.assertEqual(DeltaInt.apply(old, delta), new)

    def test_decrease(self):
        """
        Integer variable decreases.
        """
        old = 3
        new = 1
        delta = -2
        self.assertEqual(DeltaInt.create(old, new), delta)
        self.assertEqual(DeltaInt.apply(old, delta), new)

    def test_no_change(self):
        """
        Integer variable has no changes.
        """
        old = 1
        new = 1
        delta = 0
        self.assertEqual(DeltaInt.create(old, new), delta)
        self.assertEqual(DeltaInt.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
