import unittest
from SimpleArithmetic import multiply


class SimpleArithmeticUnitTests(unittest.TestCase):
    def test_multiply_function_with_two_zeros(self):
        # arrange
        num1 = 0
        num2 = 0
        expected_result = 0

        # act
        actual_result = multiply(num1, num2)

        # assert
        self.assertEqual(expected_result, actual_result)

    def test_multiply_function_passing_one_zero_and_a_positive_number(self):
        # arrange
        num1 = 0
        num2 = 8
        expected_result = 0

        # act
        actual_result = multiply(num1, num2)

        # assert
        self.assertEqual(expected_result, actual_result)

    def test_multiply_function_passing_a_positive_number_and_a_zero(self):
        # arrange
        num1 = 8
        num2 = 0
        expected_result = 0

        # act
        actual_result = multiply(num1, num2)

        # assert
        self.assertEqual(expected_result, actual_result)


    def test_multiply_function_with_two_positive_numbers(self):
        # arrange
        num1 = 7
        num2 = 8
        expected_result = 56

        # act
        actual_result = multiply(num1, num2)

        # assert
        self.assertEqual(expected_result, actual_result)

    def test_multiply_function_with_a_negative_values_and_a_positive_value(self):
        # arrange
        num1 = -7
        num2 = 8
        expected_result = -56

        # act
        actual_result = multiply(num1, num2)

        # assert
        self.assertEqual(expected_result, actual_result)

    def test_multiply_function_with_a_positive_values_and_a_negative_value(self):
        # arrange
        num1 = 7
        num2 = -8
        expected_result = -56

        # act
        actual_result = multiply(num1, num2)

        # assert
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
