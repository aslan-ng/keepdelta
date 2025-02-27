"""
Tests for the set type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

from keepdelta.config import keys
from keepdelta.types.collections import DeltaSet


class TestDeltaSet(unittest.TestCase):

    def test_change(self):
        """
        All elements are changed
        """
        old = {
            False,  # bool
            1,  # int
            1.1,  # float
            1 + 1j,  # complex
            "hello",  # str
        }
        new = {
            True,  # bool
            3,  # int
            3.3,  # float
            3 + 3j,  # complex
            "world",  # str
        }
        delta = {
            keys["add to set"]: {
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            },
            keys["remove from set"]: {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        }
        self.assertDictEqual(DeltaSet.create(old, new), delta)
        self.assertSetEqual(DeltaSet.apply(old, delta), new)

    def test_no_change(self):
        """
        No elements are changed
        """
        old = {
            False,  # bool
            1,  # int
            1.1,  # float
            1 + 1j,  # complex
            "hello",  # str
        }
        new = {
            False,  # bool
            1,  # int
            1.1,  # float
            1 + 1j,  # complex
            "hello",  # str
        }
        delta = {}
        self.assertDictEqual(DeltaSet.create(old, new), delta)
        self.assertSetEqual(DeltaSet.apply(old, delta), new)

    def test_increase_size(self):
        """
        New element added
        """
        old = {
            2,  # int
            2.2,  # float
            2 + 2j,  # complex
            "hello",  # str
        }
        new = {
            True,  # bool
            2,  # int
            2.2,  # float
            2 + 2j,  # complex
            "hello",  # str
        }
        delta = {
            keys["add to set"]: {
                True,  # bool
            },
        }
        self.assertDictEqual(DeltaSet.create(old, new), delta)
        self.assertSetEqual(DeltaSet.apply(old, delta), new)

    def test_decrease_size(self):
        """
        Old element removed
        """
        old = {
            False,  # bool
            2,  # int
            2.2,  # float
            2 + 2j,  # complex
            "hello",  # str
        }
        new = {
            2,  # int
            2.2,  # float
            2 + 2j,  # complex
            "hello",  # str
        }
        delta = {
            keys["remove from set"]: {
                False,  # bool
            },
        }
        self.assertDictEqual(DeltaSet.create(old, new), delta)
        self.assertSetEqual(DeltaSet.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
