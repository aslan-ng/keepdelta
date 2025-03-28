"""
Tests for the dictionary type handler.
The result of type handler may differ from the KeepDelta's final result since it's not post-processed.
"""

import unittest

try:
    from .assertEqual import TolerantTestCase
except:
    from assertEqual import TolerantTestCase
from keepdelta.types.collections import DeltaDict
from keepdelta.config import keys


class TestDeltaDict(TolerantTestCase):

    def test_change(self):
        """
        All elements change
        """
        old = {
            "bool": False,  # bool
            "complex": 1 + 1j,  # complex
            "float": 1.1,  # float
            "int": 1,  # int
            "str": "hello",  # str
        }
        new = {
            "bool": True,  # bool
            "complex": 3 + 3j,  # complex
            "float": 3.3,  # float
            "int": 3,  # int
            "str": "world",  # str
        }
        delta = {
            "bool": True,  # bool
            "complex": 2 + 2j,  # complex
            "float": 2.2,  # float
            "int": 2,  # int
            "str": "world",  # str
        }
        self.assertDictAlmostEqual(DeltaDict.create(old, new), delta)
        self.assertDictAlmostEqual(DeltaDict.apply(old, delta), new)

    def test_no_change(self):
        """
        No elements change
        """
        old = {
            "bool": False,  # bool
            "complex": 1 + 1j,  # complex
            "float": 1.1,  # float
            "int": 1,  # int
            "str": "hello",  # str
        }
        new = {
            "bool": False,  # bool
            "complex": 1 + 1j,  # complex
            "float": 1.1,  # float
            "int": 1,  # int
            "str": "hello",  # str
        }
        delta = {}
        self.assertDictEqual(DeltaDict.create(old, new), delta)
        self.assertDictEqual(DeltaDict.apply(old, delta), new)

    def test_add(self):
        """
        Add a new element
        """
        old = {
            "one": 1,
            "two": 2,
        }
        new = {
            "one": 1,
        }
        delta = {"two": keys["delete"]}
        self.assertDictEqual(DeltaDict.create(old, new), delta)
        self.assertDictEqual(DeltaDict.apply(old, delta), new)

    def test_delete(self):
        """
        Delete an old element
        """
        old = {
            "one": 1,
            "two": 2,
        }
        new = {
            "one": 1,
            "two": 2,
            "three": 3,
        }
        delta = {"three": 3}
        self.assertDictEqual(DeltaDict.create(old, new), delta)
        self.assertDictEqual(DeltaDict.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
