"""
Tests for the none type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestDeltaNone(unittest.TestCase):
    
    def test_none_to_none(self):
        """
        None variable has no changes.
        It is the only possible test for None value without type change.
        """
        old = None
        new = None
        delta = keys["nothing"]
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
