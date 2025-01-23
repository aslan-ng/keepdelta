import unittest

from keepdelta.types.primitives import DeltaBool


class TestDeltaBool(unittest.TestCase):

    def test_0(self):
        old = True
        new = False
        delta = False
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)

    def test_1(self):
        old = False
        new = True
        delta = True
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)

    def test_2(self):
        old = False
        new = False
        delta = False
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)

    def test_3(self):
        old = True
        new = True
        delta = True
        self.assertEqual(DeltaBool.create(old, new), delta)
        self.assertEqual(DeltaBool.apply(old, delta), new)


if __name__ == '__main__':
    unittest.main()