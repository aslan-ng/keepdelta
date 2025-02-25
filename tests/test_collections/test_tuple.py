import unittest

from keepdelta.types.collections import DeltaTuple


class TestDeltaTuple(unittest.TestCase):

    def test_0(self):
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
            2: 2.1999999999999997,  # float
            3: 2,  # int
            4: "world",  # str
        }
        self.assertDictEqual(DeltaTuple.create(old, new), delta)
        self.assertTupleEqual(DeltaTuple.apply(old, delta), new)

    def test_1(self):
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


if __name__ == "__main__":
    unittest.main()
