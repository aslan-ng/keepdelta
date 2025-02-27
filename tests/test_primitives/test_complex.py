"""
Tests for the complex type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

from keepdelta.types.primitives import DeltaComplex


class TestDeltaComplex(unittest.TestCase):

    def test_increase(self):
        """
        Complex variable increases.
        """
        old = 1 + 1j
        new = 3 + 3j
        delta = 2 + 2j
        self.assertEqual(DeltaComplex.create(old, new), delta)
        self.assertEqual(DeltaComplex.apply(old, delta), new)

    def test_decrease(self):
        """
        Complex variable decreases.
        """
        old = 3 + 3j
        new = 1 + 1j
        delta = -2 - 2j
        self.assertEqual(DeltaComplex.create(old, new), delta)
        self.assertEqual(DeltaComplex.apply(old, delta), new)

    def test_no_change(self):
        """
        Complex variable has no changes.
        """
        old = 1 + 1j
        new = 1 + 1j
        delta = 0
        self.assertEqual(DeltaComplex.create(old, new), delta)
        self.assertEqual(DeltaComplex.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
