"""
Tests for the invalid type.
"""

import unittest

import keepdelta as kd


class TestInvalidType(unittest.TestCase):

    def setUp(self):

        class CustomType:
            """
            Saves the integer as binary representation
            """
            def __init__(self, value: int):
                self.value = bin(value)[2:]

            def __eq__(self, value):
                return self.value == value
            
        self.invalid_type = CustomType

    def test_old_invalid_type(self):
        """
        The old variable type is not supported.
        """
        old = self.invalid_type(value=2)
        new = 3
        delta = 3
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_new_invalid_type(self):
        """
        The new variable type is not supported.
        """
        old = 2
        new = self.invalid_type(value=3)
        delta = self.invalid_type(value=3)
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_both_invalid_type(self):
        """
        The new variable type is not supported.
        """
        old = self.invalid_type(value=2)
        new = self.invalid_type(value=3)
        with self.assertRaises(ValueError):
            kd.create(old, new)


if __name__ == "__main__":
    unittest.main()
