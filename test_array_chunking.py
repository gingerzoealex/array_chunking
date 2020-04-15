import unittest
import numpy as np
import array_chunking


class TestCorrectOutput(unittest.TestCase):

    def test_correct_division_1(self):
        result = array_chunking.section_array([1, 3, 4, 5], 2)
        expected = 2
        self.assertEqual(len(result), expected)

    def test_correct_division_2(self):
        result = array_chunking.section_array([1, 2, 3, 4, 5, 6, 7, 8], 2)
        expected = 4
        self.assertEqual(len(result), expected)

    def test_modulo_calculation_1(self):
        result = array_chunking.section_array([1, 2, 3], 2)
        expected = 1
        self.assertEqual(len(result), expected)

    def test_modulo_calculation_2(self):
        result = array_chunking.section_array(
            [1, 2, 3, 4, 5, 6, 5, 3, 4, 5, 6], 3)
        expected = 2
        self.assertEqual(len(result), expected)

    def test_array_of_strings(self):
        result = array_chunking.section_array(
            ['one', 'two', 'three', 'four', 'five', 'six'], 2)
        expected = 3
        self.assertEqual(len(result), expected)

    def test_array_of_strings_2(self):
        result = array_chunking.section_array(
            ['one', 'two', 'three', 'four', 'five'], 2)
        expected = 1
        self.assertEqual(len(result), expected)

    def test_array_of_arrays_1(self):
        result = array_chunking.section_array(
            [[1, 3, 2], [4, 6, 5], [7, 9, 8], [1, 2, 3]], 2)
        expected = 2
        self.assertEqual(len(result), expected)

    def test_array_of_arrays_2(self):
        result = array_chunking.section_array(
            [[1, 3, 2], [4, 6, 5], [7, 9, 8], [1, 2, 3], [3, 4, 5], [7, 6, 8], [1, 2, 3]], 2)
        expected = 1
        self.assertEqual(len(result), expected)


if __name__ == '__main__':
    unittest.main()
