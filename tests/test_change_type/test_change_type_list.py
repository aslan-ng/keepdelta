import unittest

import keepdelta as kd


class TestChangeTypeList(unittest.TestCase):

    def test_none_to_list(self):
        old = None
        new = [
            "hello",
            True,
        ]
        delta = [
            "hello",
            True,
        ]
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_list_to_none(self):
        old = [
            "hello",
            True,
        ]
        new = None
        delta = None
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()