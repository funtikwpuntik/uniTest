import unittest
from parameterized import parameterized

from app.error import InvalidInputException
from app.main import Calculator

class TestLogCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    @parameterized.expand(
        [
            ('test_log_int', 2, 4, 0.5),
            ('test_log_float', 4, 2, 2.0),
        ]
    )
    def test_log(self, name, a, b, expected_result):
        actual_result = self.calc.log(a, b)
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [
            ('test_log_string', '2', 4, TypeError),
            ('test_log_bool', 4, None, TypeError),
        ]
    )
    def test_log_invalid_values(self, name, a, b, expected_result):

        with self.assertRaises(expected_result):
            self.calc.log(a, b)

    @parameterized.expand(
        [
            ('test_log_a<=0', -1, 4, InvalidInputException),
            ('test_log_a<=0', 0, 4, InvalidInputException),
            ('test_log_a=1', 1, 3, InvalidInputException),
            ('test_log_base<=0', 2, 0, InvalidInputException),
            ('test_log_base<=0', 2, -1, InvalidInputException),
        ]
    )
    def test_log_invalid_input(self, name, a, b, expected_result):

        with self.assertRaises(expected_result):
            self.calc.log(a, b)


if __name__ == "__main__":
    unittest.main()