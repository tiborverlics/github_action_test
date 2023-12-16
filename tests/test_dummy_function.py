import unittest

from src.functions import dummy_function


class TestSquare(unittest.TestCase):
    def test_square_int(self):

        input_number = 3

        expected_result = 9

        actual_result = dummy_function.square_number(input_number)

        self.assertEqual(actual_result, expected_result)

    def test_square_float(self):

        input_number = 2.12

        expected_result = 4.494400000000001

        actual_result = dummy_function.square_number(input_number)

        self.assertEqual(actual_result, expected_result)

    def test_non_numerical_input(self):

        input_number = 'some text'

        with self.assertRaises(Exception) as context:
            dummy_function.square_number(input_number)

        self.assertTrue('Type error - Input should be numerical' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
