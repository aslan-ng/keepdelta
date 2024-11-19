import unittest

from keepdelta.types.collections import DeltaDict


class TestDeltaDict(unittest.TestCase):

    def test_0(self):
        old = {
            'bool': False,
            'int': 1,
            'float': 1.1,
            'complex': 1 + 1j,
            'str': 'hello',
        }
        new = {
            'bool': True,
            'int': 3,
            'float': 3.3,
            'complex': 3 + 3j,
            'str': 'world',
        }
        delta = {
            'bool': True,
            'int': 2,
            'float': 2.1999999999999997,
            'complex': 2 + 2j,
            'str': 'world',
        }
        self.assertDictEqual(DeltaDict.create(old, new), delta)
        self.assertDictEqual(DeltaDict.apply(old, delta), new)

    def test_1(self):
        old = {
            'bool': False,
            'int': 1,
            'float': 1.1,
            'complex': 1 + 1j,
            'str': 'hello',
        }
        new = {
            'bool': False,
            'int': 1,
            'float': 1.1,
            'complex': 1 + 1j,
            'str': 'hello',
        }
        delta = {}
        self.assertDictEqual(DeltaDict.create(old, new), delta)
        self.assertDictEqual(DeltaDict.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()