"""
Tests for the boolean type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

from keepdelta.types.primitives import DeltaBool


class TestDeltaBool(unittest.TestCase):

    def test_true_to_false(self):
        """
        Boolean variable was true then changed to false.
        """
        old = True
        new = False
        delta = False
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)

    def test_false_to_true(self):
        """
        Boolean variable was false then changed to true.
        """
        old = False
        new = True
        delta = True
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)

    def test_false_to_false(self):
        """
        Boolean variable is false and has not changed.
        """
        old = False
        new = False
        delta = False
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)

    def test_true_to_true(self):
        """
        Boolean variable is true and has not changed.
        """
        old = True
        new = True
        delta = True
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
