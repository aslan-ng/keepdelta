"""
Tests for the float type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

from keepdelta.types.primitives import DeltaFloat


class TestDeltaFloat(unittest.TestCase):

    def test_increase(self):
        """
        Float variable increases.
        """
        old = 1.1
        new = 3.3
        delta = 2.2
        self.assertAlmostEqual(DeltaFloat.create(old, new), delta, places=5)
        self.assertAlmostEqual(DeltaFloat.apply(old, delta), new, places=5)

    def test_decrease(self):
        """
        Float variable decreases.
        """
        old = 3.3
        new = 1.1
        delta = -2.2
        self.assertAlmostEqual(DeltaFloat.create(old, new), delta, places=5)
        self.assertAlmostEqual(DeltaFloat.apply(old, delta), new, places=5)

    def test_no_change(self):
        """
        Float variable has no changes.
        """
        old = 1.1
        new = 1.1
        delta = 0.0
        self.assertEqual(DeltaFloat.create(old, new), delta)
        self.assertEqual(DeltaFloat.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
