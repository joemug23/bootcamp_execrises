import unittest
from prime_number import prime_numbers


class TestPrimeNumber(unittest.TestCase):
    
    def test_argument_is_not_a_string(self):
        # test if the parameter passed is not a string
        with self.assertRaises(TypeError):
            prime_numbers("String")

    def test_argument_is_not_float(self):
        # test if the parameter is not a float
        with self.assertRaises(TypeError):
            prime_numbers(17.5)

    def test_correct_result_10(self):
        self.assertEqual(prime_numbers(10), [2, 3, 5, 7])

    def test_if_empty(self):
        result = prime_numbers(0)
        self.assertEqual(result, [], msg="Should return an empty list for n==0")

    def test_output_of_1(self):
        result = prime_numbers(1)
        self.assertEqual(result, "That is a special case")

    def test_show_param_if_prime(self):
        result = prime_numbers(17)
        self.assertTrue([17 in result], msg="17 should be part of its list of prime numbers")

    def test_negative(self):

        with self.assertRaises(ValueError):
            prime_numbers(-1050)

    def test_if_list(self):
        with self.assertRaises(TypeError):
            prime_numbers([2, 4, 100])

    def test_if_dict(self):
        with self.assertRaises(TypeError):
            prime_numbers({"first": [2, 4, 100]})

    def test_answer_for_100(self):
        result = prime_numbers(100)
        self.assertEquals(result, [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97], msg="Should return list of prime numbers below 100")