import unittest


class TolerantTestCase(unittest.TestCase):
    """
    Extending unittest.TestCase to add custom assertion methods for collections to address float comparsion tolerance.
    """
    def assertDictAlmostEqual(self, dict1, dict2, places=7, msg=None):
        """
        Asserts that two dictionaries are equal, with tolerance for float comparisons.
        """
        self.assertEqual(set(dict1.keys()), set(dict2.keys()), msg or 'Keys do not match.')
        for key in dict1:
            val1, val2 = dict1[key], dict2[key]
            if isinstance(val1, dict) and isinstance(val2, dict):
                self.assertDictAlmostEqual(val1, val2, places=places, msg=f'Nested dict mismatch at key "{key}"')
            elif isinstance(val1, list) and isinstance(val2, list):
                self.assertListAlmostEqual(val1, val2, places=places, msg=f'Nested list mismatch at key "{key}"')
            elif isinstance(val1, tuple) and isinstance(val2, tuple):
                self.assertTupleAlmostEqual(val1, val2, places=places, msg=f'Nested tuple mismatch at key "{key}"')
            elif isinstance(val1, float) and isinstance(val2, float):
                self.assertAlmostEqual(val1, val2, places=places, msg=f'Key "{key}" mismatch: {val1} != {val2}')
            else:
                self.assertEqual(val1, val2, msg=f'Key "{key}" mismatch: {val1} != {val2}')

    def assertListAlmostEqual(self, list1, list2, places=7, msg=None):
        """
        Asserts that two lists are equal, with tolerance for float comparisons.
        """
        self.assertEqual(len(list1), len(list2), msg or 'List lengths do not match.')
        for i, (val1, val2) in enumerate(zip(list1, list2)):
            if isinstance(val1, float) and isinstance(val2, float):
                self.assertAlmostEqual(val1, val2, places=places, msg=f'Index {i} mismatch: {val1} != {val2}')
            elif isinstance(val1, dict) and isinstance(val2, dict):
                self.assertDictAlmostEqual(val1, val2, places=places, msg=f'Nested dict mismatch at index {i}')
            elif isinstance(val1, list) and isinstance(val2, list):
                self.assertListAlmostEqual(val1, val2, places=places, msg=f'Nested list mismatch at index {i}')
            elif isinstance(val1, tuple) and isinstance(val2, tuple):
                self.assertTupleAlmostEqual(val1, val2, places=places, msg=f'Nested tuple mismatch at index {i}')
            else:
                self.assertEqual(val1, val2, msg=f'Index {i} mismatch: {val1} != {val2}')

    def assertTupleAlmostEqual(self, tuple1, tuple2, places=7, msg=None):
        """
        Asserts that two tuples are equal, with tolerance for float comparisons.
        """
        self.assertEqual(len(tuple1), len(tuple2), msg or 'Tuple lengths do not match.')
        for i, (val1, val2) in enumerate(zip(tuple1, tuple2)):
            if isinstance(val1, float) and isinstance(val2, float):
                self.assertAlmostEqual(val1, val2, places=places, msg=f'Index {i} mismatch: {val1} != {val2}')
            elif isinstance(val1, dict) and isinstance(val2, dict):
                self.assertDictAlmostEqual(val1, val2, places=places, msg=f'Nested dict mismatch at index {i}')
            elif isinstance(val1, list) and isinstance(val2, list):
                self.assertListAlmostEqual(val1, val2, places=places, msg=f'Nested list mismatch at index {i}')
            elif isinstance(val1, tuple) and isinstance(val2, tuple):
                self.assertTupleAlmostEqual(val1, val2, places=places, msg=f'Nested tuple mismatch at index {i}')
            else:
                self.assertEqual(val1, val2, msg=f'Index {i} mismatch: {val1} != {val2}')


if __name__ == '__main__':
    
    class TestAlmostEqual(TolerantTestCase):

        def test_dict(self):
            dict1 = {'a': 1.0, 'b': 2.0, 'c': {'d': 3.0}}
            dict2 = {'a': 1.0, 'b': 2.0000001, 'c': {'d': 3.0000001}}
            self.assertDictAlmostEqual(dict1, dict2, places=5)

    unittest.main()