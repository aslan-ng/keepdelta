import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestDeltaNone(unittest.TestCase):

    def test_0(self):
        old = None
        new = None
        delta = keys['nothing']
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == '__main__':
    unittest.main()