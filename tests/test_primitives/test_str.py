"""
Tests for the string type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

from keepdelta.types.primitives import DeltaStr


class TestDeltaStr(unittest.TestCase):

    def test_change(self):
        """
        String variable is changed.
        """
        old = "hello"
        new = "world"
        delta = "world"
        self.assertEqual(DeltaStr.create(old, new), delta)
        self.assertEqual(DeltaStr.apply(old, delta), new)

    def test_no_change(self):
        """
        String variable has no changes.
        """
        old = "hello"
        new = "hello"
        delta = "hello"
        self.assertEqual(DeltaStr.create(old, new), delta)
        self.assertEqual(DeltaStr.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
