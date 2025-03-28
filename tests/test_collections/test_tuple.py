"""
Tests for the tuple type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

try:
    from .assertEqual import TolerantTestCase
except:
    from assertEqual import TolerantTestCase
from keepdelta.types.collections import DeltaTuple
from keepdelta.config import keys


class TestDeltaTuple(TolerantTestCase):

    def test_change(self):
        """
        All elements change
        """
        old = (
            False,  # bool
            1 + 1j,  # complex
            1.1,  # float
            1,  # int
            "hello",  # str
        )
        new = (
            True,  # bool
            3 + 3j,  # complex
            3.3,  # float
            3,  # int
            "world",  # str
        )
        delta = {
            0: True,  # bool
            1: (2 + 2j),  # complex
            2: 2.2,  # float
            3: 2,  # int
            4: "world",  # str
        }
        self.assertDictAlmostEqual(DeltaTuple.create(old, new), delta)
        self.assertTupleAlmostEqual(DeltaTuple.apply(old, delta), new)

    def test_no_change(self):
        """
        No elements change
        """
        old = (
            False,  # bool
            1 + 1j,  # complex
            1.1,  # float
            1,  # int
            "hello",  # str
        )
        new = (
            False,  # bool
            1 + 1j,  # complex
            1.1,  # float
            1,  # int
            "hello",  # str
        )
        delta = {}
        self.assertDictEqual(DeltaTuple.create(old, new), delta)
        self.assertTupleEqual(DeltaTuple.apply(old, delta), new)

    def test_add(self):
        """
        Add a new element
        """
        old = (
            False,  # bool
            1 + 1j,  # complex
            1.1,  # float
            1,  # int
        )
        new = (
            False,  # bool
            1 + 1j,  # complex
            1.1,  # float
            1,  # int
            "hello",  # str
        )
        delta = {
            4: "hello",
        }
        self.assertDictEqual(DeltaTuple.create(old, new), delta)
        self.assertTupleEqual(DeltaTuple.apply(old, delta), new)

    def test_delete(self):
        """
        Delete an old element
        """
        old = (
            False,  # bool
            1 + 1j,  # complex
            1.1,  # float
            1,  # int
            "hello",  # str
        )
        new = (
            False,  # bool
            1 + 1j,  # complex
            1.1,  # float
            1,  # int
        )
        delta = {
            4: keys["delete"],
        }
        self.assertDictEqual(DeltaTuple.create(old, new), delta)
        self.assertTupleEqual(DeltaTuple.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
