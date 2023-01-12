import unittest
import math


def get_power(a, b):
    if 1 > b > 0 < a:
        raise ValueError('incorrect power')
    return a**b


def get_factorial(a):
    if a < 0:
        raise ValueError('you can\'t calculate factorial of the negative number')
    return math.factorial(a)


def get_tan(a):
    if a == math.pi/2:
        raise ValueError('no such tan of this value')
    return math.tan(a)


class TestCalc(unittest.TestCase):

    def test_power(self):
        self.assertEqual(math.pow(3, 2), 9)

    def test_negative_power(self):
        with self.assertRaises(ValueError):
            math.pow(-1, 0.5)

    def test_factorial(self):
        self.assertEqual(math.factorial(4), 24)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            math.factorial(-1)

    def test_get_tan(self):
        self.assertEqual(math.tan(math.pi/4), 0.9999999999999999)

    # def test_no_tan(self):
    #     with self.assertRaises(ValueError):
    #         math.tan(math.pi/2)
#     цей тест не виконується, бо пайтон вміє розраховувати такий тангенс, попри те, чого мене в школі вчили =)


if __name__ == '__main__':
    unittest.main()
