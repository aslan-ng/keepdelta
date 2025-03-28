"""
Tests for the nested data structures.
"""

import unittest

try:
    from .assertEqual import TolerantTestCase
except:
    from assertEqual import TolerantTestCase
from keepdelta.types.collections import Delta
from keepdelta.config import keys


class TestDeltaNested(TolerantTestCase):
    """
    All elements change in a nested data structure
    """
    def test_dict_top(self):
        """
        Top level is dict
        """
        old = {
            "dict": {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            "list": [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            "tuple": (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            "set": {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        }
        new = {
            "dict": {
                "bool": True,
                "int": 3,
                "float": 3.3,
                "complex": 3 + 3j,
                "str": "world",
            },
            "list": [
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            ],
            "tuple": (
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            ),
            "set": {
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            },
        }
        delta = {
            "dict": {
                "bool": True,
                "int": 2,
                "float": 2.2,
                "complex": 2 + 2j,
                "str": "world",
            },
            "list": {
                0: True,  # bool
                1: 2,  # int
                2: 2.2,  # float
                3: (2 + 2j),  # complex
                4: "world",  # str
            },
            "tuple": {
                0: True,  # bool
                1: 2,  # int
                2: 2.2,  # float
                3: (2 + 2j),  # complex
                4: "world",  # str
            },
            "set": {
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
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertDictAlmostEqual(Delta.apply(old, delta), new)

    def test_list_top(self):
        """
        Top level is list
        """
        old = [
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        ]
        new = [
            # dict
            {
                "bool": True,
                "int": 3,
                "float": 3.3,
                "complex": 3 + 3j,
                "str": "world",
            },
            # list
            [
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            ],
            # tuple
            (
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            ),
            # set
            {
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            },
        ]
        delta = {
            # dict
            0: {
                "bool": True,
                "int": 2,
                "float": 2.2,
                "complex": 2 + 2j,
                "str": "world",
            },
            # list
            1: {
                0: True,  # bool
                1: 2,  # int
                2: 2.2,  # float
                3: (2 + 2j),  # complex
                4: "world",  # str
            },
            # tuple
            2: {
                0: True,  # bool
                1: 2,  # int
                2: 2.2,  # float
                3: (2 + 2j),  # complex
                4: "world",  # str
            },
            # set
            3: {
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
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertListAlmostEqual(Delta.apply(old, delta), new)

    def test_tuple_top(self):
        """
        Top level is tuple
        """
        old = (
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        )
        new = (
            # dict
            {
                "bool": True,
                "int": 3,
                "float": 3.3,
                "complex": 3 + 3j,
                "str": "world",
            },
            # list
            [
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            ],
            # tuple
            (
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            ),
            # set
            {
                True,  # bool
                3,  # int
                3.3,  # float
                3 + 3j,  # complex
                "world",  # str
            },
        )
        delta = {
            # dict
            0: {
                "bool": True,
                "int": 2,
                "float": 2.2,
                "complex": 2 + 2j,
                "str": "world",
            },
            # list
            1: {
                0: True,  # bool
                1: 2,  # int
                2: 2.2,  # float
                3: (2 + 2j),  # complex
                4: "world",  # str
            },
            # tuple
            2: {
                0: True,  # bool
                1: 2,  # int
                2: 2.2,  # float
                3: (2 + 2j),  # complex
                4: "world",  # str
            },
            # set
            3: {
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
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertTupleAlmostEqual(Delta.apply(old, delta), new)

class TestDeltaNestedAdd(TolerantTestCase):
    """
    Add a new element to a nested data structure
    """
    def test_dict_top(self):
        """
        Top level is dict
        """
        old = {
            "dict": {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
            },
            "list": [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ],
            "tuple": (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ),
            "set": {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            },
        }
        new = {
            "dict": {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            "list": [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            "tuple": (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            "set": {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        }
        delta = {
            "dict": {
                "str": "hello",  # str
            },
            "list": {
                4: "hello",  # str
            },
            "tuple": {
                4: "hello",  # str
            },
            "set": {
                keys["add to set"]: {
                    "hello",  # str
                },
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertDictAlmostEqual(Delta.apply(old, delta), new)

    def test_list_top(self):
        """
        Top level is list
        """
        old = [
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            },
        ]
        new = [
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        ]
        delta = {
            # dict
            0: {
                "str": "hello",  # str
            },
            # list
            1: {
                4: "hello",  # str
            },
            # tuple
            2: {
                4: "hello",  # str
            },
            # set
            3: {
                keys["add to set"]: {
                    "hello",  # str
                },
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertListAlmostEqual(Delta.apply(old, delta), new)

    def test_tuple_top(self):
        """
        Top level is tuple
        """
        old = (
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            },
        )
        new = (
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        )
        delta = {
            # dict
            0: {
                "str": "hello",  # str
            },
            # list
            1: {
                4: "hello",  # str
            },
            # tuple
            2: {
                4: "hello",  # str
            },
            # set
            3: {
                keys["add to set"]: {
                    "hello",  # str
                },
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertTupleAlmostEqual(Delta.apply(old, delta), new)

class TestDeltaNested(TolerantTestCase):
    """
    Remove an old element from a nested data structure
    """
    def test_dict_top(self):
        """
        Top level is dict
        """
        old = {
            "dict": {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            "list": [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            "tuple": (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            "set": {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        }
        new = {
            "dict": {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
            },
            "list": [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ],
            "tuple": (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ),
            "set": {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            },
        }
        delta = {
            "dict": {
                "str": keys["delete"],  # str
            },
            "list": {
                4: keys["delete"],  # str
            },
            "tuple": {
                4: keys["delete"],  # str
            },
            "set": {
                keys["remove from set"]: {
                    "hello",  # str
                },
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertDictAlmostEqual(Delta.apply(old, delta), new)
        
    def test_list_top(self):
        """
        Top level is list
        """
        old = [
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        ]
        new = [
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            },
        ]
        delta = {
            0: {
                "str": keys["delete"],  # str
            },
            1: {
                4: keys["delete"],  # str
            },
            2: {
                4: keys["delete"],  # str
            },
            3: {
                keys["remove from set"]: {
                    "hello",  # str
                },
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertListAlmostEqual(Delta.apply(old, delta), new)

    def test_tuple_top(self):
        """
        Top level is tuple
        """
        old = (
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
                "str": "hello",
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
                "hello",  # str
            },
        )
        new = (
            # dict
            {
                "bool": False,
                "int": 1,
                "float": 1.1,
                "complex": 1 + 1j,
            },
            # list
            [
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ],
            # tuple
            (
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            ),
            # set
            {
                False,  # bool
                1,  # int
                1.1,  # float
                1 + 1j,  # complex
            },
        )
        delta = {
            0: {
                "str": keys["delete"],  # str
            },
            1: {
                4: keys["delete"],  # str
            },
            2: {
                4: keys["delete"],  # str
            },
            3: {
                keys["remove from set"]: {
                    "hello",  # str
                },
            },
        }
        self.assertDictAlmostEqual(Delta.create(old, new), delta)
        self.assertTupleAlmostEqual(Delta.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()
