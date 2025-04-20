"""
Tests for the equal inputs.
"""

import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestNoChange(unittest.TestCase):

    def test_no_change(self):
        old = 1
        new = 1
        delta = keys["nothing"]
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()